from Clases.Orden import Orden
from Clases.Producto import Producto

producto1 = Producto('Mouse', 130.00)
producto2 = Producto('Teclado', 95.00)
producto3 = Producto('Torre', 120.00)
producto4 = Producto('Monitor', 69.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
orden2 = Orden(productos2)
print(f'{orden1}\nTotal: {orden1.calcular_total()}')
print(f'{orden2}\nTotal: {orden2.calcular_total()}')
