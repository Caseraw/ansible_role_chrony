import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_chrony_file(host):
    os = host.system_info.distribution
    if os == 'centos':
        f = host.file('/etc/chrony.conf')
        assert f.exists
        assert f.is_file
        assert f.user == 'root'
        assert f.group == 'root'
        assert f.mode == 0o644


def test_chrony_is_installed(host):
    chrony = host.package("chrony")
    assert chrony.is_installed


def test_chrony_is_running(host):
    if os == 'centos':
        service = host.service('chronyd')
        assert service.is_running
