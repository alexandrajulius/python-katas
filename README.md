# Python Katas
This repository provides some simple code katas in Python and an instruction on how to set up a python project with a testing environment on your local (mac).

## Usage

# install python
Go to any directory and type
```
brew install python3
```
Use python in the command line
```
python3 
```
Exit with
```
quit()
```
# install virtual env
```
pip3 install virtualenv
```
Create your project directory
```
mkdir projectname
cd projectname
```
Create directory that holds all libraries of the project, call it venv
```
virtualenv -p python3 venv
```
Activate the virtualenv
```
. venv/bin/activate
```
Create a file requirements.txt 
```
touch requirements.txt
```
and add the favoured packages to it. For now those will be:
```
pytest
pyhamcrest
flake8
mypy
```
with
pytest: unit tests
pyhamcrest: matcher objects
flake8, mypy: linters / statical analysis / type annotation checks

# install the required packages on your project
```
pip install -r requirements.txt
```
By running the above command you will install these packages only for your project. In this way you can provide different versions per project.

Add the `venv` directory to your `.gitignore`, instead users who will work on your project will pull `requirements.txt` from your repository and install all required libraries with the above command.

## How to test
Run the test suites in your root directory
```
venv/bin/pytest -vvv
```

## Author Contact
[alexandra.julius@gmail.com](mailto:alexandra.julius@gmail.com)
