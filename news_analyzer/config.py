"""Conffiguración de aplicación, como claves de API, URLs base, etc. Esta configuración se puede cargar desde variables de entorno o archivos de configuración para mantener la seguridad y flexibilidad del código."""

# Modulo nativo de python para interactuar con el sistema operativo, en este caso para acceder a las variables de entorno.
import os

# Modulo de terceros que permite cargar variables de entorno desde un archivo .env, facilitando la gestión de configuraciones sensibles como claves de API.
from dotenv import load_dotenv

# Instrucción que carga las variables de entorno desde un archivo .env ubicado en el mismo directorio que este script. Esto permite mantener las claves de API y otras configuraciones sensibles fuera del código fuente, mejorando la seguridad y facilitando la gestión de configuraciones en diferentes entornos (desarrollo, producción, etc.).
load_dotenv()

# Aquí usa el módulo os para buscar una variable específica llamada API_KEY. El método .get() es más seguro que un acceso directo porque, si la llave no existe, el programa no se rompe; simplemente devuelve None.
API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"
