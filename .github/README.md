[![tests](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/reports/tests-badge.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/reports/junit/report.html)
[![coverage](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/reports/coverage-badge.svg)](https://htmlpreview.github.io/?https://github.com/yamenk-gribaudo/python_files_merger/blob/master/htmlcov/index.html)

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

Check [https://github.com/yamenk-gribaudo/python_files_merger](https://github.com/yamenk-gribaudo/python_files_merger)