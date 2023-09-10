![Python](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/python.svg)
![Version](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/version.svg)
![License](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/license.svg)
![Workflow](https://github.com/yamenk-gribaudo/python_files_merger/actions/workflows/test.yml/badge.svg)
[![Tests](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/tests.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/reports/junit/report.html)
[![Coverage](https://raw.githubusercontent.com/yamenk-gribaudo/python_files_merger/master/badges/coverage.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/htmlcov/index.html)


The Python Files Merger is a tool that seamlessly combines multiple Python files into a single, well-organized unit while automatically handling imports, checking definition collisions, and resolving dependencies. It can be used to merge standard Python files but works especially well hadnling files designed for microcontrollers. The package supports Python, MicroPython, and CircuitPython files.

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

## Tests 

You can click on the tests badge to check the tests status

    pytest 
    
## Coverage

You can clickon the coverage badge to check the code coverage

    coverage run --source=python_files_merger -m unittest discover && coverage report
## Reports and badges

Right now, badges are generated locally and uploaded to github, we should really do this in github workflows. 

To generate reports and badges:

    python genbadges.py

## Upload to pip

1. Update python_files_merger version in `python_files_merger/__init__.py`.
1. Run `python setup.py sdist` to create the dist tar which will be uploadad to pip.
1. Run `python -m twine upload dist/$(ls dist | tail -n 1)` to upload the most up to date tar folder in the sir directory.
