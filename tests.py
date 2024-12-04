import pytest
from main import calculate_discriminant

def test_positive_discriminant():
    assert calculate_discriminant(1, 5, 6) == 1  

def test_zero_discriminant():
    assert calculate_discriminant(1, 2, 1) == 0  

def test_negative_discriminant():
    assert calculate_discriminant(1, 2, 3) == -8  #
