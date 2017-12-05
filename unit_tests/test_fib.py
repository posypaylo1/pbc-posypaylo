from fibonacci import fib

def test_quantity_of_numbers():
    assert len(fib(2)) == 2

def test_output_type_is_list():
    assert type(fib(4)) is list

def test_float_as_argument():
    assert len(fib(3.1)) == 0

def test_sting_as_argument():
    assert len(fib('this is string')) == 0

def test_use_zero_value_():
    assert len(fib(0)) == 0


