from .circular_dependencies import find
from .merger import merge as mergermerge

__version__ = "1.0.9"


def merge(args):
    return mergermerge(args)


def find_circular_dependencies(args):
    return find(args)
