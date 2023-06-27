[![Build Status](https://secure.travis-ci.org/yamenk-gribaudo/python_files_merger.svg?branch=main)](http://travis-ci.org/christophevg/python_files_merger)
[![Tests Status](./reports/tests-badge.svg)](./reports/tests-badge.svg)
[![Coverage Status](./reports/coverage-badge.svg)](./reports/coverage-badge.svg)

# Merge files
    python python_files_merger src/*

or

    python python_files_merger src/lorem.py src/ipsum.py

# Lint

    pylint python_files_merger

# Test with coverage

    pytest --junitxml=unittests.xml

# TODOs:
- Add test for remove_comments
- Add test for merger
- Add test for parser
- Improve circular dependencies (CDs) algorithm, it should return all the CDs instead of just the first one
- Add definitions collition check before merging
- Add test coverage
