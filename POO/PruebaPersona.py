from Persona import Persona

print('Creacion objetos'.center(30, '-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

#Imprimir el nombre del módulo, por si esta en otro
print(__name__)

print('Eliminacion de objetos'.center(30, '-'))
del persona1

