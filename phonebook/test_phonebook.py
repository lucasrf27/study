from phonebooked import PhoneBook
import pytest


def test_add():
    t2 = PhoneBook()
    t2.add('joe', 123456)
    assert t2.lookup('joe') == 123456
    assert t2.numbers['joe'] == 123456
    with pytest.raises(KeyError):
        t2.lookup('mari')
    with pytest.raises(TypeError):
        t2.lookup()
        

def test_zero_divisio():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    with pytest.raises(BaseException) as excinfo:

        def f():
            f()
        f()

def test_missing_name():
    t1 = PhoneBook()
    with pytest.raises(KeyError):
        t1.lookup('ana')

def test_is_prefix():
    t1 = PhoneBook()
    t1.add('bob', '1234')
    t1.add('tina', '12345')
    t1.add('caco', '12')
    assert t1.is_prefix('bob') == ['tina']
    assert t1.is_prefix('caco') == sorted(['bob', 'tina'])
    assert 'caco' not in t1.is_prefix('bob')