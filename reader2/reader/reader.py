import os
from compressed import gzipped, bzipped

extention_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener

}

class Ler:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(self.filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()