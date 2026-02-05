"""Typing con Python"""

variable = 42 #python automatica mente lo caracteriza como int

print(type(variable))

variable = "Texto de prueba"
print(variable)
print(type(variable))

otra_variable: str = 43
print(f"Variable: {otra_variable}, del tipo: {type(otra_variable)}")

user_id: int | None = None

#Para el tipado de variables usamos :
#Variable: tipo = valor