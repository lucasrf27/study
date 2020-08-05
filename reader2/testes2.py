import testes

testes.register('lucas')
testes.register('caco')

for name in testes.registered_names():
    print(name)