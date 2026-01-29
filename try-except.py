class DivisionError(Exception):
    """Error en operación"""
    pass

a = 0
b = 0

try:
    a = int(input("Digita un numero: "))
    b = int(input("Digita otro numero: "))
    if b==2:
        raise DivisionError("No está permitido la división por 2") #raise==lanzar: Palabra clave para generar una excepción, forzar que ocurra.
    resultado = a/ b
    print(f"Resultado: {resultado}")
except ValueError:
    print("Lo que digitaste no es un numero")
except ZeroDivisionError:
    print("No está permitido dividir por 0")
finally:
    print("Print desde finally")

print("este es otro print")

#Hay una gran cantidad de exceptions disponibles que podemos consultar en la documentación de python