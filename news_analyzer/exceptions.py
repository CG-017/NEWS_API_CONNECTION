"""Definición de excepciones personalizadas para manejar errores específicos relacionados con la aplicación de análisis de noticias, como errores de clave de API, errores de conexión, etc. Esto permite una gestión de errores más clara y específica en el código."""


class NewsSystemError(Exception):
    """error general en la app"""

    pass


class APIKeyError(NewsSystemError):
    """Error relacionado con la clave de API, como clave faltante o inválida."""

    pass
