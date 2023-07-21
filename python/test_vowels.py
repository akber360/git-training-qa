import pytest
import vowels

def test_vowels():
    assert vowels.vowels("abcdefg") == 2
    assert vowels.vowels("aaaa") == 4
    assert vowels.vowels("bbbbb") == 0
    assert vowels.vowels("ooooaaaaeeeeiiiiouuu") == 20
