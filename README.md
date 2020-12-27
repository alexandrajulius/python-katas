# Python Katas
This repository provides some simple code katas in Python and an instruction on how to set up a python project with a testing environment on your local (mac).

# Usage

## Install python
Go to any directory and type
```
$ brew install python3
```
Use python in the command line
```
$ python3 
quit()
```
Or play with it on [Jupyter Notebook](https://jupyter.org/install) preferably on your local
```
$ pip install notebook
$ jupyter notebook
```
Then in your browser on [http://localhost:8888/](http://localhost:8888/) go to **New** -> **Python3** and start coding without tests :)

## Install a virtual env
```
$ pip3 install virtualenv
```
Create your project directory
```
$ mkdir projectname
$ cd projectname
```
Create a directory that holds all libraries of the project, call it venv
```
$ virtualenv -p python3 venv
```
Activate the virtual env
```
$ . venv/bin/activate
```

## Install packages on your project
Create a file [requirements.txt](https://github.com/alexandrajulius/pythonKatas/blob/master/requirements.txt) and add your favourite packages to it. For now those will be:
* **pytest**: unit tests
* **pyhamcrest**: matcher objects in assert statements
* **flake8**, **mypy**: linters / static analysis / type annotation checks

Install the packages with
```
$ pip install -r requirements.txt
```
By running the this command the above packages will be installed only on your project. In this way you can provide different versions per project.

Add the created `venv` directory to your `.gitignore`. Developers who will work on your project will pull the `requirements.txt` from your repository and install all required packages with the above command.

## How to test
Run the test suites in your root directory
```
$ venv/bin/pytest -vvv
$ venv/bin/pytest binary_search/test_binary_search.py -vvv
```

## Author Contact
[alexandra.julius@gmail.com](mailto:alexandra.julius@gmail.com)
