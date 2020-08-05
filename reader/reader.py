import statistics


lista = [2, 5, 10, 11]
                # DO MODO CONVENCIONAL#
def above(l):
    data = []
    for v in l:
        if v > statistics.mean(l):
            data.append(v)
    return data

a1 = above(lista)
print(a1, 'e maior que', statistics.mean(lista))

                #USANDO LAMBDA E COMPREHENSION#
                
avg = statistics.mean(lista)
a2 = list(filter(lambda x: x > avg, lista))
print(a2, 'e maior que', avg)
