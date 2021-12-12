# Polimorfismo: multiples formas en tiempo de ejecucion

from Empleado import *
from Gerente import *


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Felipe', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Carol', 10000, 'Sistemas')
imprimir_detalles(gerente)