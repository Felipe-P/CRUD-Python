class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return f'{self.nombre} {other.nombre}'

# obj1 + obj2
# obj1.__add__(obj2)

persona1 = Persona('Felipe', 40)
persona2 = Persona('Luis', 16)

print(persona2 + persona1)
print(persona1.edad - persona2.edad)
