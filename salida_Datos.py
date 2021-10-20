codpais = 34
# Rellena con ceros a la izquierda
print(str(codpais).zfill(4))

valor = 2.34565676
print('Valor aprox. {0:.3f}'.format(valor))

nombre = 'Claudio'
edad = 35
altura = 1.82
#%s cadena, %i entero, %f numero con decimales
#%10s reserva 10 posiciones y alinea a la izquierda (tabular) %-10s derecha
print('Tiene %i años' % edad)
print('%s tiene %i años y mide %.3f' % (nombre, edad, altura))

print(f'Datos {valor}-{nombre}')