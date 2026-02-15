"""Typing con Python"""

variable = 42 #python automatica mente lo caracteriza como int

print(type(variable))

variable = "Texto de prueba"
print(variable)
print(type(variable))

otra_variable: str = 43
print(f"Variable: {otra_variable}, del tipo: {type(otra_variable)}")

user_id: int | None = None #Para que permita vacíos

#Para el tipado de variables usamos :
#Variable: tipo = valor

def suma_clara(a: int, b: int) -> int:
    return a+b

articles: list[dict] = [
    {"title": "Example"},
    {"title2": "Example2"},
    ]

from typing import Any  #proyectos que inician y no se sabe el tipo de dato (no abusar)

articles2: list[list[Any]] = [
    ["articulos", "otros", 1234],
    ["articulos2", "otros2"]
    ]

# int, str, list, dict, tuple, Any