"""Ejemplo de manejo de excepciones en Python utilizando try, except y finally. Este código solicita al usuario que ingrese dos números y realiza una división, manejando posibles errores como la división por cero o la entrada de datos no numéricos."""


# 1 Definimos una excepción personalizada para el caso de división por 2
class NoDividirPorDosError(Exception):
    """Excepción lanzada cuando el divisor es 2."""

    pass


try:
    a = int(input("Digita un numero: "))
    b = int(input("Digita otro numero: "))

    # Usamos 'raise' para forzar que ocurra nuestra excepción personalizada
    if b == 2:
        raise NoDividirPorDosError("No está permitido la división por 2")
    resultado = a / b
    print(f"Resultado: {resultado}")

except ValueError:
    print("Lo que digitaste no es un numero")

except ZeroDivisionError:
    print("No está permitido dividir por 0")

except NoDividirPorDosError as e:
    print(e)

finally:
    print("Ha finalizado la operación")

print("Ha finalizado la operación 2")

# Hay una gran cantidad de exceptions disponibles que podemos consultar en la documentación de python
