# With abre y cierra el archivo de manera automática, conocido como context manager

# with open('prueba.txt', 'r', encoding='utf8') as archivo:
from Archivos.ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

