class Base():
    def __init__(self):
        print('base init')
    
    def t2 (self):
        print('base.t1')



class Sub(Base):
    def __init__(self):
        super().__init__()
        print('sub init')


    def t2 (self):
        print('sub.t2')


class Sub_sub(Sub):
    def __init__(self):
        super().__init__()
        print('SUB DO SUB')

    def t3(self):
        print('sub.t3')
