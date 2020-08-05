
class Scope():
    def __init__(self):
        self.message = 'global'
     
    def func(self):
        self.message = 'func'
        def local(self):
            self.message = 'local'
            print(self.message)
        
        

s = Scope()
print(s.message)
s.func()
print(s.message)