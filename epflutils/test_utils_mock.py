try:
    from mock import patch, MagicMock
except:
    from unittest.mock import MagicMock, patch


@patch('epflutils.utils.get_sciper')
def test_get_sciper(get_sciper):

    mock_get_sciper = MagicMock(return_value="188475")
    get_sciper.return_value = mock_get_sciper()
    assert get_sciper(username="charmier") == "188475"

    mock_get_sciper = MagicMock(return_value="133134")
    get_sciper.return_value = mock_get_sciper()
    assert get_sciper(username='kermit') == "133134"


@patch('epflutils.utils.get_username')
def test_get_username(get_username):

    mock_get_username = MagicMock(return_value="charmier")
    get_username.return_value = mock_get_username()
    assert get_username(sciper="188475") == "charmier"

    mock_get_username = MagicMock(return_value="kermit")
    get_username.return_value = mock_get_username()
    assert get_username(sciper="133134") == "kermit"


@patch('epflutils.utils.get_units')
def test_get_units(get_units):

    mock_get_units = MagicMock(return_value=["13030"])
    get_units.return_value = mock_get_units()

    units = get_units(username="charmier")
    assert len(units) == 1
    assert '13030' == units[0]

    mock_get_units = MagicMock(return_value=["13029", "13030", "13051"])
    get_units.return_value = mock_get_units()

    units = get_units(username="ebreton")
    assert len(units) == 3
    assert '13029' == units[0]
    assert '13030' == units[1]
    assert '13051' == units[2]


@patch('epflutils.utils.is_unit_exist')
def test_is_unit_exist(is_unit_exist):

    mock_is_unit_exist = MagicMock(return_value=True)
    is_unit_exist.return_value = mock_is_unit_exist()

    # Success
    assert is_unit_exist(unit_id="13030")

    mock_is_unit_exist = MagicMock(return_value=False)
    is_unit_exist.return_value = mock_is_unit_exist()

    # Fail
    assert not is_unit_exist(unit_id="88")


@patch('epflutils.utils.get_unit_name')
def test_get_unit_name(get_unit_name):

    mock_get_unit_name = MagicMock(return_value="idevelop")
    get_unit_name.return_value = mock_get_unit_name()

    unit = get_unit_name(unit_id="13030")
    assert unit.lower() == "idevelop"
