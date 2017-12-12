from selenium.webdriver import Firefox


def test_sel_grid(selenium_precondition):
    client = selenium_precondition
    assert len(client.send_command('pgrep java')) == 2
    stdout = client.send_command('cat log.txt')
    errors = []
    for row in stdout:
        if 'error' in row:
            errors.append(row)
    if errors:
        raise Exception('errors detected')


def test_check_grid():
    driver = Firefox()
    driver.get("http://192.168.33.10:4444/grid/console")
    icons = driver.find_elements_by_xpath("//div[@class='content_detail']//img")
    assert len(icons) == 5
    driver.close()