from pymongo import MongoClient, ReturnDocument
from datetime import datetime, timedelta
import random
from variables import paises_ciudades, nombres, apellidos, aerolineas, caracteristicas, paises_aeropuertos

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Alpine']  


paises = list(paises_ciudades.keys())

try:
    vuelos_bulk = []
    for i in range(500000):
        pais = random.choice(paises)
        ciudad = random.choice(paises_ciudades[pais])
        aeropuerto = random.choice(paises_aeropuertos[pais])
        origen = random.choice(paises)
        destino = random.choice(paises)
        while origen == destino:
            destino = random.choice(pais)
        fecha_salida = datetime.now() + timedelta(days=random.randint(1, 365))
        fecha_llegada = fecha_salida + timedelta(hours=random.randint(1, 24))
        vuelos_bulk.append({
            "_id": i+1,
            "aeropuerto": aeropuerto,
            "pais": pais,
            "ciudad": ciudad,
            "origen": origen,
            "destino": destino,
            "fecha_salida": fecha_salida.strftime("%Y-%m-%d"),
            "fecha_llegada": fecha_llegada.strftime("%Y-%m-%d"),
            "hora_salida": fecha_salida.strftime("%H:%M"),
            "hora_llegada": fecha_llegada.strftime("%H:%M"),
            "aerolinea": random.choice(aerolineas),
            "precio_dolares": random.randint(20, 1293),
            "asientos_disponibles": random.randint(0, 213),
            "pasajeros": [random.randint(1,500000) for _ in range(random.randint(1,10))]
        })

        if len(vuelos_bulk) == 500000:
            db.Vuelos.insert_many(vuelos_bulk)
            vuelos_bulk = []

    if vuelos_bulk:
        db.Vuelos.insert_many(vuelos_bulk)
except Exception as e:
    print(f"Error durante la inserción: {e}")