import sys
import reader

r=reader.Ler(sys.argv[1])

try:
    print(r.read())
finally:
    r.close()

