# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings


# PEP 8: Utilidades comunes del proyecto - funciones en snake_case
def clean_text(text):
    # PEP 8: 4 espacios por indentación, no tabs
    """Limpia y normaliza texto."""  # PEP 8: Docstrings en comillas dobles triples
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble líneas en blanco entre funciones para separar lógicamente
def validate_api_key(api_key):
    """Valida que la API key tenga formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas después de utilidades
def fetch_news_from_api(api_name, query):
    """Obtiene noticias de una API específica."""
    pass


def process_article_data(raw_data):
    """Procesa datos crudos de artículo."""
    pass


# Longitud de línea: Máximo 88 caracteres (Ruff default)
# Indentación: 4 espacios, nunca tabs
# Nombres descriptivos: snake_case para funciones y variables
# Imports ordenados: estándar → terceros → locales
# Líneas en blanco: Separar funciones y clases lógicamente

def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"

import json
import urllib.parse
import urllib.request


class NewsSystemError(Exception):
    """Error General en la app"""

    pass

class APIKeyError(NewsSystemError):
    """Error cuando la API Key es invalida"""

    pass


BASE_URL = "https://newsapi.org/v2/everything"


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key}) #Convierte el query y api a lenguaje de URL
    url = f"{BASE_URL}?{query_string}" #Creamos el URL para consulta
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:  #Hace la consulta con la URL y lo guarda en el response
            data =response.read().decode("utf-8") #Decodifica los bytes y lo convierte en string,
            return json.loads(data) #Lo convierte en listas o diccionarios para que sean fáciles de leer y trabajar en python
        
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrió un error, no se pudo conectar con la API")
    return f"NewsAPI: {query} con timeout {timeout}" 


def fetch_news(api_name, *args, **kwargs): #Buscador de noticias que escoge el API_client a consultar 
    """
    Función flexible para conectar la API
    """
    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {
        **base_config,
        **kwargs,
    }

    api_clients = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)

response_data = None
try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"{e}")
    print(response_data)


if response_data:
    print(response_data.keys())
    for article in response_data["articles"]:
        print(article["title"])

    print(len(response_data["articles"]))

