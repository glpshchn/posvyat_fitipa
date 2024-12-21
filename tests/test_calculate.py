import pytest
from unittest.mock import patch
from calculate import calc

def test_invalid_triangle_negative_sides():
    with pytest.raises(ValueError, match="The sides of a triangle cannot be negative."):
        calc('triangle', 'area', [3, -3, 5])

def test_invalid_triangle_sides_sum():
    with pytest.raises(ValueError, match="The sides do not form a triangle."):
        calc('triangle', 'area', [1, 2, 10])

def test_invalid_figure():
    with pytest.raises(ValueError, match="Figure 'hexagon' is not available"):
        calc('hexagon', 'area', [5])

def test_invalid_function():
    with pytest.raises(ValueError, match="Function 'volume' is not available."):
        calc('circle', 'volume', [5])

def test_invalid_circle_negative_radius():
    with pytest.raises(ValueError, match="The radius cannot be negative."):
        calc('circle', 'area', [-5])

def test_invalid_square_negative_side():
    with pytest.raises(ValueError, match="The side of the square cannot be negative."):
        calc('square', 'area', [-4])

def test_invalid_circle_parameters_count():
    with pytest.raises(ValueError, match="For figure 'circle', 1 parameter\\(s\\) are required, but 2 were provided."):
        calc('circle', 'area', [3, 4])

def test_invalid_triangle_parameters_count():
    with pytest.raises(ValueError, match="For figure 'triangle', 3 parameter\\(s\\) are required, but 2 were provided."):
        calc('triangle', 'area', [3, 4])

def test_valid_circle_area():
    with patch('builtins.print') as mocked_print:
        result = calc('circle', 'area', [4])
        assert result == pytest.approx(50.26548245743669)
        mocked_print.assert_called_with(
            'Area of circle with size(s) [4] is 50.26548245743669'
        )

def test_valid_circle_perimeter():
    with patch('builtins.print') as mocked_print:
        result = calc('circle', 'perimeter', [4])
        assert result == pytest.approx(25.132741228718345)
        mocked_print.assert_called_with(
            'Perimeter of circle with size(s) [4] is 25.132741228718345'
        )

def test_valid_square_area():
    with patch('builtins.print') as mocked_print:
        result = calc('square', 'area', [4])
        assert result == 16
        mocked_print.assert_called_with(
            'Area of square with size(s) [4] is 16'
        )

def test_valid_square_perimeter():
    with patch('builtins.print') as mocked_print:
        result = calc('square', 'perimeter', [4])
        assert result == 16
        mocked_print.assert_called_with(
            'Perimeter of square with size(s) [4] is 16'
        )

def test_valid_triangle_area():
    with patch('builtins.print') as mocked_print:
        result = calc('triangle', 'area', [3, 4, 5])
        assert result == pytest.approx(6.0)
        mocked_print.assert_called_with(
            'Area of triangle with size(s) [3, 4, 5] is 6.0'
        )

def test_valid_triangle_perimeter():
    with patch('builtins.print') as mocked_print:
        result = calc('triangle', 'perimeter', [3, 4, 5])
        assert result == 12
        mocked_print.assert_called_with(
            'Perimeter of triangle with size(s) [3, 4, 5] is 12'
        )
