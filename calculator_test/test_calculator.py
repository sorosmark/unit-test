# python -m pytest test_calculator.py -v 
import pytest
from calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(-2, -2) == -4

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, -3) == 5
    assert subtract(-5, -3) == -2

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(2, -3) == -6
    assert multiply(-5, -3) == 15

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, -2) == -2.5
    assert divide(-9, -3) == 3