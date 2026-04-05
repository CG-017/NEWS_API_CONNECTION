import json
import urllib
import urllib.parse
import urllib.request
from typing import Callable

from .config import BASE_URL
from .exceptions import APIKeyError

# La validez de la API key es crucial para garantizar que las solicitudes a la API se realicen correctamente y que el sistema pueda manejar errores de autenticación de manera efectiva. La función validate_api_key verifica que la clave tenga un formato adecuado, lo que ayuda a prevenir errores antes de realizar solicitudes a la API. Si la clave no es válida, se puede lanzar una excepción específica (como APIKeyError) para informar al usuario o al sistema sobre el problema, permitiendo una gestión de errores más clara y específica en el código.


def validate_api_key(api_key: str) -> bool:
    """Valida que la API key tenga formato correcto.

    Args:
        api_key (str): La API key a validar.
    Returns:
        bool: True si la API key es válida, False en caso contrario.
    """
    return len(api_key) > 10 and api_key.isalnum()


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    """
    Cliente para la API de The Guardian.
    Args:
        api_key (str): La API key para autenticación.
        section (str): Sección de noticias a consultar.
        from_date (str): Fecha desde la cual obtener noticias (formato YYYY-MM-DD).
        timeout (int, optional): Tiempo máximo de espera para la respuesta. Por defecto es
        30 segundos.
        retries (int, optional): Número de reintentos en caso de fallo. Por defecto
        es 3.
    Raises:
        APIKeyError: Si la API key no es válida o hay un error en la conexión
    Returns:
        dict: Datos de la respuesta en formato JSON.
    """
    return f"Guardian {section} desde {from_date} con timeout {timeout} y retries {retries}"


def newsapi_client(api_key, query, timeout=30, retries=3):
    """
    Cliente para la API de NewsAPI.
    Args:
        api_key (str): La API key para autenticación.
        query (str): Término de búsqueda.
        timeout (int, optional): Tiempo máximo de espera para la respuesta. Por defecto es
        30 segundos.
        retries (int, optional): Número de reintentos en caso de fallo. Por defecto
        es 3.
    Raises:
        APIKeyError: Si la API key no es válida o hay un error en la conexión
    Returns:
        dict: Datos de la respuesta en formato JSON.
    """
    query_string = urllib.parse.urlencode(
        {"q": query, "apiKey": api_key}
    )  # Convierte el query y api a lenguaje de URL
    url = f"{BASE_URL}?{query_string}"  # Creamos el URL para consulta
    try:
        with urllib.request.urlopen(
            url, timeout=timeout
        ) as response:  # Hace la consulta con la URL y lo guarda en el response
            data = response.read().decode(
                "utf-8"
            )  # Decodifica los bytes y lo convierte en string,
            return json.loads(
                data
            )  # Lo convierte en listas o diccionarios para que sean fáciles de leer y trabajar en python

    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrió un error, no se pudo conectar con la API")
    return f"NewsAPI: {query} con timeout {timeout}"


def fetch_news(
    api_name, *args, **kwargs
):  # Buscador de noticias que escoge el API_client a consultar
    """
    Función flexible para conectar la API y sus parametros y llamar al cliente correspondiente.
    """

    if api_name not in ("newsapi", "guardian"):
        raise ValueError("API no soportada. Elige 'newsapi' o 'guardian'.")

    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {
        **base_config,
        **kwargs,
    }

    api_clients: dict[str, Callable] = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)
