#epfl-utils

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
