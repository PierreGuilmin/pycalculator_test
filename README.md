[![build status](https://travis-ci.com/PierreGuilmin/pycalculator_test.svg?branch=master)](https://travis-ci.com/PierreGuilmin/pycalculator_test)
[![documentation status](https://readthedocs.org/projects/pycalculator-test/badge/?version=latest)](https://pycalculator-test.readthedocs.io/en/latest/?badge=latest)

:construction: Work in progress... :construction:

See documentation at: https://pycalculator-test.readthedocs.io/en/latest/

# pycalculator_test

This project is a Python inline terminal `pycalculator`.

***

## Work with this repository

### Clone the repository

To clone this repository on your local computer please run:
```bash
$ git clone https://github.com/PierreGuilmin/pycalculator.git
```

https://github.com/StevenBlack/hosts/blob/master/ci/install_conda.sh
https://github.com/StevenBlack/hosts/blob/master/ci/setup_conda_env.sh
https://gist.github.com/dan-blanchard/7045057
https://choosealicense.com/

### Setup a Python conda-environment on your local computer

> :warning: We assume you have `conda` installed on your computer, otherwise please see https://conda.io/docs/index.html (conda documentation) and https://conda.io/docs/_downloads/conda-cheatsheet.pdf (conda cheat sheet).

The repository was written and tested under `Python 3.6`. You can see the requirements under [`environment.yaml`](environment.yaml). To create the conda-env, please run the following command:
```bash
# create the conda-env
$ conda env create --file environment.yaml
```

Some useful command lines to work with this conda-env:
```bash
# activate the conda-env
$ source activate pycalculator_env

# deactivate the conda-env
$ source deactivate

# remove the conda-env
$ conda env remove --name pycalculator_env
```

### Notes
The environment was created with the following command
```bash
# crate the conda-env
conda create --name pycalculator_env python=3.6 sphinx sphinx_rtd_theme
pip install sphinxcontrib-napoleon
```

And the requirements were exported with the folowing command:
```bash
# export the current conda-env requirements as .yaml (without the final "prefix: ..." line and some useless not available on Linux MacOS specific libraries)
conda env export --no-builds --name pycalculator_env | grep -E -v "^prefix|libcxx|libcxxabi" > environment.yaml
```

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
