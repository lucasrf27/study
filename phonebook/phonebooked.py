import sys

class PhoneBook():

    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number
        print('ok')

    def lookup(self, name):
        return self.numbers[name]


    def __eq__(self, rhs):
        return self.numbers == rhs.numbers

    def consintancy(self, name):
        t2 = self.numbers[name]


    def is_prefix(self, name):
        lis = []
        for num in self.numbers:
           if self.numbers[num].startswith(self.numbers[name]):
                lis.append(num)
        lis.remove(name)
        return sorted(lis)

    def names(self):
        return self.numbers.keys()

t1 = PhoneBook()
t1.add('bob', '1234')
t1.add ('luc', '1')
t1.add('ana', '12')
t1.add('tina', '12345')

print(t1.is_prefix('luc'))


print (set(t1.names()))



'''
print(t1.numbers['luc'])

print('==============')
lis = []
for num in t1.numbers:
    if t1.numbers[num].startswith('12'):
        lis.append(num)
print(lis)

print('==============')

if t1.numbers['ana'] in t1.numbers:
    print('ok')

t1.add('alo', '123')
for name in t1.numbers:
    if t1.numbers[name].startswith(t1.numbers['alo']):
        raise BaseException ('deu merda')
'''