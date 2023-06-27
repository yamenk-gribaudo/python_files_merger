import ast
import os
from glob import glob
import builtins
import remove_comments
import ast_scope

WARNING = '\033[33m'
ENDC = '\033[0m'
built_ins = dir(__builtins__) + dir(builtins) + ["__builtins__"]
built_ins.append(None)


def get_definitions(root):
    definitions = set()
    for node in ast.walk(root):
        if node.scope == "global":
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for name in node.names:
                    final_name = name.asname if name.asname else name.name
                    if final_name != "*":  # This catchs the 'from <x> import *'
                        definitions.add(final_name)
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                definitions.add(node.name)
            if isinstance(node, ast.ClassDef):
                definitions.add(node.name)
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    for target_node in ast.walk(target):
                        if hasattr(target_node, 'id'):
                            definitions.add(target_node.id)
            if isinstance(node, ast.AnnAssign):
                for target_node in ast.walk(node.target):
                    if hasattr(target_node, 'id'):
                        definitions.add(target_node.id)
    return definitions


# This could be done a lot better
def get_dependencies(node, definitions):
    scope_info = ast_scope.annotate(node)
    all_definitions = scope_info.static_dependency_graph.nodes()

    dependencies = set()
    for all_definition in all_definitions:
        if all_definition not in definitions and all_definition not in built_ins:
            dependencies.add(all_definition)
    return dependencies


def parse_root(root, global_definitions):
    nodes = []
    for node in root.body:
        definitions = get_definitions(node)
        dependencies = get_dependencies(node, definitions)
        for definition in definitions:
            if definition in global_definitions:
                global_definitions.remove(definition)
        nodes.append({
            'node': node, 
            'definitions': definitions, 
            'dependencies': dependencies
        })
    if len(global_definitions) > 0:
        print(WARNING + "Some global symbol definitions couldnt be found: '" + "', '".join(global_definitions) + "'. You should report this." + ENDC)
    return nodes


def get_imports(string):
    imports = []
    root = ast.parse(string)
    for node in ast.walk(root):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.append({'name': name.name, 'asname': name.asname if name.asname else name.name})
    return imports


def get_from_imports(string):
    imports = []
    root = ast.parse(string)
    for node in ast.walk(root):
        if isinstance(node, ast.ImportFrom):
            for name in node.names:
                imports.append({'name': name.name, 'asname': name.asname if name.asname else name.name, 'module': node.module })
    return imports


def add_scope(root):
    for node in ast.walk(root):
        scope = "global"
        current_node = node.parent
        while True:
            if current_node:
                if isinstance(current_node, ast.FunctionDef) or isinstance(current_node, ast.AsyncFunctionDef) or isinstance(current_node, ast.ClassDef):
                    scope = "local"
                current_node = current_node.parent
            else:
                break
        node.scope = scope


def and_parent(root):
    for node in ast.walk(root):
        for child in ast.iter_child_nodes(node):
            child.parent = node
    root.parent = None


def parse_string(string):
    string_without_comments = remove_comments.remove_comments(string)
    root = ast.parse(string_without_comments)
    and_parent(root)
    add_scope(root)
    global_definitions = get_definitions(root)
    parsed_nodes = parse_root(root, global_definitions)
    return parsed_nodes


def parse_file(pathname):
    file = open(pathname)
    string = file.read()
    parsed_file = {}
    parsed_file["name"] = file.name.split("/")[len(file.name.split("/"))-1].split(".")[len(file.name.split("."))-2]
    parsed_file["filepath"] = file.name
    parsed_file["imports"] =  get_imports(string)
    parsed_file["from_imports"] =  get_from_imports(string)
    parsed_file["nodes"] =  parse_string(string)
    definitions = set()
    for node in parsed_file["nodes"]:
        for dep in node['definitions']:
            definitions.add(dep)
    parsed_file["definitions"] = definitions
    return parsed_file


def parse(args):
    # Get file paths using args
    file_paths = set()
    for arg in args:
        if os.path.exists(arg):
            file_paths_list = glob(arg, recursive=True)
            for file_path in file_paths_list:
                if os.path.exists(file_path) and os.path.isfile(file_path) and file_path.split(".")[len(file_path.split("."))-1] == 'py':
                    file_paths.add(file_path)
        else:
            raise Exception(arg + " do not exist, posible paths are \"" + "\",\"".join(os.listdir('.')) +
                            "\" and its decendents")
    # Parse files
    parsed_files = []
    for file_path in file_paths:
        parsed_files.append(parse_file(file_path))
    return parsed_files
