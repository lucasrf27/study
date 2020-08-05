from math_func import add, lista, counter


def test_add():
    assert add(7,3) == 10
    assert add (8,10) == 18



def test_add_strings():
    result = 'ola lucas'
    assert add('ola', ' lucas') == result
    assert type(result) == str


def test_lista():
    t2 = lista()
    assert 2 and 5 in t2

def test_counter():
    t3 = counter(lista())
    assert t3 == len(lista())