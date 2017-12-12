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

