import os
import testinfra.utils.ansible_runner
import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleVars(host):
    all_vars = host.ansible.get_variables()
    return all_vars


def test_app_directory(host, AnsibleVars):
    file_dest = AnsibleVars['app_dest']
    file_handler = host.file(str(file_dest))
    assert file_handler.exists
    assert file_handler.is_directory
    assert file_handler.mode == 0o775
    assert file_handler.group == 'deployers'

