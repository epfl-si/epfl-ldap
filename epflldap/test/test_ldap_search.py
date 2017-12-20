"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""
import pytest

from epflldap.ldap_search import get_username, get_sciper, get_units, is_unit_exist, get_unit_name, get_email, \
    get_unit_id
from epflldap.utils import EpflLdapException


def test_get_sciper():
    # Success
    assert get_sciper(username="charmier") == "188475"
    assert get_sciper(username='kermit') == "133134"

    # Fail
    with pytest.raises(
            EpflLdapException,
            match=r"No sciper corresponds to username GuidovanRossum"):
        get_sciper(username="GuidovanRossum")


def test_get_username():
    # Success
    assert get_username(sciper="188475") == "charmier"
    assert get_username(sciper="133134") == "kermit"

    # Fail
    with pytest.raises(
            EpflLdapException,
            match=r"No username corresponds to sciper 42"):
        get_username(sciper="42")


def test_get_email():
    # Success
    assert get_email(sciper="133134") == "kermit.lagrenouille@epfl.ch"
    assert get_email(sciper="188475") == "gregory.charmier@epfl.ch"

    # Fail
    with pytest.raises(
            EpflLdapException,
            match=r"No email address corresponds to sciper 42"):
        get_email(sciper="42")


def test_get_units():
    # Success
    units = get_units(username="charmier")
    assert len(units) == 1
    assert '13030' == units[0]

    units = get_units(username="ebreton")
    assert len(units) == 3
    assert '13029' == units[0]
    assert '13030' == units[1]
    assert '13051' == units[2]

    # Fail
    units = get_units(username="GuidovanRossum")
    assert len(units) == 0


def test_is_unit_exist():
    # Success
    assert is_unit_exist(unit_id="13030")
    assert is_unit_exist(unit_id="13548")
    assert is_unit_exist(unit_id="12493")
    assert is_unit_exist(unit_id="13031")
    assert is_unit_exist(unit_id="13029")
    assert is_unit_exist(unit_id="12634")
    assert is_unit_exist(unit_id="12922")
    assert is_unit_exist(unit_id="10426")
    assert is_unit_exist(unit_id="13471")
    assert is_unit_exist(unit_id="13548")
    assert is_unit_exist(unit_id="13565")
    assert is_unit_exist(unit_id="12922")
    assert is_unit_exist(unit_id="12634")

    # Fail
    assert not is_unit_exist(unit_id="88")


def test_get_unit_name():
    # Success
    unit = get_unit_name(unit_id="13030")
    assert unit.lower() == "idevelop"

    unit = get_unit_name(unit_id="13548")
    assert unit.lower() == "spring"

    unit = get_unit_name(unit_id="12493")
    assert unit == "tunes"

    unit = get_unit_name("13031")
    assert unit == "ideving"

    unit_name = get_unit_name("13029")
    assert unit_name == "idevam"

    unit_name = get_unit_name("12634")
    assert unit_name == "dcsl"

    unit_name = get_unit_name("12922")
    assert unit_name == "scitas"

    unit_name = get_unit_name("13565")
    assert unit_name == "lpbs"

    unit_name = get_unit_name("13471")
    assert unit_name == "flexlab"

    unit_name = get_unit_name("10426")
    assert unit_name == "lca1"

    unit_name = get_unit_name("12637")
    assert unit_name == "vpsi"

    # Fail
    with pytest.raises(
            EpflLdapException,
            match=r"The unit with id '42' was not found"):
        get_unit_name(unit_id="42")


def test_get_unit_id():
    # Success
    unit_id = get_unit_id("IDEVELOP")
    assert unit_id == "13030"

    unit_id = get_unit_id("idevelop")
    assert unit_id == "13030"

    unit_id = get_unit_id("IDEVING")
    assert unit_id == "13031"

    unit_id = get_unit_id("IDEVAM")
    assert unit_id == "13029"

    unit_id = get_unit_id("DCSL")
    assert unit_id == "12634"

    unit_id = get_unit_id("SCITAS")
    assert unit_id == "12922"

    unit_id = get_unit_id("LPBS")
    assert unit_id == "13565"

    unit_id = get_unit_id("SPRING")
    assert unit_id == "13548"

    unit_id = get_unit_id("TUNES")
    assert unit_id == "12493"

    unit_id = get_unit_id("FLEXLAB")
    assert unit_id == "13471"

    unit_id = get_unit_id("LCA1")
    assert unit_id == "10426"

    unit_id = get_unit_id("VPSI")
    assert unit_id == "12637"

    # Fail
    with pytest.raises(
            EpflLdapException,
            match=r"The unit named 'idevelop_pas_souvent' was not found"):
        get_unit_id(unit_name="idevelop_pas_souvent")
