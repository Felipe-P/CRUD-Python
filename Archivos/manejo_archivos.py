try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agragamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
