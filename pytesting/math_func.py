def add(a, b):
    print (a+b)
    return a+b

def lista():
    t1 = [5, 2, 3, 4]
    return t1


def counter(obj):
    index = 0
    for i in obj:
        index += 1
    return index
        

counter(lista())
print(len(lista()))