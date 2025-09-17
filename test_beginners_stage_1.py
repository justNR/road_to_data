import pytest
from beginners_stage_1 import is_odd


def test_digits_divide_3():
    assert is_odd(9)
    assert is_odd(12)
    assert is_odd(3)

def test_digits_not_divide_3():
    assert not is_odd(2)
    assert not is_odd(4)
    assert not is_odd(8)


def test_divide_by_zero():
    assert is_odd(0)

def test_negative_digits_divide_3():
    assert is_odd(-3)
    assert is_odd(-6)
    assert is_odd(-15)

def test_negative_digits_not_divide_3():
    assert not is_odd(-1)
    assert not is_odd(-5)
    assert not is_odd(-7)
