def buble_sort(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if numeros[j] < numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    return numeros

numeros = [15, 8, 95, 33, 14, 7, 9]

print(buble_sort(numeros))