import parser
import os
import astunparse
import re
import circular_dependencies
import ast

WARNING = '\033[33m'
ENDC = '\033[0m'


def merge(args):
    # Get file paths using args
    file_paths = set()
    no_python_files = False
    for arg in args:
        if os.path.exists(arg) and os.path.isfile(arg):
            if arg.split(".")[len(arg.split("."))-1] == 'py':
                file_paths.add(arg)
            else:
                no_python_files = True
        else:
            print(WARNING + arg + " do not exist as path" + ENDC)

    if len(file_paths) == 0:
        print(WARNING + "No files to merge" + ENDC)
        if no_python_files:
            print(WARNING + "There are some files not ending with '.py'" + ENDC)

    # Parse files
    parsed_files = []
    for file_path in file_paths:
        parsed_files.append(parser.parse_file(file_path))

    # Replace dependencies from 'from X import Y'
    for file in parsed_files:
        for import_ in file['from_imports']:
            for node in file['nodes']:
                for parsed_file in parsed_files:
                    if import_['module'] == parsed_file['name']:
                        if import_['asname'] == "*":
                            for other_file_definition in parsed_file['definitions']:
                                for node_dependency in node['dependencies']:
                                    if other_file_definition == node_dependency and node_dependency not in file['definitions']:
                                        node['dependencies'].remove(node_dependency)
                                        node['dependencies'].add(parsed_file['name'] + "." + node_dependency)
                        else:
                            if import_['asname'] in node['dependencies']:
                                string = astunparse.unparse(node['node'])
                                regex = "(?<![a-zA-Z0-9_.])" + import_['asname'] + "(?![a-zA-Z0-9_])"
                                node['node'] = ast.parse(re.sub(regex, import_['name'], string))
                                for dependency in node['dependencies']:
                                    if dependency == import_['asname']:
                                        node['dependencies'].remove(dependency)
                                        node['dependencies'].add(import_['module'] + "." + import_['name'])

    # Replace dependencies from other files: <dependency> -> <imported_name>.<dependency>
    for file in parsed_files:
        for file2 in parsed_files:
            if file['filepath'] != file2['filepath']:
                for import_ in file['imports']:
                    if import_['name'] == file2['name']:
                        for node in file['nodes']:
                            accumulator = set()
                            for dependency in node['dependencies']:
                                if dependency == import_['asname']:
                                    for imported_definition in file2['definitions']:  
                                        string = astunparse.unparse(node['node'])
                                        regex = "(?<![a-zA-Z_.])" + import_['asname'] + "." + imported_definition + "(?![a-zA-Z_])"
                                        result = re.search(regex, string)
                                        if result: 
                                            node['node'] = ast.parse(re.sub(regex, imported_definition, string))
                                            for dep in node['dependencies']:
                                                if dep == import_['asname']:
                                                    accumulator.add(import_['name'] + "." + imported_definition)
                            node['dependencies'] =  node['dependencies'].union(accumulator)
                            if import_['asname'] in node['dependencies']:
                                node['dependencies'].remove(import_['asname'])

    # Replace dependencies from same file: <dependency> -> <name>.<dependency>
    for file in parsed_files:
        for node in file['nodes']:
            for dependency in node['dependencies']:
                if len(dependency.split('.')) == 1:
                    node['dependencies'].remove(dependency)
                    node['dependencies'].add(file['name'] + "." + dependency)  
            for definition in node['definitions']:
                if len(definition.split('.')) == 1:
                    node['definitions'].remove(definition)
                    node['definitions'].add(file['name'] + "." + definition)

    # Combine nodes
    all_nodes = []
    for file in parsed_files:
        for node in file['nodes']:
            all_nodes.append(node)     

    # Add imports to final_string
    final_string = ""
    used_blocks = set()  
    removed_nodes = []
    from_future_import_node = ast.ImportFrom()
    setattr(from_future_import_node, 'module', '__future__')
    setattr(from_future_import_node, 'names', [])
    setattr(from_future_import_node, 'level', 0)
    from_import_string = ""
    import_node = ast.Import()
    setattr(import_node, 'names', [])
    for node in all_nodes:
        if isinstance(node['node'], ast.ImportFrom):
            removed_nodes.append(node)
            should_add_node = True
            for parsed_file in parsed_files:
                if parsed_file['name'] == node['node'].module:
                    should_add_node = False
            if should_add_node:
                if node['node'].module == "__future__":
                    for name in node['node'].names:
                        name_already_in = False
                        for name_in_import_node in from_future_import_node.names:
                            if name.name == name_in_import_node.name and name.asname == name_in_import_node.asname:
                                name_already_in = True
                        if not name_already_in:
                            from_future_import_node.names.append(name)
                else:
                    string = astunparse.unparse(node['node']).strip()
                    if string not in used_blocks:
                        used_blocks.add(string)
                        from_import_string += string + "\n"
        if isinstance(node['node'], ast.Import):
            removed_nodes.append(node)
            import_nodes_to_be_removed = []
            for name in node['node'].names:
                for parsed_file in parsed_files:
                    if parsed_file['name'] == name.name:
                        import_nodes_to_be_removed.append(name)
            for import_node_to_be_removed in import_nodes_to_be_removed:
                node['node'].names.remove(import_node_to_be_removed)
            if len(node['node'].names) > 0:
                for name in node['node'].names:
                    name_already_in = False
                    for name_in_import_node in import_node.names:
                        if name.name == name_in_import_node.name and name.asname == name_in_import_node.asname:
                            name_already_in = True
                    if not name_already_in:
                        import_node.names.append(name)
    if len(from_future_import_node.names) > 0:
        final_string += astunparse.unparse(from_future_import_node).strip() + "\n"
    final_string += from_import_string
    if len(import_node.names) > 0:
        final_string += astunparse.unparse(import_node).strip() + "\n"
    for node in removed_nodes:
        all_nodes.remove(node)

    # Extract main module blocks to merge them and put them at the end
    removed_nodes = []
    main_block = ast.If()
    setattr(main_block, 'test', None)
    setattr(main_block, 'body', [])
    setattr(main_block, 'orelse', None)
    for node in all_nodes:
        if isinstance(node['node'], ast.If):
            if astunparse.unparse(node['node'].test).strip() == "(__name__ == '__main__')":
                if main_block.test == None:
                    main_block.test = node['node'].test
                removed_nodes.append(node)
                main_block.body += node['node'].body
    for node in removed_nodes:
        all_nodes.remove(node)    

    # Add everything else to final_string
    removed_nodes = []
    last_all_nodes_len = len(all_nodes)
    while True:     
        # Check if a all dependencies of a blocked and stisfied (not in any definition), and,
        # in that case, add it to the final string and remove the node from the nodes to be merged
        for node in all_nodes:
            depedencies_stisfied = True
            for dependency in node['dependencies']:
                for node2 in all_nodes:
                    if dependency in node2['definitions']:
                        depedencies_stisfied = False
            if depedencies_stisfied:
                string = astunparse.unparse(node['node']).strip()
                removed_nodes.append(node)
                if string not in used_blocks:
                    used_blocks.add(string)
                    final_string += string + "\n"
        for node in removed_nodes:
            all_nodes.remove(node)
        removed_nodes = []
        if len(all_nodes) == last_all_nodes_len:
            break
        else:
            last_all_nodes_len = len(all_nodes)

    if len(all_nodes) > 0:
        # Check cicular dependencies here
        circular_dependencies_object = []
        for node in all_nodes:
            for dependency in node['definitions']:
                circular_dependencies_object.append({'parents': [dependency], 'dependencies': list(node['dependencies'])})
        print(WARNING + "There are circular dependencies in some of the blocks to be merged: " + " -> ".join(circular_dependencies.find(circular_dependencies_object)) + ENDC)
        # Merge block with circular dependencies anyway
        for node in all_nodes:
            if node not in removed_nodes:
                string = astunparse.unparse(node['node']).strip()
                if string not in used_blocks:
                    used_blocks.add(string)
                    final_string += string + "\n"

    # Add main block
    final_string += astunparse.unparse(main_block).strip() + "\n"
    
    return final_string
