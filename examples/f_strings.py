"""Ejemplos y explicación de f-strings en Python, una forma concisa y legible de formatear cadenas de texto utilizando expresiones dentro de llaves {}."""

from datetime import datetime

name = "Ana"
year = 2020
text = f"Hola {name}"
text_2 = "Hola"

text_calculo = f"Hola, {name}, tu edad es: {2025 - year} años"
print(text_calculo)

text_func = f"Hola {name.upper()}"
print(text_func)

edad = 10
text_if = f"Hola, {name} eres {'mayor' if edad >= 18 else 'menor'} de edad"
print(text_if)


bank_balance = 1234567890
texto = f"Tu saldo en la cuenta bancaria es {bank_balance:,}."
print(texto)
# Tu saldo en la cuenta bancaria es 1,234,567,890.

stock_price = 1.405
texto = f"El valor del stock es {stock_price:.1f}."
print(texto)
# El valor del stock es 1.4.

texto2 = f"El valor del stock es {stock_price:.2f}."
print(texto2)
# El valor del stock es 1.41.

user_id = 10000
text = f"Su id es: {user_id:04d}"
print(text)


product = "Laptop"
price = 1000

text = f"Producto: {product:<15} | Precio: {price:>10}"
print(f"{text}\n{text}")


date = datetime(2024, 12, 5, 10, 10)
text = f"La fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
print(text)
