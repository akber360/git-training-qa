import pytest
import squares
#adasdas
def test_squares():
    assert squares.list_of_squares(2) == {1: 1, 2: 4}
    assert squares.list_of_squares(4) == {1: 1, 2: 4, 3: 9, 4: 16}
    assert squares.list_of_squares(6) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
    assert squares.list_of_squares(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    assert squares.list_of_squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    assert squares.list_of_squares(12) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
