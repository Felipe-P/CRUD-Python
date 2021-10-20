diccionario = {'Cancion': "Africa", 'Genero': "Rock", 'Reproducciones': 10}

print(diccionario['Reproducciones'])

# Tamaño
print(len(diccionario))

# Acceder a un elemento
print(diccionario.get('Genero'))

# Modificar un elemento
diccionario['Reproducciones'] = 15
print(diccionario)

# Recorre un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Recorrer solo los terminos
for termino in diccionario.keys():
    print(termino)

# Recorrer solo los terminos
for valor in diccionario.values():
    print(valor)

# Comprobar si un elemento existe
print('Cancion' in diccionario)

# Agregar un elemento
diccionario['Autor'] = 'TOTO'
print(diccionario)

# Eliminar un elemento
diccionario.pop('Reproducciones')
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
print(diccionario)