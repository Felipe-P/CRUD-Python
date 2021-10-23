class Aritmetica:
    """
    Clase aritmetica para realizar operaciones
    """

    # Método dunder (double underline)

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmerica1 = Aritmetica(5, 30)
print(f'Suma: {aritmerica1.sumar()}  \nResta: {aritmerica1.restar()}')
print(f'Multiplicacion: {aritmerica1.multiplicar()} \nDivision: {aritmerica1.dividir():.3f}')
