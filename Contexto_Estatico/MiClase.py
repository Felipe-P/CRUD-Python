class MiClase:
    # Variable que es igual para todos los que la acceden
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        # El valor de la variable puede cambiar con cada instancia u objeto
        self.variable_instancia = variable_instancia

    # El decorador permite asociar el metodo con la clase en si misma y no con los objetos
    # El metodo estatico no puede accder a las veriables de instancia (self)
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # Recibe el paraetro de la clase en su misma
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_instancia)
        print(self.variable_clase)

MiClase.metodo_estatico()
MiClase.metodo_clase()
print("Fin del metodo estatico y clase\n")

miObjeto1 = MiClase('Variable instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

# miclase1 = MiClase('Valor variable instancia')
# print(MiClase.variable_clase)
# print(miclase1.variable_instancia)
# print(miclase1.variable_clase)
#
# miclase2 = MiClase('Otro valor para variable instancia')
# print(miclase2.variable_instancia)
# print(miclase2.variable_clase)
#
# MiClase.variable_clase2 = 'Varible clase al vuelo'
# print(MiClase.variable_clase2)
# print(miclase1.variable_clase2)
# print(miclase2.variable_clase2)
