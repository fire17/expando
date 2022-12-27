# expando
Dynamic Dictionary Object Wrapper

<!-- [![Build Status](https://travis-ci.org/robertzk/expando.svg?branch=master)](https://travis-ci.org/robertzk/expando)
[![Coverage Status](https://coveralls.io/repos/robertzk/expando/badge.svg?branch=master&service=github)](https://coveralls.io/github/robertzk/expando?branch=master)
[![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/expando)](http://cran.r-project.org/package=expando)
[![Downloads](http://cranlogs.r-pkg.org/badges/expando)](http://cran.rstudio.com/package=expando) -->

## Installation

```python
pip install expando
```

## to reupload to pip after edits (internal use only)
```
# Copy/edit setup.py
# install twine
python3 -m pip install twine

# update setup.py version
python setup.py sdist bdist_wheel
twine upload dist/*
export VERSION=0.5.1
git tag -a 0.5.1 -m "Release $VERSION"
git add .
git commit -m "Release $VERSION"
git push origin --tags
git push
```