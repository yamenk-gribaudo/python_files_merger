[![tests](./reports/tests-badge.svg)](./reports/tests-badge.svg)
[![coverage](./reports/coverage-badge.svg)](./reports/junit/report.html)

# Merge files
    python python_files_merger src/*

or

    python python_files_merger src/lorem.py src/ipsum.py

# Contributing 

## Lint

    pylint python_files_merger

## Tests

    pytest --junitxml=reports/junit/junit.xml --html=reports/junit/report.html && genbadge tests -o reports/tests-badge.svg

## Coverage

    coverage run --source=python_files_merger -m unittest discover && coverage report && coverage xml -o reports/coverage/coverage.xml && genbadge coverage -o reports/coverage-badge.svg

## TODOs:
- Add test for remove_comments
- Add test for merger
- Add test for parser
- Improve circular dependencies (CDs) algorithm, it should return all the CDs instead of just the first one
- Add definitions collition check before merging
- Add test coverage
