# production_ml
Machine learning models and methods to a production standard. 

The source files are in the src directory, that must be installed as a 
package before tests can run. This is to prevent tools like pytest incidentally 
importing it.

*module* a module is a file containing Python functions.

*package* a package is a collection of modules intended to be installed and
 used together.

## Virtual Environment

The virtual environment for this repo was created using a 
[pyproject.toml](pyproject.toml)  file

`poerty install`

`poerty build`

Then install the project locally run this:

`pip install -e .`

If you don't install locally then the tests won't run
because the package will not be installed.

## What is pyproject.toml?

The [pyproject.toml](pyproject.toml) file be used for wider project configuration
and a setup.py file is no longer needed for editable installation using pip.

TOML stands for Tom's Obvious, Minimal Language.

When a toml script is added or updated, run `poetry install` to make them 
available in virtual env.

## Pre-Commit hooks

Install dev packages `poetry install --with dev`

hen a script is added or updated, run poetry install to make them available
in the project’s virtualenv.

Use pre-commit hooks, once it's installed from the 
[pre-commit-config.yaml](.pre-commit-config.yaml) in the repository:

To set up the git hook run `pre-commit install`

Avoid using args in the hook in [pre-commit-config.yaml]. Instead, store
necessary configuration in [pyproject.toml](pyproject.toml) for consistently
for your project. 

Can build project using `pip -m build . --wheel`or  with editable 
`install with pip install -e .`

## Data

The data was obtained from the 
[Kaggle API](https://github.com/Kaggle/kaggle-api#api-credentials)
 by installing kaggle python package (included in toml file) using the command
  line: 

`pip install kaggle`

The coffee kaggle dataset was download via Kaggle API using:

`kaggle datasets download -d michals22/coffee-dataset`

## MkDocs

Create and manage project pages documentation in ![mkdocs.yaml](mkdocs.yml)

Set up for the repo using https://www.mkdocs.org/getting-started/#creating-a-new-project

### serve docs locally

Activate virtual environment, run the `mkdocs serve` command to locally run:

Open up http://127.0.0.1:8000/ in browser

### serve docs remotely 

Deploy Mk documentation by creating a documentation site that only uses static
files to host. Simply upload the contents of the entire site directory.

Step 1) `mkdocs build`

To deploy projects pages sites to a branch within GHE project repo (gh-pages)

Step 2) `mkdocs gh-deploy`

## JupyterLab Notebooks

Create a kernel for notebook, by `pip install ipykernel` on virtual 
environment and active environment

`source prod_ml\scripts\activate`

`python -m ipykernel install --name prod_ml`

https://nbviewer.org/