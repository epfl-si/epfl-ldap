"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""
import ldap3

from epflldap.utils import get_optional_env


def _get_LDAP_connection():
    """
    Return a LDAP connection
    """
    server = ldap3.Server('ldap://' + get_optional_env('EPFL_LDAP_SERVER_FOR_SEARCH'))
    connection = ldap3.Connection(server)
    connection.open()

    return connection, get_optional_env('EPFL_LDAP_BASE_DN')


def LDAP_search(pattern_search, attribute):
    """
    Do a LDAP search
    """
    connection, ldap_base = _get_LDAP_connection()

    connection.search(
        search_base=ldap_base,
        search_filter=pattern_search,
        attributes=[attribute]
    )
    return connection.response


def is_unit_exist(unit_id):
    """
    Return True if the unit 'unid_id' exists.
    Otherwise return False
    """
    attribute = 'objectClass'
    response = LDAP_search(
        pattern_search="(uniqueidentifier=" + unit_id + ")",
        attribute=attribute
    )

    try:
        return 'EPFLorganizationalUnit' in response[0]['attributes'][attribute]
    except Exception:
        return False


def get_unit_name(unit_id):
    """
    Return the unit name to the unit 'unit_id'
    """
    attribute = 'cn'
    response = LDAP_search(
        pattern_search='(uniqueIdentifier=' + unit_id + ')',
        attribute=attribute
    )
    return response[0]['attributes'][attribute][0]


def get_unit_id(unit_name):
    """
    Return the unit id to the unit 'unit_name'
    """
    attribute = 'uniqueIdentifier'
    response = LDAP_search(
        pattern_search='(cn=' + unit_name + ')',
        attribute=attribute
    )
    print(response)
    return response[0]['attributes'][attribute][0]


def get_units(username):
    """
    Return all units of user 'username'
    """
    connection, ldap_base = _get_LDAP_connection()

    # Search the user dn
    connection.search(
        search_base=ldap_base,
        search_filter='(uid=' + username + '@*)',
    )

    # For each user dn give me the unit
    dn_list = [connection.response[index]['dn'] for index in range(len(connection.response))]

    units = []
    # For each unit search unit information and give me the unit id
    for dn in dn_list:
        unit = dn.split(",ou=")[1]
        connection.search(search_base=ldap_base, search_filter='(ou=' + unit + ')', attributes=['uniqueidentifier'])
        units.append(connection.response[0]['attributes']['uniqueIdentifier'][0])

    return units


def get_sciper(username):
    """
    Return the sciper of user
    """
    attribute = 'uniqueIdentifier'
    response = LDAP_search(
        pattern_search='(uid=' + username + ')',
        attribute=attribute
    )
    return response[0]['attributes'][attribute][0]


def get_username(sciper):
    """
    Return username of user
    """
    attribute = 'uid'
    response = LDAP_search(
        pattern_search='(uniqueIdentifier=' + sciper + ')',
        attribute=attribute
    )
    return response[0]['attributes'][attribute][0]


def get_email(sciper):
    """
    Return email of user
    """
    attribute = 'mail'
    response = LDAP_search(
        pattern_search='(uniqueIdentifier=' + sciper + ')',
        attribute=attribute
    )
    return response[0]['attributes'][attribute][0]
