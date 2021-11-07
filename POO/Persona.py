# class Persona:
#     # Init premite agregar y usar los atributos de la clase
#     # Atributos de objeto (instancia)
#     def __init__(self):
#         self.nombre = 'Juan'
#         self.apellido = 'Perez'
#         self.edad = 28
#
#
# persona1 = Persona()
# print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
# persona1.nombre = 'Andrea'
# persona1.apellido = 'Bedoya'
# print("Persona1:", persona1.nombre, persona1.apellido, persona1.edad)

# class Persona:
#     # Con parametos
#     # Pasar un tupla y un diccionario
#     def __init__(self, nombre, apellido, edad, *args, **kwards):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.args = args
#         self.kwards = kwards
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwards}')
#
#
# persona1 = Persona('Carol', 'Hernandez', 24)
# persona1.mostrar_detalle()
# persona1.telefono = '123465789'
# print(persona1.telefono)
# Persona.mostrar_detalle(persona1)

# persona2 = Persona('Pedro', 'Gomez', 10, '321654', 2, 3, 5, m='Manzana', p='Pera')
# persona2.mostrar_detalle()


# ENCAPSULAMIENTO

class Persona:
    # Con parametos
    # Pasar un tupla y un diccionario
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Property permite acceder al metodo como si fuera un atributo
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

#Condicion para ejecutar el codigo de este modulo
if __name__ == '__main__':
    persona1 = Persona('Carol', 'Hernandez', 24)
    persona1.nombre = 'Maria Fernanda'
    persona1.apellido = 'Gomez'
    persona1.edad = 18
    persona1.mostrar_detalle()

    # Imprimir el nombre del módulo
    print(__name__)
