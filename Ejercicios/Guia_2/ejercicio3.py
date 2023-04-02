class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def es_equilatero(self):
        return self.lado1 == self.lado2 == self.lado3


# Ejemplo de uso
triangulo = Triangulo(5, 5, 5)
print("El lado mayor es:", triangulo.lado_mayor())
print("¿Es equilátero?:", triangulo.es_equilatero())