try:
    articulos = int(input('Articulos: '))
    precio = int(input('Precio: '))
    print('Pagar: ' + str(articulos * precio) + '$')

except:
    print('Error, deben ser numeros')
