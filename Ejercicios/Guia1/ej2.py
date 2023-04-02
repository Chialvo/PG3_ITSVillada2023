def comprobar(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio = int(input("Ingrese un año: "))

if comprobar(anio):
    print(anio, "es un año bisiesto.")
else:
    print(anio, "no es un año bisiesto.")
