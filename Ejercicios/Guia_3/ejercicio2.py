while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print("El resultado es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir por 0")
    finally:
        aux = input("¿Desea seguir sumando valores? (s/n): ")
        if aux.lower() != 's':
            break
