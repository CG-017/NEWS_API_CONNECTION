"""Ejemplo de uso de la función enumerate() para numerar los artículos de una lista. Se muestra cómo usar un contador manual y luego cómo usar enumerate() para obtener el mismo resultado de forma más sencilla."""

import sample_data

counter = 1
for article in sample_data.sample_articles:
    print(f"{counter}: {article['title']}")
    counter += 1

# Otra forma de numerar los artículos usando enumerate
sample_articles_enum = enumerate(
    sample_data.sample_articles, start=10
)  # start=10 para comenzar la numeración desde 10
for counter, article in sample_articles_enum:
    print(f"{counter}: {article['title']}")
