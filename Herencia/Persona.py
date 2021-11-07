class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Sobreescribe el metodo
    def __str__(self):
        return f'Persona[Nombre: {self.nombre} edad: {self.edad}]'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # Contructor que permite accedeer a los metodos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Empleado[Sueldo: {self.sueldo}]'


# class Vehiculo():
#     def __init__(self, color, ruedas):
#         self.color = color
#         self.ruedas = ruedas
#
#     def __str__(self):
#         return f'Color: {self.color} Ruedas: {self.ruedas}'
#
#
# class Coche(Vehiculo):
#     def __init__(self, color, ruedas, velocidad):
#         super().__init__(color, ruedas)
#         self.velocidad = velocidad
#
#     def __str__(self):
#         return f'Vehiculo: {super().__str__()} Coche: velocidad: {self.velocidad}'
#
#
# class Bicicleta(Vehiculo):
#     def __init__(self, color, ruedas, tipo):
#         super().__init__(color, ruedas)
#         self.tipo = tipo
#
#     def __str__(self):
#         return f'Vehiculo: {super().__str__()} Coche: velocidad: {self.tipo}'
#
#
# vehiculo1 = Vehiculo('Negro', 4)
# print(vehiculo1)
#
# coche1 = Coche('Rojo', 4, 190)
# print(coche1)
#
# bicicleta1 = Bicicleta('Rosa', 2, "Montana")
# print(bicicleta1)
