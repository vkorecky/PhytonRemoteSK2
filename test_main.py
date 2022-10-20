import pytest

import main

from main import add, subtract, divide, multiply


class TestClass:

    @pytest.fixture()
    def numbers(self):
        x = 10
        y = 20
        z = 25
        return [x, y, z]

    def test_add_2(self, numbers):
        x = numbers[0]
        y = numbers[1]
        assert add(x, y) == 30

    @pytest.mark.custom_mark
    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (1.5, 0.5, 2), (10, 100, 110)])
    def test_add(self, x, y, z):
        assert add(x, y) == z

    @pytest.mark.parametrize("a, b, c", [(3, 2, 1), (10, 5, 5), (100, 60, 40)])
    def test_subtract(self, a, b, c):
        assert subtract(a, b) == c

    @pytest.mark.parametrize("x, y, z", [(1, 2, 2), (3, 3, 9), (-1, 5, -5)])
    def test_multiply(self, x, y, z):
        assert multiply(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(1, 2, 0.5), (3, 3, 1), (50, 5, 10)])
    def test_divide(self, x, y, z):
        assert divide(x, y) == z
