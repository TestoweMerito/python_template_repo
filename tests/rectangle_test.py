# tests/test_rectangle.py
import pytest
from logic.rectangle import area, perimeter

def test_area():
    assert area(2, 3) == 6
    assert area(0, 5) == 0

def test_perimeter():
    assert perimeter(2, 3) == 10
    assert perimeter(0, 5) == 10