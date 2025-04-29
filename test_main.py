# test_main.py

from codepractice1 import add, subtract, is_even

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print('pASS')
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
