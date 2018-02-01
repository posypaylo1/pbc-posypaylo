import pytest
import time
from pbc.selenium_grid import Ssh, GridSetup
from selenium.webdriver import Firefox


@pytest.fixture(scope="module")
def ssh_client(request):
    client = Ssh('192.168.33.10', 'vagrant', 'vagrant')
    def fin():
        pass
        client.send_command('killall java')
        client.close()
    request.addfinalizer(fin)
    return client


@pytest.fixture()
def browser(request):
    driver = Firefox()
    request.addfinalizer(driver.close)
    return driver


@pytest.fixture(scope='session')
def run_grid(request):
    client = Ssh('192.168.33.10', 'vagrant', 'vagrant')
    grid = GridSetup(client)
    grid.download()
    grid.start_hub()
    grid.add_node()
    time.sleep(5)
    def fin():
        client.send_command('rm log.txt')
        client.send_command('killall java')
        client.close()
    request.addfinalizer(fin)