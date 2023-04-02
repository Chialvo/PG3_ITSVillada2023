class Familia:
    def __init__(self, nombre_padre, nombre_madre, hijos):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.hijos = hijos

    def __str__(self):
        nombres_hijos = ", ".join(self.hijos)
        return f"Padre: {self.nombre_padre}\nMadre: {self.nombre_madre}\nHijos: {nombres_hijos}"

familia = Familia("Lautaro", "Sofia", ["Pedro", "Renzo", "Teo"])
print(familia)
