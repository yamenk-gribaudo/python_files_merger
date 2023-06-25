import json

def check_format(input):
    if isinstance(input, list):
        for inp in input:
            if 'parents' not in inp or 'dependencies' not in inp:
                raise TypeError("Input must be formatted as [{'parents':['a',...], 'dependencies':['b',...]},...]")
            
def find_dependencies(dependencies, parent):
    for dependency in dependencies:
        if dependency['parents'] == [parent]:
            return dependency["dependencies"]
    return []

def check(dependencies, objects=[], iterations=0):
    check_format(dependencies)
    check_format(objects)
    if iterations > len(dependencies):
        return []
    if len(objects) == 0:
        objects = json.loads(json.dumps(dependencies))
    new_objects = []
    for object in objects:
        for parent in object['parents']:
            for dependency in object['dependencies']:
                if parent == dependency:
                    return object['parents'] + [parent]
                new_objects.append({"parents": object['parents'] + [
                                   dependency], 'dependencies': find_dependencies(dependencies, dependency)})
    return check(dependencies, new_objects, iterations+1)
