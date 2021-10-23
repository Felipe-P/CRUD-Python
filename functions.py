def holamundo():
    print('Hola Mundo')


holamundo()


def rholamundo():
    return 'Hola Mundo'


print(rholamundo())


def paramfunction(param1, param2):
    print(param1)
    print(param2)
    print(f'Parametro1: {param1}, Parametro2: {param2}')


paramfunction('Dato1', 59.05)


# def suma():
#     x = input('Ingrese el valor de x: ')
#     y = input('Ingrese el valor de y: ')
#     z = None
#     if x.isnumeric() and y.isnumeric():
#         z = int(x) + int(y)
#     return z
#
# print(suma())

# Funcion que recibe x cantidad de parametros
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'Carlos', 'Andres', 'Pedro')


# def multNumeros(*args):
#     resultado = 1
#     for data in args:
#         resultado *= data
#     return resultado
#
# print(multNumeros(1, 3, 5))

# Funcion que recibe un diccionario
def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')


listarTerminos(Nombre='Juan Perez', Edad=15)


# Funcion que recibe una lista
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Ana', 'Carlos', 'Maria']
desplegarNombres(nombres)
desplegarNombres('Andres')
desplegarNombres([10, 20, 30])


# Recursividad
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


print(factorial(6))


def numeros(numero):
    if numero >= 1:
        print(numero)
        return numeros(numero - 1)


print(numeros(6))