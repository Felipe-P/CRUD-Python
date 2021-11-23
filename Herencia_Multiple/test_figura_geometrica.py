from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='Azul')
cuadrado1.alto = -15
print(f'Área C: {cuadrado1.calcular_area()}')
print(f'Cuadrado: {cuadrado1}')

print('Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(8, 3, 'Rojo')
rectangulo1.alto = -15
print(f'Área R: {rectangulo1.calcular_area()}')
print(f'Rectangulo: {rectangulo1}')

# Method Resolution Order, muestra el orden en que se van a ejecutar los metodos segun la jerarquia
print(Cuadrado.mro())
print(Rectangulo.mro())
