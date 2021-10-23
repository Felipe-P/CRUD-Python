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

class Persona:
    # Con parametos
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Carol', 'Hernandez', 24)
persona1.mostrar_detalle()
persona1.telefono = '123465789'
print(persona1.telefono)
# Persona.mostrar_detalle(persona1)

persona2 = Persona('Pedro', 'Gomez', 10)
persona2.mostrar_detalle()
