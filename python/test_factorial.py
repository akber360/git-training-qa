import pytest
import factorial

def test_factorial():
    assert factorial.fact(0) == 1
    assert factorial.fact(4) == 24
    assert factorial.fact(3) == 6
    assert factorial.fact(7) == 5040
    assert factorial.fact(7) == 5040 # should fail