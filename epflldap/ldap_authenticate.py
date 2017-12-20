"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""
import re
import ldap3

from epflldap.utils import get_optional_env


class Authenticator:
    """ Class to authenticate users using LDAPS """

    def __init__(self):
        self.ldap_server = get_optional_env('EPFL_LDAP_SERVER_FOR_AUTHENTICATE')
        self.protocol = 'ldaps' if get_optional_env('EPFL_LDAP_USE_SSL') == 'true' else 'ldap'

        self.use_ssl = True if get_optional_env('EPFL_LDAP_USE_SSL') == 'true' else False
        self.uri = self.protocol + '://' + self.ldap_server
        self.dn = get_optional_env('EPFL_LDAP_BASE_DN_FOR_AUTHENTICATE')
        self.user_attr = get_optional_env('EPFL_LDAP_USER_SEARCH_ATTR')

    def get_user_dn(self, username):
        """
        Get the user distinguished name (dn)
        """
        server = ldap3.Server('ldap://' + self.ldap_server)
        connection = ldap3.Connection(server)
        connection.open()

        connection.search(
            search_base=self.dn,
            search_filter='(' + self.user_attr + '=' + username + ')'
        )
        return connection.response[0]['dn']

    def authenticate(self, username, password):
        """
        Authenticate the user with a bind on the LDAP server
        """

        if username is None or password is None:
            return False

        # check the username
        if not re.match("^[A-Za-z0-9_-]*$", username):
            return False

        user_dn = self.get_user_dn(username)

        server = ldap3.Server(
                self.uri,
                use_ssl=self.use_ssl
            )

        connection = ldap3.Connection(server, user=user_dn, password=password)

        return connection.bind()
