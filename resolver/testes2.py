import socket

class Lucas():
    def __init__(self):
        self.lista = {}

    def __call__(self, host):
        if host not in self.lista:
            self.lista[host] = socket.gethostbyname(host)
        return self.lista[host]

    def clear(self):
        self.lista.clear()

    def has_host(self, host):
        return host in self.lista


    