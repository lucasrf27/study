def testing():
    '''
    DOC
    '''
    a = 2
    def testing2():
        print('ok')

print(testing.__doc__)

class Teste():

    def __init__(self): 
        self.a = 1

    def tent(self):
        self.a = 0
        def tent2(self):
            self.a = 3
        tent2(self)

t1 = Teste()
print(t1.a)
t1.tent()
print(t1.a)
t = Teste()
