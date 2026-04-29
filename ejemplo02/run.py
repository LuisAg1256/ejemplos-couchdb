import requests
import json
from config import url_base

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

base_datos = "demo2"
# Configurar el acceso a la base de datos
url = f"{url_base}/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos
response = requests.post(url, headers=headers, json=data)

# Mostrar respuesta
print(response.status_code)
print(response.json())
