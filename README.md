# expando
Dynamic Dictionary Object Wrapper

<!-- [![Build Status](https://travis-ci.org/robertzk/expando.svg?branch=master)](https://travis-ci.org/robertzk/expando)
[![Coverage Status](https://coveralls.io/repos/robertzk/expando/badge.svg?branch=master&service=github)](https://coveralls.io/github/robertzk/expando?branch=master)
[![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/expando)](http://cran.r-project.org/package=expando)
[![Downloads](http://cranlogs.r-pkg.org/badges/expando)](http://cran.rstudio.com/package=expando) -->

## Installation/Update

```python
python3 -m pip install --upgrade expando
```

## import

```python
from xo import xo, Expando
# or
from xo import *
```

## Usage
```python

# Use xo as your root object
xo.foo.bar(17).baz.plus.something = lambda *a, **kv : (f"Hello Expando! {xo.foo.bar.value}" , a, kv)
print(xo.foo.bar.baz.plus.something())

# Create a new Expando object
myStore = Expando()
```

## to reupload to pip after edits (internal use only)
```
# install twine
python3 -m pip install twine 
# Skip if you have it already

export VERSION=0.5.5
# Copy/edit setup.py
# update setup.py version
python3 setup.py sdist bdist_wheel
twine upload dist/*

# to install locally (before twine upload)
python3 -m pip install --force-reinstall --no-deps . 
```

```
```
# make sure you'd like to commit all changes
git add . 
git tag -a $VERSION -m "Release $VERSION"
git commit -m "Release $VERSION"
git push origin --tags
git push
```