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

Then install the project locally run this:

`pip install -e .`

If you don't install locally then the tests won't run
because the package will not be installed.

## What is pyproject.toml?

The [pyproject.toml](pyproject.toml) file be used for wider project configuration
and a setup.py file is no longer needed for editable installation using pip.

TOML stands for Tom's Obvious, Minimal Language.

## Pre-Commit hooks

Install dev packages `pip install -e . [dev]`

Use pre-commit hooks, once it's installed from the 
[pre-commit-config.yaml](.pre-commit-config.yaml) in the repository:

Then run `pre-commit install`

Avoid using args in the hook in [pre-commit-config.yaml]. Instead, store
necessary configuration in [pyproject.toml](pyproject.toml) for consistently
for your project. 
