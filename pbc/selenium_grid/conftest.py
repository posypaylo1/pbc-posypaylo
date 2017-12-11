import pytest
from pbc.selenium_grid.sg_setup import Grid


@pytest.fixture(scope="session")
def selenium_precondition():
    grid = Grid()
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(grid.send_command('pgrep java')) == 2
    yield grid.client
    grid.send_command('killall java')
    grid.close()