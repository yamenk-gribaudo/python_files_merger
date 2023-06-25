[![Build Status](https://secure.travis-ci.org/yamenk-gribaudo/python_file_merger.svg?branch=master)](http://travis-ci.org/christophevg/python_file_merger)
[![Documentation Status](https://readthedocs.org/projects/python_file_merger/badge/?version=latest)](https://python_file_merger.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/yamenk-gribaudo/python_file_merger/badge.svg?branch=master)](https://coveralls.io/github/yamenk-gribaudo/python_file_merger?branch=master)

# Test
    python -B -m unittest

# Merge files
    python python_files_merger/merger.py <folder>/*

# TODOs:
- Make the test work, right now, the circular_dependencies import in merger and the remove_comments import in parser are failing.
- Add test for remove_comments
- Add test for merger
- Add test for parser
- Improve circular dependencies (CDs) algorithm, it should return all the CDs instead of just the first one
- Add definitions collition before merging
- Add output filepath as config argumment
- Add things to repo to be able to publish it
