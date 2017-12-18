"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""
import os

from epflldap.settings import CONSTANTS


class EpflLdapException(Exception):
    pass


def get_optional_env(key):
    """
    Return the value of an optional environment variable, and use
    the provided default if it's not set.
    """
    environment_variable_value = os.environ.get(key)
    if environment_variable_value:
        return environment_variable_value
    elif key in CONSTANTS:
        return CONSTANTS[key]
    else:
        raise Exception("The variable {1} is not set".format(key))
