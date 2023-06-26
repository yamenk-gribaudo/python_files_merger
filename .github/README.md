[![Build Status](https://secure.travis-ci.org/yamenk-gribaudo/python_files_merger.svg?branch=main)](http://travis-ci.org/christophevg/python_files_merger)
[![Documentation Status](https://readthedocs.org/projects/python_files_merger/badge/?version=latest)](https://python_files_merger.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/yamenk-gribaudo/python_files_merger/badge.svg?branch=main)](https://coveralls.io/github/yamenk-gribaudo/python_files_merger?branch=main)

# Test
    python -m unittest

# Merge files
    python python_files_merger -o output.py <files_to_be_merged>
ex: 
    python python_files_merger -o output.py src/*

    python python_files_merger src/lorem.py src/ipsum.py

# TODOs:
- Add test for remove_comments
- Add test for merger
- Add test for parser
- Improve circular dependencies (CDs) algorithm, it should return all the CDs instead of just the first one
- Add definitions collition check before merging
- Add test coverage
