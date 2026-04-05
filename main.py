"""
Sistema de análisis de noticias con APIs múltiples.
"""

from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError

response_data = None
try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"{e}")


if response_data:
    print(response_data.keys())
    for article in response_data["articles"]:
        print(article["title"])

    print(len(response_data["articles"]))
