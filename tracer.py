class Tracer():
    def __init__(self):
        self.enable = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enable == True:
                print ('calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Tracer()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


class IslandMaker():  
    def __init__(self, f):
        self.f = f

    def make_island(self, name):
        return name + self.f

    
        



