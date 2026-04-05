"""
Docstrings o documentación de funciones es una práctica recomendada en Python para describir el propósito, los argumentos, el valor de retorno y cualquier excepción que pueda generar una función. Esto ayuda a otros desarrolladores (o a ti mismo en el futuro) a entender rápidamente lo que hace la función sin tener que leer todo el código.
"""


def ejemplo_sin_docstring():
    return "Hola mundo"


def ejemplo_con_docstring():
    """
    DESCRIPTION
    ARGS
    RETURNS
    EXCEPTIONS
    EXAMPLES
    """
    return "Hola Mundo"


print(
    ejemplo_con_docstring.__doc__
)  # Accede al atributo que almacena la documentación de la función
help(
    ejemplo_con_docstring
)  # Muestra la documentación de la función, incluyendo su nombre, argumentos y docstring
