"""Ejemplo de uso de la función map() para aplicar una función a cada elemento de una lista. En este caso, se calcula el cuadrado de cada número en una lista de números del 1 al 5."""

numeros = [1, 2, 3, 4, 5]
cuadrado = []

for num in numeros:
    cuadrado.append(num**2)

print(numeros)
print(cuadrado)


def square(num):
    return num**2


cuadrados_map = list(map(square, numeros))
print(cuadrados_map)
