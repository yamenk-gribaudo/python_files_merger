from merger import merge
from circular_dependencies import find

__version__ = "1.0.1"

def find_circular_dependencies(args):
    return find(args)
