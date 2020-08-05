from collections.abc import Sequence
from datetime import datetime



class SortedSet():

    all_items = [2, 4, 1, 3]

    def __init__(self, items):
        self.all_items = sorted(items)

    def __contains__(self, item):
        return item in self.all_items

    def __iter__(self):
        return iter(self.all_items)

    def __getitem__(self, index):
        return self.all_items[index]

    def __repr__(self):
        return 'SortedSet {}'.format(self.all_items)

    def __eq__(self, rhs):
        return self.all_items == rhs.all_items

    def __ne__(self, rhs):
        return self.all_items == rhs.all_items
    
    def __len__(self):
        return len(self.all_items)

    def __count__(self, item):
        lista = []
        c = 0
        for item1 in self.all_items:
            lista.append(item1)
        for p in range(len(lista)):
            if item in lista:
                c += 1
                lista.remove(item)
            else :
                pass
        return (c)

    def __reverseder__(self):
        lista = []
        r1 = list(reversed(self.all_items))
        i1 = iter(r1)
        for item in self.all_items:
            lista.append(next(i1))
        return lista

    def __indexer__(self, x):
        c = 0
        for item in self.all_items:
            c += 1
            if item == x:
                break
        return (c - 1)


t1 = SortedSet([5,2,3])
print(t1.__doc__)
'''
t1 = SortedSet([5, 2 , 3])
i = t1.all_items[2]
t2 = SortedSet([5, 5, 5, 2 ,3, 3, 3, 3, 3, 3])

t3 = SortedSet([5, 2 , 3])
print(t3.__reverseder__())
print(reversed(t3.all_items))
print(t3.all_items)
print(t3.__count__(4))
print(list(t3).count(2))
'''
'''
print(t1.__indexer__(2))
print(list(reversed(t1)))
'''

'''
print(list(reversed(t1.all_items)))
if t1 == t2:
    print('ok')

print(t1.index(5))

'''





'''
print(t1.__eq__(t2))
print(t1.count(5))
print(t1.__counter__(5))
print(repr(t1))
print(list(reversed(t1)))
print(t1.__reverseder__())


'''
#COUNTER
'''
lista = [5, 2, 2,  3 ]
for item in SortedSet([5, 2 ,3]).all_items:
    lista.append(item)
print(lista)
print ('----------------')
'''
#REVERSEDER
'''
print(t1.__count__(2))
print('=-=====================')
print (i.__index__())
print(list(reversed(lista)))
r1 = list(reversed(lista))
i1 = iter(r1)
print(next(i1))
print(next(i1))
print(next(i1))

t1 = SortedSet(range(10))
t2 = SortedSet([])

print (t1.__reversed__())
'''

'''
print(t1[9])
print(t1.__repr__())
print(repr(t2))
print(t1.all_items)
print(t1.all_items.reversed)
'''

#CONTAINS
'''
print(t1.all_items)
print(t1.__contains__(11))
print(len(t1.all_items))

i = iter(t1.all_items)
for item in range (len(t1.all_items)):
    print(next(i))

'''
#ITER
'''
index = 0
i = iter(t1.all_items)
for item in range(len(t1.all_items)):
        print(t1.all_items[index])
        print(next(i))
        print('index{}'.format(index))
        index += 1
'''