import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from square import area, perimeter

def test_negative_side_perimeter():
    a = -13
    with pytest.raises(ValueError):
        perimeter(a)

def test_negative_side_area():
    a = -13
    with pytest.raises(ValueError):
        area(a)

def test_zero_side_area():
    a = 0
    correct = 0
    assert area(a) == correct

def test_zero_side_perimeter():
    a = 0
    correct = 0
    assert perimeter(a) == correct

def test_positive_side_area():
    a = 13
    correct = a * a
    assert area(a) == correct

def test_positive_side_perimeter():
    a = 13
    correct = 4 * a
    assert perimeter(a) == correct
