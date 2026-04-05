"""Typing con Python"""

from typing import Any  # proyectos que inician y no se sabe el tipo de dato (no abusar)

variable = 42  # python automatica mente lo caracteriza como int

print(f"Variable: {variable}, del tipo: {type(variable)}")

variable = "Texto de prueba"  # Muestra es imcompatible con el tipo de dato ya definido anteriormente, pero no es un error, python lo permite y cambia el tipo de dato a str.
print(f"Variable: {variable}, del tipo: {type(variable)}")
1
otra_variable: str = 43  # Indica que el tipo de dato definido es str y genera alerta, pero permite asignarlo.
print(f"Variable: {otra_variable}, del tipo: {type(otra_variable)}")

user_id: int | None = None  # Para que permita vacíos

# Para el tipado de variables usamos:
# Variable: tipo = valor


def suma_clara(
    a: int, b: int
) -> int:  # parametros a y b enteros y el resultado es otro entero
    return a + b


# Lista que contiene diccionarios
articles: list[dict] = [
    {"title": "Example"},
    {"title2": "Example2"},
]

# Lista quye contiene listas y acepta cualquier tipo de dato.
articles2: list[list[Any]] = [["articulos", "otros", 1234], ["articulos2", "otros2"]]

# int, str, list, dict, tuple, Any
