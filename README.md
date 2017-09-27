<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  epfl-ldap
</h1>

<h4 align="center">
  Python toolkit for EPFL
</h4>

<p align="center">
  <a href="https://travis-ci.org/epfl-idevelop/epfl-ldap">
    <img src="https://travis-ci.org/epfl-idevelop/epfl-ldap.svg?branch=master"
         alt="Travis">
  </a>
</p>
<br>

## Overview

epfl-ldap is an amazing toolkit that provides basics functionalities to EPFL

* LDAP search
* LDAP authenticate
* etc

## License

[MIT license - Copyright (c) EPFL](./LICENSE)

## Requirements

Python (2.7, 3.5)

## Installation

```
pip install epfl-ldap
```

## How test

To run tests locally :
```
pytest
```
> You must create enviroment variables for authenticate 
``` 
export EPFL_LDAP_TEST_CORRECT_USERNAME=kermit
export EPFL_LDAP_TEST_CORRECT_PWD=xxxxxx
```

To run tests with coverage in your current python version :
```
pytest --cov=epflldap
```

To run mock tests in all python version : 
```
tox
```

## How check PEP8

To check if the python code is PEP8 compliant :
```
flake8 --max-line-length=120
```

## How to publish a new version

* Update the CHANGELOG.md file
* Update the version of this package. See __init__.py file
* Generate a new distribution
```
python setup.py sdist
```
a new *.tar.gz file is created in dist/
* Test this new version
* Push all changes on github (with tests, docs, etc)
* Publish this new version on pypi
```
twine upload dist/*
```


## TODO 

- [x] Config flake8 to check PEP8
- [x] Config pytest 
- [x] Config pytest with coverage
- [x] Config tox to support many python versions
- [x] Config mock tests
- [x] Config travis CI
- [ ] Write doc and publish it on http://docs.readthedocs.io
- [x] LDAP search
    - [x] Define CONSTANTS
        - [x] ldap_server = 'ldap.epfl.ch'
        - [x] ldap_base = "o=epfl,c=ch"
    - [x] User can define environment variable to override constants
- [x] LDAP authenticate
