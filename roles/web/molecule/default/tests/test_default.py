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
    file_version = AnsibleVars['app_version']
    file_handler = host.file(str(file_dest) + "/" + str(file_version))
    assert file_handler.exists
    assert file_handler.is_directory
    assert file_handler.mode == 0o775
    assert file_handler.group == 'deployers'


def test_git_is_installed(host):
    pkg = host.package("git")
    assert pkg.is_installed


def test_app_repository(host, AnsibleVars):
    file_dest = AnsibleVars['app_dest']
    file_version = AnsibleVars['app_version']
    file_handler = host.file("{}/{}/.git".format(str(file_dest), str(file_version)))
    assert file_handler.exists
    assert file_handler.is_directory
    git_config_handler = host.file("{}/{}/.git/config".format(str(file_dest), str(file_version)))
    assert git_config_handler.exists
    assert git_config_handler.is_file
    assert git_config_handler.contains(AnsibleVars['app_repository'])
    assert host.run("cd {}/{} & git rev-parse --is-inside-work-tree".format(str(file_dest), str(file_version)))


def test_nginx_config(host):
    nginx_conf_file = host.file("/etc/nginx/nginx.conf")
    assert nginx_conf_file.exists
    assert nginx_conf_file.is_file
    assert nginx_conf_file.group == 'deployers'
    conf_file = host.file("/etc/nginx/conf.d/example.conf")
    assert conf_file.exists
    assert conf_file.is_file
    assert conf_file.group == 'deployers'
