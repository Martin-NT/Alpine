from pymongo import MongoClient, ReturnDocument
from datetime import datetime, timedelta
import random
from variables import paises_ciudades, nombres, apellidos, aerolineas, caracteristicas, paises_atracciones, paises_direcciones

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Alpine']  



try:
    atracciones_bulk = []
    for i in range(1500000):
        pais = random.choice(list(paises_ciudades.keys()))
        ciudad = random.choice(paises_ciudades[pais])
        atraccion = random.choice(paises_atracciones[pais])
        direccion = random.choice(paises_direcciones[pais])
        atracciones_bulk.append({
            "_id": i+1,
            "nombre_de_atraccion": atraccion,
            "pais": pais,
            "ciudad": ciudad,
            "direccion": direccion,
            "costo": random.randint(8, 112),
            "horario": f"{random.randint(9, 17)}:00 - {random.randint(18, 22)}:00",
            "duracion_horas": random.randint(1, 5),
            "edad_minima": random.randint(8, 90),
            "edad_maxima": random.randint(8, 90),
            "caracteristicas": random.sample(caracteristicas, random.randint(1, len(caracteristicas))),
            "descripcion": f"Descripción detallada de la atracción {atraccion}...",
            "usuarios_reservados": [random.randint(1,500000) for _ in range(random.randint(1,10))]
        })

        if len(atracciones_bulk) == 1500000:
            db.Atracciones.insert_many(atracciones_bulk)
            atracciones_bulk = []

    if atracciones_bulk:
        db.Atracciones.insert_many(atracciones_bulk)

    print("Colección Atracciones poblada")

except Exception as e:
    print(f"Error durante la inserción: {e}")