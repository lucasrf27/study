class Trace:
    def __init__(self):
        self.enable=True

    def __call__(self, f):
        def wrap (*args, **kwargs):
            if self.enable:
                print ('calling{}'.format(f))
            return f(*args, **kwargs)
        return wrap
    
tracer = Trace()

@tracer
def rotate_list(l): 
    result = l[1:] + [l[0]]
    return result

