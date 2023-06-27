import sys
import os
sys.path.append(os.getcwd() + "/python_files_merger")

import merger
import circular_dependencies

__version__ = "0.0.1"


def merge(args):
    return merger.merge(args)


def find_circular_dependencies(args):
    return circular_dependencies.find(args)
