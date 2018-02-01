import requests
from pbc.selenium_grid import GridSetup
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def test_deploying_grid(ssh_client):
    grid = GridSetup(ssh_client)
    try:
        assert 'selenium-server-standalone-3.8.0.jar' in grid.get_list_of_files()
        assert 'sg-node.json' in grid.get_list_of_files()
    except AssertionError:
        grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(ssh_client.send_command('pgrep java')) == 2


def test_errors_in_log(ssh_client):
    grid = GridSetup(ssh_client)
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert not 'error' in str(ssh_client.send_command('cat log.txt'))


def test_check_grid_ui(run_grid, browser):
    browser.get("http://192.168.33.10:4444/grid/console")
    icons = browser.find_elements_by_xpath("//div[@class='content_detail']//img")
    assert len(icons) == 5


def test_nodes_rest(run_grid):
    r = requests.get('http://192.168.33.10:4444/grid/console')
    soup = BeautifulSoup(r.text, 'html.parser')
    # rows = soup.find_all('img')              # long way
    # lst = []
    # for row in rows:
    #     if str(row['src']).endswith('firefox.png'):
    #         lst.append(row)
    # assert len(lst) == 5
    assert len([x for x in soup.find_all('img') if str(x['src']).endswith('firefox.png')]) == 5  # short way


def test_remote_ui_demo(run_grid):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor='http://192.168.33.10:4444/wd/hub',
        desired_capabilities={'browserName': 'firefox'},
        options=options
    )
    try:
        driver.get("http://www.python.org")
        driver.save_screenshot('python.png')
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot('pycon.png')
        driver.get("http://www.python.org")
        # assert "No results found." not in driver.page_source
    except Exception as a:
        print a.message
        raise a
    finally:
        print 'close'
        driver.close()
