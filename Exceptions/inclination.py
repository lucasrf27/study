import math
import traceback

class InclinationErro(Exception):
    pass

def inclination(dx, dy):
    try:
        return print(math.degrees(math.atan(dy / dx)))
    except ZeroDivisionError as e:
        raise InclinationErro('nao pode por 0') from e


def main():
    try:
        inclination(0, 5)
    except InclinationErro as e:
        print(e.__traceback__)
        traceback.print_tb(e.__traceback__)


    finally:
        print('finish')

if __name__ == '__main__':
    main()

