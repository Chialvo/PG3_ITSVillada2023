class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"El alumno {self.nombre} tiene una nota de {self.nota}")
    
    def esta_regular(self):
        if self.nota >= 6:
            print(f"El alumno {self.nombre} está regular")
        else:
            print(f"El alumno {self.nombre} no está regular")

alumno1 = Alumno("Juan", 8)
alumno2 = Alumno("María", 5)

alumno1.imprimir()
alumno1.esta_regular()
alumno2.imprimir()
alumno2.esta_regular()