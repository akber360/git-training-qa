import pytest
import squares

def test_squares():
    assert squares.list_of_squares(2) == {1: 1, 2: 4}
