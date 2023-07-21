import pytest

def f():
    return 3

def test_function():
    assert f() == 4

def func(num):
    return num * 2

def test_answer():
    assert func(6) == 10