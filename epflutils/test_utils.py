from epflutils.utils import get_username


def test_get_username():

    assert get_username(sciper="188475") == 'charmier'
