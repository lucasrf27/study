def escape_unicode(f):
    def wrap(*args, **kwargs):
        x= f(*args, **kwargs)
        return ascii(x)

    return wrap

def city():
    return 'Ϛlabama'



class callCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@callCount
def hello(name):
    print('name is {a}'.format(a = name))
        