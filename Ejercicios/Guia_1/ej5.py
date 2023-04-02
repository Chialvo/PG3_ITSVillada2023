def comprobar(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

a = input("Ingrese una palabra: ")
print(comprobar(a))