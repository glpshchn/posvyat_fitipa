import pytest
from circle import area, perimeter
import math

def test_negative_radius_perimeter():
    r = -52
    with pytest.raises(ValueError):
        perimeter(r)

def test_negative_radius_area():
    r = -52
    with pytest.raises(ValueError):
        area(r)

def test_zero_radius_area():
    r = 0
    correct = 0
    assert area(r) == correct

def test_zero_radius_perimeter():
    r = 0
    correct = 0
    assert perimeter(r) == correct

def test_positive_radius_area():
    r = 52
    correct = math.pi * r * r
    assert area(r) == pytest.approx(correct)

def test_positive_radius_perimeter():
    r = 52
    correct = 2 * math.pi * r
    assert perimeter(r) == pytest.approx(correct)
