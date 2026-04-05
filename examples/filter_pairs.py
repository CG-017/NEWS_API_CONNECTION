"""Uso de la función filter para filtrar elementos de una lista según una condición específica. En este caso, se filtran los números pares de una lista de números del 1 al 10."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []

for num in numbers:
    if num % 2 == 0:
        pairs.append(num)

print(numbers)
print(pairs)


def is_pair(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


pairs_filter = list(filter(is_pair, numbers))
print(pairs_filter)
