t1 = [int (i) for i in range(5)]
l = [1, 2, 3, 4]
t = 0
for v in t1:
    t += v
    print('SOMA', v)

    print (t)

'''
t1 = [int (i) for i in range(5)]
i = (str (i) for i in range(5))

bigger = filter(lambda x : x > 2, t1)
bigger2 = filter(lambda x : x > '2', i)

'''

'''
i = map(str, range(5))
j = filter(i = '1')
print(list(i))
print(list(j))
'''