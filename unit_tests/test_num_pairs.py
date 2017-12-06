import pytest
from my_tested_app import number_pairs


TEN_ITEMS_IN_LIST = {(2, 8), (3, 7), (1, 9), (4, 6), (5, 5)}
MORE_THAN_TEN = {(5, 5), (4, 6), (2, 8), (0, 10), (1, 9), (3, 7)}
NINE_ITEMS = {(2, 8), (3, 7), (4, 6), (5, 5)}
EIGHT_ITEMS = {(3, 7), (4, 6), (5, 5)}
SEVEN_ITEMS = {(4, 6), (5, 5)}
SIX_ITEMS = {(5, 5)}
LESS_THAN_SIX = set()


@pytest.mark.pairs
@pytest.mark.parametrize("length, expected", [
    (10, TEN_ITEMS_IN_LIST),
    (20, MORE_THAN_TEN),
    (100, MORE_THAN_TEN),
    (9, NINE_ITEMS),
    (8, EIGHT_ITEMS),
    (7, SEVEN_ITEMS),
    (6, SIX_ITEMS),
    (5, LESS_THAN_SIX)
])
@pytest.mark.pairs
def test_input(length, expected):
    actual_sequence = number_pairs(length)
    assert actual_sequence == expected

