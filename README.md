[![build status](https://travis-ci.com/PierreGuilmin/pycalculator_test.svg?branch=master)](https://travis-ci.com/PierreGuilmin/pycalculator_test)
[![documentation status](https://readthedocs.org/projects/pycalculator-test/badge/?version=latest)](https://pycalculator-test.readthedocs.io/en/latest/?badge=latest)

:construction: work in progress... :construction:

# pycalculator_test

This project is:
- a module and set of classes to check the syntax of an unparenthesized infix expression and convert it to an expression tree in order to evaluate it  
![basic infix to tree conversion](images/basic_infix_to_tree_conversion.svg)

- a powerful inline terminal calculator  
![terminal calculator](images/terminal_calculator.svg)

- a toy project for me gathering continous integration (Travis CI), automatic documentation (Sphinx) and Python module
packaging (PyPI, conda)  
![ci sphinx packaging](images/ci_sphinx_packaging.svg)

***

## Work with this repository

### Clone the repository

[![build status](https://travis-ci.com/PierreGuilmin/pycalculator.svg?branch=master)](https://travis-ci.com/PierreGuilmin/pycalculator)

To clone this repository on your local computer please run:
```bash
$ git clone https://github.com/PierreGuilmin/pycalculator.git
```

:warning: This project is still under development and not stable yet.

### Setup a Python conda environment on your local computer

> :point_up: We assume you have `conda` installed on your computer, otherwise please see [conda documentation](https://conda.io/docs/index.html) and [conda cheat sheet](https://conda.io/docs/_downloads/conda-cheatsheet.pdf).

The repository was written and tested under `Python 3.6`. You can see the requirements under [`environment.yml`](environment.yml). To create the conda environment named `pycalculator_env` and used by the project, please run the following command:
```bash
# create the conda environment
$ conda env create --file environment.yml
```

Some useful command lines to work with this conda environment:
```bash
# activate the conda environment
$ source activate pycalculator_env

# deactivate the conda environment
$ source deactivate

# remove the conda environment
$ conda env remove --name pycalculator_env
```

### Documentation

[![documentation status](https://readthedocs.org/projects/pycalculator-test/badge/?version=latest)](https://pycalculator-test.readthedocs.io/en/latest/?badge=latest)

The documentation of the module is available online at https://pycalculator-test.readthedocs.io/en/latest/.

It is created with Sphinx and updated from the master branch of the repository every 15 minutes.

### Repository structure
- **`doc/`**: directory holding the Sphinx configuration and documentation website structure.

- **`pycalculator/`**: the main Python module.

- **`temp/`**: drafts, temporary files and old scripts.
  > :warning: This directory should not be versionned.

- **`test/`**: Python `unittest` directory for the `pycalculator` module.

- **`travis/`**: Travis CI related directory.

### Emoji commit code table

Please use the following table to commit code:

| emoji        | meaning                      | code           |
| :----------: | :--------------------------- | :------------- |
| :sos:        | critical bug                 | `:sos:`        |
| :warning:    | bug                          | `:warning:`    |
| :flashlight: | simplification/clarification | `:flashlight:` |
| :clipboard:  | comment                      | `:clipboard:`  |
| :sparkles:   | typos & style                | `:sparkles:`   |
| :tada:       | new feature                  | `:tada:`       |
| :cloud:      | minor modification           | `:cloud:`      |

For example if you want to commit a new rocket feature — `🎉 new feature, flying rocket!` — please do:
```diff
# bad syntax
- $ git commit -m 'new feature, flying rocket!'

# good syntax
+ $ git commit -m ':tada: new feature, flying rocket!'
```

### Notes
The conda environment was created with the following command
```bash
# crate the conda environment
$ conda create --name pycalculator_env python=3.6 sphinx sphinx_rtd_theme
$ pip install sphinxcontrib-napoleon
```

And the requirements were exported with the folowing command:
```bash
# export the current conda environment requirements as .yml, we remove
#   - the final "prefix: ..." line
#   - some MacOS specific modules not available on Linux (libcxx and libcxxabi)
$ conda env export --no-builds --name pycalculator_env | grep -E -v "^prefix|libcxx|libcxxabi" > environment.yml
```
