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

## General
- [ ] :tada: package code and upload it to PyPI

## `tools.py`
- [ ] :warning: make `color()` cross-platform, issue on Windows with ANSI escape code (use package `colarama`?)

## `expression_tree.py`
- [ ] :clipboard: comment all
- `ExpressionTree`:
    - [ ] :tada: new output
    - [ ] :sparkles: `_is_leaf()` rather than `is_leaf()`

## Sphinx
- [ ] :flashlight: necessary to add `.. testsetup::` at the beginning of every module for the doctest to work

## Vrac
https://python-docs.readthedocs.io/en/latest/writing/documentation.html
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/
http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html

```bash
conda install sphinx
#pip install sphinxcontrib-napoleon
mkdir docs
cd docs
sphinx-quickstart
sphinx-apidoc -o source/ ../pycalculator
pip install sphinx_rtd_theme
```

```python
# in conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../../pycalculator'))

# add to extensions
'sphinxcontrib.napoleon'

html_theme = 'sphinx_rtd_theme'
```


Tavis: run doctest python -m doctest -v tools.py and regular tests



```
$ python -m doctest -v pycalculator/*.py
$ python -m unittest -v tests/*.py
$ cd docs
$ make doctest
$ make html
```

