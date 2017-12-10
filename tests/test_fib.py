import pytest
from my_tested_app import fib


@pytest.mark.parametrize("test_input, expected", [
    (1, 1),
    (10, 10),
    (100, 100),
    (3.1, 0),
    ("this is string", 0),
    (0, 0),
    (-2, 0)
])
@pytest.mark.numbers
def test_input(setup_selenium, test_input, expected):
    assert len(setup_selenium) == 2
    assert len(fib(test_input)) == expected


@pytest.mark.numbers
def test_output_type_is_list():
    assert type(fib(4)) is list
