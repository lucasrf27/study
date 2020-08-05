l = [1, 2, 3, 4]


print(len(l))
l1 = iter(l)
for n in range (len(l)):
    print (next(l1))

print(list(l1))