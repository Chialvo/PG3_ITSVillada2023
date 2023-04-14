strings = ["Hola", "men", "como estas?"]
try:
    with open("Guia_3/archivo.txt", "w") as f:
        for string in strings:
            f.write(string + "\n")
        f.write(42) 
except TypeError:
    print("Error: No se puede escribir un entero en un archivo de texto.")