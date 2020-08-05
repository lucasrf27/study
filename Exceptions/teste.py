

def teste():
    try:
        a = int(input("um numero"))
        b = int(input("divisor"))
        assert a < b , 'A MENOR Q B'
        print(a/b)

    except ValueError as e:
        print('VALOR ERRADO')

    except ZeroDivisionError as e:
        print('nao divisivel por 0', e)
        print(e.__cause__)

    finally:
        print(' ACABOU')

teste()