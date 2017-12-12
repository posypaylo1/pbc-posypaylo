import pytest
from pbc.selenium_grid.ssh_setup import Ssh
from pbc.selenium_grid.sg_setup import GridSetup


@pytest.fixture(scope="session")
def selenium_precondition(request):
    client = Ssh('192.168.33.10', 'vagrant', 'vagrant')
    grid = GridSetup(client)
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(client.send_command('pgrep java')) == 2
    def fin():
        client.send_command('rm log.txt')
        client.send_command('killall java')
        client.close()
    request.addfinalizer(fin)
    return client
