mi_lista = ["Hola", 24, 69.5, "Otro dato", 57]

print(mi_lista[:3])
mi_lista[2] = "dato"
print(mi_lista[1:])
print(mi_lista[-2])
print(mi_lista)

#+ concatena listas
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# #* repite una lista x numero de veces
a = [0] * 4
print(a)
b = [1, 2, 3] * 3
print(b)

#Muestra solo una parte de la lista
t = ["a", "b", "c", "d", "e", "f"]
print(t[1:3])
print(t[:4])
t[1:3] = ["x", "y", "z"]
print(t)
print(len(t))
print(max(t))
print(min(t))
#print(sum(t))
#print(sum(t)/len(t))


#insertar datos en la posicion
t.append("H")
print(t)

#insertar datos en la posicion
t.insert(7, "g")
print(t)

#elimina datos
t.remove("g")
print(t)

#Elimina un indice
del t[5]
print("Eliminando indice", t)

#Eliminar datos por indice pop(indice o vacio para ultimo), o por valor remove("dato")
t.pop(0)
print(t)

#Lista en reversa
t.reverse()
print(t)

#Ordanar en forma ascendente
t.sort()
print(t)



