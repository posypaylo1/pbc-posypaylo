from numbers_pairs import number_pairs


EXPECTED_SEQUENCE = {(2, 8), (3, 7), (1, 9), (4, 6), (5, 5)}


def test_equals_to_expected_sequence():
    actual_sequence = number_pairs(list(range(10)))
    assert  actual_sequence == EXPECTED_SEQUENCE