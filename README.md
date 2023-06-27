[![tests](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/reports/tests-badge.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/reports/junit/report.html)
[![coverage](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/reports/coverage-badge.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/htmlcov/index.html)

# Merge files
    python -m python_files_merger src/*

or

    python -m python_files_merger src/lorem.py src/ipsum.py

# Contributing 

## Developing

You can download the repo and run the merger with `python -m python_files_merger <files_to_merge>`

## Lint

    pylint python_files_merger

## Tests, coverage and badges

You can click on the tests or coverage badges to check the code coverage and tests coverage. We should create the badges in github workflows. Also we should add workflow status to the badges

Tests and create tests badge:

    pytest --junitxml=reports/junit/junit.xml --html=reports/junit/report.html && genbadge tests -o reports/tests-badge.svg

Coverage and create coverage badge:

    coverage run --source=python_files_merger -m unittest discover && coverage report && coverage html && coverage xml -o reports/coverage/coverage.xml && genbadge coverage -o reports/coverage-badge.svg

## TODOs:

- Add test for remove_comments
- Add test for merger
- Add test for parser
- Improve circular dependencies (CDs) algorithm, it should return all the CDs instead of just the first one
- Add definitions collition check before merging
- Add badges generation in github workflow
