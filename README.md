# Python Katas
This repository provides some simple code katas in Python and an instruction on how to set up a Python project with a testing environment on your local (mac).

# Usage

## Install Python
Location agnostic type
```
$ brew install python3
```
Use Python in the command line 
```
$ python3 
>>> import this
(find joy in reading the Zen of Python)
>>> quit()
```
Or play with Python on [Jupyter Notebook](https://jupyter.org/install) preferably on your local
```
$ pip3 install notebook
$ jupyter notebook
```
Then in your browser on [http://localhost:8888/](http://localhost:8888/) go to **New** -> **Python3** and start coding without tests :)

## Install a virtual environment
Install the virtualenv
```
$ pip3 install virtualenv
```
In your project directory, create the virtual environment (that is a directory `venv` where all libraries of your project live)
```
$ virtualenv -p python3 venv
```
Activate the virtual env
```
$ . venv/bin/activate
```

## Install packages on your project
In your root directory, create a file [requirements.txt](https://github.com/alexandrajulius/pythonKatas/blob/master/requirements.txt) and add your favourite packages to it. For now those will be:
* **pytest**: unit test framework
* **pyhamcrest**: matcher objects in assert statements
* **flake8**: syntax checks / linter
* **mypy**: type annotation checks 

Install the packages with
```
$ pip install -r requirements.txt
```
By running this command the above packages will be installed only on your project. In this way you can provide different versions per project.

Add the created `venv` directory to your `.gitignore`. Developers who will work on your project will pull the `requirements.txt` from your repository and install all required packages with the above command.

### Notes on usage
#### Flake8
When opening your project in VSCode for the first time, your IDE will ask you to install a linter. Click `Select Linter` and chose `Flake8`.

#### Mypy
`mypy` validates types and can be pretty annoying sometimes. You can disable it with `# type: ignore` where ever needed (see [example](https://github.com/alexandrajulius/python-katas/blob/master/dijkstra_shortest_path/dijkstra.py#L27)). But in general, type checks make sense of course. Out of the box, `mypy` validates simple types such as `int`, `str`, `float`, `bool`. To validate more complex types (`list`, `tuple`, `dict`, ..) we have to import the types from the built-in library in the code, e.g. `from typing import Tuple`.

## How to test
Run the test suites in your root directory
```
$ venv/bin/pytest -vvv
$ venv/bin/pytest binary_search/test_binary_search.py -vvv
```
Pytest will show print output from your code in the command line only on test failure. 
You can disable per-test capturing with `-s`
```
$ venv/bin/pytest -s
```

### Fixtures
Store your fixture file as [/tests/fixtures/fixture.txt](https://github.com/alexandrajulius/python-katas/blob/master/advent_of_code/2019/tests/fixtures/day_02.txt). 
In your [test_example.py](https://github.com/alexandrajulius/python-katas/blob/master/advent_of_code/2019/tests/unit/test_day_02.py) use Pytest's `fixture` decorator to create a method that reads the file and returns its content. Pass this method as an
argument into your test method.

Use the following code to provide fixtures in your test:
```
import pytest

@pytest.fixture
def fixture_content():
    with open("tests/fixtures/fixture.txt") as f:
        return f.read()
        
def test_runs_example(fixture_content):
    expected = "expected output"
    actual = run(fixture_content)
    assert_that(actual, equal_to(expected))
```

Using Python's Content Manager (`with` statement) will open the fixture file, read from it and then close it. 

## Author Contact
[alexandra.julius@gmail.com](mailto:alexandra.julius@gmail.com)
