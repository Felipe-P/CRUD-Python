#Set no mantiene un orden no permite almacenar elementos duplicados
#No permite modificar los elementos del set, pero si es posible agregar y eliminar elementos
# Contiene datos unicos, no repetidos

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#Largo de los elementos
print(len(planetas))

#Revisar si un elemento esta presente
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra')
print(planetas)

#No se puede duplicar elementos
planetas.add('Tierra')
print(planetas)

#Eliminar elementos con posible error
planetas.remove('Tierra')
print(planetas)

#Elimina un elemento
planetas.discard('Venus')
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set por completo
del planetas
print(planetas)