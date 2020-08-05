

class Names():
    def __init__(self):
        self.lista = {}

    def __call__(self, nome):
        if nome not in self.lista:
            self.lista[nome]= len(nome)
        return self.lista[nome]

