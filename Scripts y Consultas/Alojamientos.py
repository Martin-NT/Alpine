from pymongo import MongoClient, ReturnDocument
from datetime import datetime, timedelta
import random
from variables import paises_ciudades, paises_direcciones

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Alpine']  





try:
   
    # Poblar colección Alojamiento (10 documentos)
    alojamiento_bulk = []
    for i in range(1000000):
        pais = random.choice(list(paises_ciudades.keys()))
        ciudad = random.choice(paises_ciudades[pais])
        direccion = random.choice(paises_direcciones[pais])
        alojamiento_bulk.append({
            "_id": i + 1,
            "pais": pais,
            "ciudad":ciudad,
            "direccion": direccion,
            "duracion_dias": random.randint(1, 30),
            "estacionamiento": random.choice([True, False]),
            "precio_dolares": random.randint(33, 527),
            "telefono": f"{random.randint(1000000000, 9999999999)}",
            "descripcion": f"Descripción detallada del alojamiento {direccion}...",
            "usuarios_reservados": [random.randint(1,500000) for _ in range(random.randint(1,10))]
        })

        if len(alojamiento_bulk) == 1000000:
            db.Alojamientos.insert_many(alojamiento_bulk)
            alojamiento_bulk = []
    
    if alojamiento_bulk:
        db.Alojamientos.insert_many(alojamiento_bulk)


except Exception as e:
    print(f"Error durante la inserción: {e}")