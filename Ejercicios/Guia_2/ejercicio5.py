class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Sueldo: {self.sueldo}")
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")


persona = Persona("", 0)
persona.cargar_datos()
persona.imprimir_datos()

empleado = Empleado("", 0, 0)
empleado.cargar_datos()
empleado.imprimir_datos()
