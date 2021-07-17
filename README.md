# string-find
String Find

Note:
* Currently find is case-insensitive. Everything will be compared with lowercase.
* Added Github Action and Pre-commit for Pylint Check (Using Black - https://black.readthedocs.io/en/stable/).
* Pytest for testing.

Todo:
* Improvements needed for error handling, eg:- If integer passed instead of string, it will give error.
* Optimization might be needed for large datasets.

## Environment and Package Management
Install Poetry

    $ pip install poetry
    or
    $ pip3 install poetry

Activate or Create Env

    $ poetry shell

Install Packages from Poetry

    $ poetry install

## Usage

    from string_find import find
    from string_find_cls import Find

    data = ["helloworld", "foo", "bar", "stylight_team", "seo"]
    query = "eos"

    # Function Usage
    result = find(data, query)
    print(result)  # ["seo"]

    # Class Usage
    result = Find(data, query)
    print(result)  # ["seo"]

## Test

    $ pytest

## Version
* Python: 3.8+
