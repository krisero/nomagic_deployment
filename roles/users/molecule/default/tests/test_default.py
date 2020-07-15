def test_group_deployers_exists(host):
    group = host.group("deployers")
    assert group.exists


def test_vagrant_user(host):
    user = host.user("vagrant")
    assert user.exists
    assert 'deployers' in user.groups


def test_john_snow_user(host):
    user = host.user("johnsnow")
    assert user.exists
    assert user.uid == 1040
    assert 'deployers' in user.groups
