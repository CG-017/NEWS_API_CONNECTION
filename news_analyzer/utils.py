def clean_text(text):
    """Limpia y normaliza texto removiendo espacios y convirtiendo a minúsculas.

    Esta función toma una cadena de texto y realiza operaciones de limpieza
    básicas para normalizar el contenido. Elimina espacios en blanco al inicio
    y final, y convierte todo el texto a minúsculas para facilitar comparaciones
    y procesamiento posterior.

    Args:
        text (str): La cadena de texto que se desea limpiar y normalizar.
                   Puede contener espacios, caracteres especiales y mayúsculas.

    Returns:
        str: El texto limpio y normalizado. Si el texto de entrada está vacío
             o es None, retorna una cadena vacía.

    Raises:
        TypeError: Si el parámetro text no es de tipo str.

    Examples:
        >>> clean_text("  HOLA MUNDO  ")
        'hola mundo'

        >>> clean_text("Python Programming")
        'python programming'

        >>> clean_text("")
        ''

        >>> clean_text("   ")
        ''

        >>> clean_text("MiXeD cAsE tExT   ")
        'mixed case text'
    """
    if not text:
        return ""
    return text.strip().lower()


# Basicamente le podemos dar formato a los datos que nos devuelve la API para que sean más fáciles de manejar en el resto del código, como por ejemplo convertir fechas a un formato específico, extraer solo la información relevante, o normalizar textos.


def process_article_data(raw_data: dict) -> dict:
    """Procesa datos crudos de artículo."""
    pass


# Retorna una lista de fuentes únicas a partir de una lista de artículos, utilizando comprensión de conjuntos para extraer los nombres de las fuentes de manera eficiente y evitando duplicados.
def get_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    return list(
        filter(
            lambda article: article["source"]["name"].lower() == source.lower(),
            articles,
        )
    )


def get_reading_time(article: dict) -> dict:
    """Calcula el tiempo de lectura"""
    minutes = len(article["content"]) // 200 + 1
    article["reading_time"] = minutes
    return article
