"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, subtract, multiply, divide, power, square_root
class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class


def test_add_negative_numbers():
    """Test addition with negative numbers."""
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2


def test_subtract_negative_numbers():
    """Test subtraction with negative numbers."""
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2

def test_power_function():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1


def test_square_root_function():
    assert square_root(4) == 2
    assert square_root(9) == 3

def test_square_root_negative():
    import pytest
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        square_root(-4)
