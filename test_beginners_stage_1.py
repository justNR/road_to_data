import pytest
from beginners_stage_1 import is_odd, is_prime, is_arifm_progression


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
    

def test_digits_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(11)

def test_digits_is_not_prime():
    assert not is_prime(1)
    assert not is_prime(0)
    assert not is_prime(-1)

def tests_is_progression():
    assert is_arifm_progression(2,4,6)
    assert is_arifm_progression(3,6,9)
    assert is_arifm_progression(5,10,15)

def tests_is_not_progression():
    assert not is_arifm_progression(2,6,8)
    assert not is_arifm_progression(4,6,10)
    assert not is_arifm_progression(5,7,0)



