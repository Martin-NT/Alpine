from pymongo import MongoClient, ReturnDocument
from datetime import datetime, timedelta
import random
from variables import paises_ciudades, nombres, apellidos, aerolineas, caracteristicas

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Alpine']  


pais = random.choice(list(paises_ciudades.keys()))
ciudad = random.choice(paises_ciudades[pais])



try:
    home_bulk = []
    categorias = ["Mas Visitados", "Mejores Atracciones", "Mejores Alojamientos", "Ofertas"]
    for i in range(4):
        home_bulk.append({
            "nombre": categorias[i],
            "imagen": [f" /home/usser/assets/img{i}-{j}.png" for j in range(15)]  # Añadimos 15 imágenes por documento
        })

        if len(home_bulk) == 4:
            db.Home.insert_many(home_bulk)
            home_bulk = []

    if home_bulk:
        db.Home.insert_many(home_bulk)

    print("Colección Home poblada con 5 documentos.")

except Exception as e:
    print(f"Error durante la inserción: {e}")