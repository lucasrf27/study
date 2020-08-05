from django.template.defaultfilters import slugify


with open('People.txt') as file:
    l=[]
    l2=[]
    for row in file:
        t1 = row.split('\n')
        l.append(t1)
        s1 = slugify(t1)
        t2 = s1.split(', ')
        l2.append(t2)

print(l[1])
print(l2[1])