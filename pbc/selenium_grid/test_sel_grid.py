from pbc.selenium_grid.sg_setup import Grid


def test_sel_grid(selenium_precondition):
    grid = Grid()
    assert len(grid.send_command('pgrep java')) == 2
    stdout = grid.send_command('cat log.txt')
    errors = []
    for row in stdout:
        if 'error' in row:
            errors.append(row)
    if errors:
        raise Exception('errors detected')

