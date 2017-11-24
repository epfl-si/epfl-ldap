"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""
from epflldap.ldap_search import get_username, get_sciper, get_units, is_unit_exist, get_unit_name, get_email, \
    get_unit_id


def test_get_sciper():
    assert get_sciper(username="charmier") == "188475"
    assert get_sciper(username='kermit') == "133134"


def test_get_username():
    assert get_username(sciper="188475") == "charmier"
    assert get_username(sciper="133134") == "kermit"


def test_get_email():
    assert get_email(sciper="133134") == "kermit.lagrenouille@epfl.ch"
    assert get_email(sciper="188475") == "gregory.charmier@epfl.ch"


def test_get_units():
    units = get_units(username="charmier")
    assert len(units) == 1
    assert '13030' == units[0]

    units = get_units(username="ebreton")
    assert len(units) == 3
    assert '13029' == units[0]
    assert '13030' == units[1]
    assert '13051' == units[2]


def test_is_unit_exist():
    # Success
    assert is_unit_exist(unit_id="13030")
    # Fail
    assert not is_unit_exist(unit_id="88")


def test_get_unit_name():
    unit = get_unit_name(unit_id="13030")
    assert unit.lower() == "idevelop"


def test_get_unit_id():
    unit_id = get_unit_id("idevelop")
    assert unit_id == "13030"
