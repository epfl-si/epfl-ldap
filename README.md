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

##How install

create a virtualenv 

mkvirtualenv epfl-utils-python27

###Define environment variables

export LDAP_SERVER_FOR_SEARCH='ldap.epfl.ch'
export LDAP_BASE_DN="o=epfl,c=ch"

##How test
pytest

pytest --cov=epflutils

tox

## PEP8
flake8 --max-line-length=120
