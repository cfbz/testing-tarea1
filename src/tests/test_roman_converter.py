import pytest
from src.roman_converter import convert

def test_converts_1_to_I():
    assert convert(1) == "I"