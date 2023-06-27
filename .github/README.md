[![tests](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/reports/tests-badge.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/reports/junit/report.html)
[![coverage](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/reports/coverage-badge.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/htmlcov/index.html)

# Usage

## Shell

    python -m python_files_merger src/*

or

    python -m python_files_merger src/lorem.py src/ipsum.py

You can see shell option with `python -m python_files_merger -h`

## In file

    import python_files_merger

    python_files_merger.merge(["src/**"], output="merged_files.py")

The function also returns the raw string, so you could do:

    import python_files_merger

    output_string = python_files_merger.merge(["src/**"])
    print(output_string)

Only optional parameter is "output", that lets you choose where the output should be saved. 

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

- Add test for merger
- Improve circular dependencies (CDs) algorithm, it should return all the CDs instead of just the first one
- Add badges generation in github workflow
