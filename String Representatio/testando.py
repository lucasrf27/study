from django.template.defaultfilters import slugify
from django.db import models



class People(models.Model):
    user = None
    cpf = None
    birthday = None
    id = 0
    t1 = []

    def __init__(self):
        with open('People.txt') as file:
            for row in file:
                t1 = row.split(', ')
                self.user = slugify(t1[0])
                self.cpf = t1[1]
                self.birthday = t1[1]
                self.id += 1
                t1.append(row)
                People.user = self.user
                People.cpf = self.cpf
                People.birthday = self.birthday
                People.id = self.id
                People.save()
'''
c1 = 0
with open('People.txt') as file:
    for row in file:
        c1 += 1
        t1 = row.split(', ')
        user = slugify(t1[0])
        cpf = t1[1]
        print(t1)
'''

