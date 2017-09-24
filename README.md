<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  epfl-utils
</h1>

<h4 align="center">
  Python toolkit for EPFL
</h4>

<p align="center">
  <a href="https://travis-ci.org/epfl-idevelop/epfl-utils">
    <img src="https://travis-ci.org/epfl-idevelop/epfl-utils.svg?branch=master"
         alt="Travis">
  </a>
</p>
<br>

## Overview

epfl-utils is an amazing toolkit that provides basics functionalities to EPFL

* LDAP search
* etc

## License

[MIT license - Copyright (c) EPFL](./LICENSE)

## Requirements

Python (2.7, 3.5)

## Installation

First create a virtualenv wrapper : 
```
mkvirtualenv epfl-utils-python27
```

Install requirements : 
```
pip install -r requirements/py2.txt
```

## How test

To run tests in your current python version :
```
pytest
```

To run tests with coverage in your current python version :
```
pytest --cov=epflutils
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

## TODO 

- [x] Config flake8 to check PEP8
- [x] Config pytest 
- [x] Config pytest with coverage
- [x] Config tox to support many python versions
- [x] Config mock tests
- [x] Config travis CI
- [x] LDAP search
    - [x] Define CONSTANTS
        - [x] ldap_server = 'ldap.epfl.ch'
        - [x] ldap_base = "o=epfl,c=ch"
    - [x] User can define environment variable to override constants
    - [x] Test ldap and scoldap  
- [ ] LDAP authenticate
