from python_files_merger import circular_dependencies, merger

__version__ = "0.0.1"

def merge(args):
    return merger.merge(args)


def find_circular_dependencies(args):
    return circular_dependencies.check(args)
