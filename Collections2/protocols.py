class Test1():
    def __init__(self, lista):
        self.lista = lista
   
t1 =  Test1([5, 2 , 3])
print(t1.lista[2])


class Test2():
    def __init__(self, lista):
        self.lista = lista
    
    def __getitem__(self, index):
        return self.lista[index]

t2 = Test2([5, 2, 3])
print(t2[2])


    
