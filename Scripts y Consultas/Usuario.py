from pymongo import MongoClient, ReturnDocument
from datetime import datetime, timedelta
import random
from variables import paises_ciudades, nombres, apellidos, aerolineas, caracteristicas

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Alpine']  


paises = list(paises_ciudades.keys())


try:
    usuarios_bulk = []
    for i in range(500000):
        pais = random.choice(paises)
        ciudad = random.choice(paises_ciudades[pais])
        usuarios_bulk.append({
            "_id": i+1,
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "DNI": random.randint(1000000, 9999999),
            "correo electronico": f"usuario{i}@example.com",
            "contraseña": f"{random.choice(['TPL60XZY9YW', 'ABC123XYZ', 'MYPASSWORD'])}",
            "pais": pais,
            "ciudad": ciudad,
            "nacimiento": datetime(random.randint(1950, 2010), random.randint(1, 12), random.randint(1, 28)),
            "alojamientos_reservados": [random.randint(1,1000000) for _ in range(random.randint(0,10))],
            "atraciones_reservadas": [random.randint(1,1500000) for _ in range(random.randint(0,10))],
            "vuelos_reservados": [random.randint(1,500000) for _ in range(random.randint(0,10))]
        })

        if len(usuarios_bulk) == 500000:
            db.Usuario.insert_many(usuarios_bulk)
            usuarios_bulk = []

            # Mensaje de progreso cada 100,000 usuarios insertados
            if i % 100000 == 0:
                print(f"{i} usuarios insertados...")

    if usuarios_bulk:
        db.Usuario.insert_many(usuarios_bulk)

    print("Colección Usuario poblada con 1,000,000 documentos.")

except Exception as e:
    print(f"Error durante la inserción: {e}")