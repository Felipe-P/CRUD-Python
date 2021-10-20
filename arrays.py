import numpy as np
import random

n = int(input('Ingrese el tamano del arreglo: '))
m = int(input('Ingrese el numero de multiplos: '))

a = []
for i in range(0, n):
    a.append(i * m)
print(a)

#Numeros impares a 3
#Append agraga un elemento al final de la lista
a = [1, 5, 8, 9, 30, 9, 13, 3, 2]
b = []
for i in a:
    if i > 3 and i % 2 != 0:
        b.append(i)
print(b)

#Encontrar un color
import random
colores = ["Azul", "Rojo", "Negro", "Naranja"]
color = input("En que color estoy pensando: ")
pc = random.randint(0,3)
if color == colores[pc]:
    print("Pensamos en el mismo color")
else:
    print("Lo siento, mi color es:", colores[pc])
