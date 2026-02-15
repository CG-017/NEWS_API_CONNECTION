"""
Docstring for docstrings
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

print(ejemplo_con_docstring.__doc__) #Accede al atributo que almacena la documentación de la función
help(ejemplo_con_docstring)