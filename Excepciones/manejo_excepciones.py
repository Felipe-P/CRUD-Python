from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))

    if a == b:
        # palabra reservada para lanzar una excepcion raise
        # raise ValueError
        # raise TypeError('Mensaje que acompaña el error')
        raise NumerosIdenticosException('Numeros identicos')
    resultado = a / b

# Tener en cuenta las excepciones padres e hijas para colocarlas en orden de ejecución
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')

# En caso de que no se haya lanzado ninguna exceocion
else:
    print('No se arrojo ninguna excepcion')

# Siempre se ejecuta independiante del except o el else
finally:
    print('Ejecucion de bloque finally')

print(f'Resultado: {resultado}')
print('continuamos...')
