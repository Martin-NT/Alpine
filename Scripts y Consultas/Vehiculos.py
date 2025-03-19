from pymongo import MongoClient, ReturnDocument
from datetime import datetime, timedelta
import random
from variables import paises_ciudades, nombres, apellidos, aerolineas, caracteristicas

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Alpine']  


paises = list(paises_ciudades.keys())


try:
    vehiculos_bulk = []
    for i in range(500000):
        pais = random.choice(paises)
        ciudad = random.choice(paises_ciudades[pais])
        vehiculos_bulk.append({
            "_id": i+1,
            "pais": pais,
            "ciudad": ciudad,
            "marca": f"Marca {random.choice(['Toyota', 'Ford', 'Honda', 'Tesla', 'BMW'])}",
            "modelo": f"Modelo {random.choice(['X', 'Y', 'Z', 'GT', 'S'])}",
            "capacidad": random.randint(2, 9),
            "precio_dia_dolares": random.randint(30, 500),
            "usuarios_reservados": random.randint(1,500000) 
        })

        if len(vehiculos_bulk) == 500000:
            db.Vehiculos.insert_many(vehiculos_bulk)
            vehiculos_bulk = []

    if vehiculos_bulk:
        db.Vehiculos.insert_many(vehiculos_bulk)

    print("Colección Vehiculos poblada con 10,000 documentos.")

except Exception as e:
    print(f"Error durante la inserción: {e}")