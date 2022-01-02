try:
    # Si esta fuera de la carpeta debe espécificar la ruta completa
    # archivo = open('C:\\Users\\felip\\Documents\\Cursos desarrollados\\Curso_Python\\Archivos\\prueba.txt', 'r', encoding='utf8')

    archivo = open('prueba.txt', 'r', encoding='utf8')

    # print(archivo.read())

    # Leer algunos caracteres
    # print(archivo.read(5))

    # Leer lineas completas
    # print(archivo.readline())

    # Iterar linea por linea el archivo
    # for linea in archivo:
    #     print(linea)

    # Leer lineas
    # print(archivo.readlines())

    # Leer una línea en específico
    # print(archivo.readlines()[1])

    # Copiar el contenido de un archivo
    # a - Anexar informacion
    # w - escribir informacion desde 0

    archivo2 = open('copia.txt', 'w', encoding='utf8')
    archivo2.write(archivo.read())
    archivo.close()
    archivo2.close()

except Exception as e:
    print(e)
finally:
    archivo.close()