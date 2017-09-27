"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""
from epflldap.ldap_authenticate import Authenticator
from epflldap.utils import get_optional_env


def test_get_user_dn():
    auth = Authenticator()
    user_dn = auth.get_user_dn(username='kermit')
    assert user_dn == "uid=kermit,ou=users,o=epfl,c=ch"


def test_authenticate():

    # Success test
    auth = Authenticator()
    username = get_optional_env('EPFL_LDAP_TEST_CORRECT_USERNAME')
    password = get_optional_env('EPFL_LDAP_TEST_CORRECT_PWD')
    assert auth.authenticate(username=username, password=password)

    # Failed test
    auth = Authenticator()
    username = 'kermit'
    password = 'badpassword'
    assert not auth.authenticate(username=username, password=password)
