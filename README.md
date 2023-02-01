# template_analytics

A tool to standardize and accelerate the set up of analytics projects.

## Environment Setup

This repository also uses `pipenv` for dependency management. Please follow these steps to get this set up:

1) Fristly install Pipenv: ``pip install --user pipenv``

2) To create/enter the virtual environment: ``pipenv shell``

3) To install the packages: ``pipenv install``

Please note that it may take a while for packages to be installed.

If you get an error that says pipenv is not found, run the above commands with `python -m` in front.

## Running the code

This tool uses Kedro, an open-source Python framework for creating reproducible, maintainable and modular data science code.

You can run your Kedro project with:

```
kedro run
```

To visualize the results please use the following command:

```
kedro viz
```

## Modifying the pipeline

The tool can be customized by providing changes in two yml files, ``parameters.yml`` and ``catalog.yml``.

``parameters.yml`` defines a set of ML and data parameters for the pipeline that stay constant.

``catalog.yml`` defines a set of input and output datasets that should be stored outside of Python memory. These can be modified based on individual needs.


## Testing the code

Testing uses the standard PyTest library, which can be run by using the following command:

```
pytest
```

The output also contains data on code coverage.
