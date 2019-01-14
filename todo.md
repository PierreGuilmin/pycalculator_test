# todo

| emoji        | meaning                      | code           |
| :----------: | :--------------------------- | :------------- |
| :sos:        | critical bug                 | `:sos:`        |
| :warning:    | bug                          | `:warning:`    |
| :flashlight: | simplification/clarification | `:flashlight:` |
| :clipboard:  | comment                      | `:clipboard:`  |
| :sparkles:   | typos & style                | `:sparkles:`   |
| :tada:       | new feature                  | `:tada:`       |
| :cloud:      | minor modification           | `:cloud:`      |

Before publishing:
- change pycalculator_test for pycalculator in `README.md`
- reread `README.md`
- > Blabla
- add pip installation
- https://pypi.org/project/binarytree/
- doc, test, pycalculator
- reinstall Sphinx and conda env
- https://www.python.org/dev/peps/pep-0008/#maximum-line-length

## General
- [ ] :tada: package code and upload it to PyPI and conda
- [ ] :tada: GUI (in JS?)
    - [ ] :tada: live suggestion while typing
    - [ ] :tada: live parenthesis and operator coloring
- [ ] :tada: propose automatic corrections
- [ ] :tada: find a license (https://choosealicense.com/)
- [ ] :tada: add codacy/codecoverage GitHub marketplace extensions

### Travis CI
- [ ] :tada: add Windows support (update `travis/install_conda.sh` and `.travis.yml`)

### Sphinx
- [ ] :flashlight: necessary to add `.. testsetup::` at the beginning of every module for the doctest to work

## `expression_tree.py`

### `ExpressionTreeNode`:
    - [ ] :tada: new tree representation
    - [ ] :tada: handle division by 0 and other wrong operations

### `ExpressionTreeBuilder`
    - [ ] :tada: integrate functions and unary operators support


## `infix_expression.py`
- [ ] check if not empty
- [ ] enable multi-parenthesing with [] and {}


## `tools.py`
- [ ] :warning: make `color()` cross-platform, issue on Windows with ANSI escape code (use package `colarama`?)
