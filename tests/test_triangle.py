import pytest
from triangle import area, perimeter
import math

def test_invalid_triangle_zero_sides_area():
    a, b, c = 0, 0, 5
    with pytest.raises(ValueError):
        area(a, b, c)

def test_invalid_triangle_sides_sum_area():
    a, b, c = 1, 2, 3
    with pytest.raises(ValueError):
        area(a, b, c)

def test_invalid_triangle_negative_sides_area():
    a, b, c = 3, -3, 5
    with pytest.raises(ValueError):
        area(a, b, c)

def test_valid_triangle_area():
    a, b, c = 3, 4, 5
    s = (a + b + c) / 2
    correct = math.sqrt(s * (s - a) * (s - b) * (s - c))
    assert area(a, b, c) == pytest.approx(correct)

def test_valid_triangle_perimeter():
    a, b, c = 3, 3, 5
    correct = a + b + c
    assert perimeter(a, b, c) == correct

def test_invalid_triangle_zero_sides_perimeter():
    a, b, c = 0, 3, 5
    with pytest.raises(ValueError):
        perimeter(a, b, c)

def test_invalid_triangle_sides_sum_perimeter():
    a, b, c = 1, 2, 3
    with pytest.raises(ValueError):
        perimeter(a, b, c)

def test_invalid_triangle_negative_sides_perimeter():
    a, b, c = -3, 3, 5
    with pytest.raises(ValueError):
        perimeter(a, b, c)
