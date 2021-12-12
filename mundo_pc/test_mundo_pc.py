from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    teclado1 = Teclado('HP', 'USB')
    monitor1 = Monitor('HP', 19)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)

    raton2 = Raton('Razer', 'Bluetooth')
    teclado2 = Teclado('Razer', 'USB')
    monitor2 = Monitor('Asus', 32)
    computadora2 = Computadora('DELL', monitor2, teclado2, raton2)

    raton3 = Raton('Gamer', 'Bluetooth')
    teclado3 = Teclado('Gamer', 'Bluetooth')
    monitor3 = Monitor('Gamer', 19)
    computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

computadoraLista1 = [computadora1, computadora2]
orden1 = Orden(computadoraLista1)
# print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoraLista2 = [computadora2, computadora3]
orden2 = Orden(computadoraLista2)
print(orden2)
