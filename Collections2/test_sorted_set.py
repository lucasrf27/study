import pytest
from .sorted_set import SortedSet


t0 = SortedSet([])
t2 = SortedSet([5, 2 ,3])
t3 = SortedSet(range(55))

def test_empty():
    assert t0.all_items == []
    
def test_sort():
    assert t2.all_items == [2, 3, 5]
    assert t2.all_items[0] <= t2.all_items[1]
    assert t2[0] <= t2[1]

def test_container():
    assert 5 in t2.all_items
    assert 4 not in t2.all_items

def test_len():
    assert len(t3.all_items) == 55

# COM __iter__():

def test_iter():
    i = iter(t2.all_items)
    assert next(i) == 2
    assert next(i) == 3
    assert next(i) == 5

# SEM __iter__():

def test_iter2():
    i = iter(t2)
    assert next(i) == 2
    assert next(i) == 3
    assert next(i) == 5


# SEM __getitem__():
def test_for():
    index = 0
    # sem __iter__():
    i = iter(t2.all_items)
    for item in range (len(t2.all_items)):
        assert t2.all_items[index] == next(i)
        index += 1


# COM __getitem__(): basicamente nao precisa chamar o all_items
def test_for2():
    index = 0
    # pode chamar iter(t2) por causa do __iter__():
    i = iter(t2)
    for item in range (len(t2.all_items)):
        assert t2[index] == next(i)
        index += 1

def test_slice():
    assert t2[1:] == [3, 5]
    assert t2[1:2] == [3]
    assert SortedSet([5, 2 ,3])[:2] == [2, 3]


def test_repr():
    assert repr(t0) == 'SortedSet {}'.format(t0.all_items)
    assert repr(t2) == 'SortedSet {}'.format(t2.all_items)
        

def test_equal():
    assert SortedSet([5, 2, 3]) == SortedSet([5, 2, 3])

# SEM __reverseder__(): mas com __getitem__ e __len__
def test_reverse():
    assert list(reversed(t2)) == [5, 3, 2]
    r1 = list(reversed(t2))
    i = iter(r1) 
    assert next(i) == 5
    assert next(i) == 3
    assert next(i) == 2

# com __reverseder__():
def test_reverse2():
    assert t2.__reverseder__() == [5, 3, 2]
    assert list(reversed(t2.all_items)) == [5, 3, 2]
    i = iter(t2.__reverseder__())
    assert next(i) == 5
    assert next(i) == 3
    assert next(i) == 2

def test_index():
    assert t2.all_items.index(2) == 0
    assert t2.all_items.index(3) == 1
    assert t2.all_items.index(5) == 2

def test_count():
    assert t2.all_items.count(11) == 0
    assert t2.all_items.count(3) == 1
    t2.all_items.append(3)
    assert t2.all_items.count(3) == 2
    assert t2.__count__(3) == 2