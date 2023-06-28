![version](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/version.svg)
![license](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/license.svg)
![workflow](https://github.com/yamenk-gribaudo/python_files_merger/actions/workflows/test.yml/badge.svg)
[![tests](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/tests.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/reports/junit/report.html)
[![coverage](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/coverage.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/htmlcov/index.html)

# Usage

## Shell example

    python -m python_files_merger src/*

or

    python -m python_files_merger src/lorem.py src/ipsum.py

You can see shell option with `python -m python_files_merger -h`

## File example

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

## Tests with coverage

You can click on the tests or coverage badges to check the code coverage and tests coverage

    coverage run --source=python_files_merger -m unittest discover && coverage report
## Reports and badges

Right now, badges are generated locally and uploaded to github. We should really do this in github workflows. 

To generate reports and badges:

    python genbadges.py

## TODOs:

- Add test for merger
- Improve circular dependencies (CDs) algorithm, it should return all the CDs instead of just the first one
- Add badges generation in github workflow
