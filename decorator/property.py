class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = '{}{}@gmail.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '%s %s' % (self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


t1= Employee('lucas', 'reimol')
t1.first = 'caco'

print(t1.first)
print(t1.last)
print(t1.email)
print(t1.full_name)