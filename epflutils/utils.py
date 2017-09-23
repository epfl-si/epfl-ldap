"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""
import ldap3
import logging
import os


def get_optional_env(key, default):
    """
    Return the value of an optional environment variable, and use
    the provided default if it's not set.
    """
    if not os.environ.get(key):
        logging.warning("The optional environment variable %s is not set, using '%s' as default" % (key, default))

    return os.environ.get(key, default)


def get_mandatory_env(key):
    """
    Return the value of a mandatory environment variable, and raise an
    Execption if it's not set.
    """
    if not os.environ.get(key):
        msg = "The mandatory environment variable {} is not set".format(key)
        logging.error(msg)
        raise Exception(msg)

    return os.environ.get(key)


def _get_LDAP_connection():
    """
    Return a LDAP connection
    """
    #ldap_server = get_mandatory_env('LDAP_SERVER_FOR_SEARCH')
    #ldap_base = get_mandatory_env('LDAP_BASE_DN')

    ldap_server = 'ldap.epfl.ch'
    ldap_base = "o=epfl,c=ch"

    server = ldap3.Server('ldap://' + ldap_server)
    connection = ldap3.Connection(server)
    connection.open()

    return connection, ldap_base


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
    except Exception as error:
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
    return username of user
    """
    attribute = 'uid'
    response = LDAP_search(
        pattern_search='(uniqueIdentifier=' + sciper + ')',
        attribute=attribute
    )
    return response[0]['attributes'][attribute][0]
