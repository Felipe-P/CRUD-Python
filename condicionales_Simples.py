nombre = input("Para comenzar, Cual es tu nombre?: ")

programacion = int(input(nombre + ", Cuál es tu calificación en programación: "))
inlges = int(input(nombre + ", Cuál es tu calificación en ingles: "))
logica = int(input(nombre + ", Cuál es tu calificación en logia: "))

promedio = int((programacion+inlges+logica)/3)

if promedio >= 6:
    print('Felicidades ' + nombre + ' aprobaste con un promedio de:', promedio)

print("Fin")