# production_ml
Machine learning models and methods to a production standard 

The source files are in the src directory

*module* – a module is a file containing Python functions.

*package* – a package is a collection of modules intended to be installed and
 used together.

Why put your package code in a src subdirectory?

Using a src/ directory ensures that you must install a package to test it, 
so as your users would do. Also it prevents tools like pytest incidently 
importing it.

## virtual environment

The virtual environment for this repo was created using [pyproject.toml](pyproject.toml)

Then install the project locally, making the “live” version available to use it locally run this:

`pip install -e .`

If you don’t do this “editable installation” then your tests won’t run
because the package will not be installed.

## What is pyproject.toml?

TOML - Tom's Obvious, Minimal Language.

The pyproject.toml file was introduced in PEP-518 (2016) as a way of separating
configuration of the build system from a specific, optional library 
(setuptools) and also enabling setuptools to install  itself without already 
being installed. Subsequently PEP-621 (2020) introduces the idea that the
[pyproject.toml](pyproject.toml) file be used for wider project configuration
and PEP-660 (2021) proposes finally doing away with the need for setup.py for 
editable installation using pip.

## pre-commit hooks 

Install dev packeages `pip install -e . [dev]`

Use pre-commit hooks, once it's installed from [pyproject.toml](pyproject.toml) the 
[pre-commit-config.yaml](.pre-commit-config.yaml) in the repository:

Then run `pre-commit install`.

Avoid using args in the hook in [pre-commit-config.yaml]. Instead, store
necessary configuration in [pyproject.toml](pyproject.toml) for consistently
for your project. 
