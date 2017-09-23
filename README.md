<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  epfl-utils
</h1>

<h4 align="center">
  Common tools for EPFL python dev
</h4>

<p align="center">
  <a href="https://travis-ci.org/epfl-idevelop/epfl-utils">
    <img src="https://travis-ci.org/epfl-idevelop/epfl-utils.svg?branch=master"
         alt="Travis">
  </a>
</p>
<br>

## How install

First create a virtualenv wrapper : 
```
mkvirtualenv epfl-utils-python27
```

Install requirements : 
```
pip install -r requirements/py2.txt
```

## How test

To run test in your current python version :
```
pytest
```

To run test with coverage in your current python version :
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

Define CONST 
- ldap_server = 'ldap.epfl.ch'
- ldap_base = "o=epfl,c=ch"

and test :
- ldap.epfl 
- scoldap
