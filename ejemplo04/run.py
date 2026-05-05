import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['nombre'][0] in ["A", "B", "L"]:
        lista_datos.append(d)

base_datos = "personas004"
puerto = "5985"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:{puerto}/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc
    )
    print(f"Insertando {doc['nombre']} | {response.status_code}")
# En el ejemplo 4 se envian uno por uno, gracias al for  doc in lista_datos, haciendo un post por cada documento. En cambio en el ejemplo 3 los datos se envian todos juntos, ya que usamos el _bulk_doc lo que crea un diccionario {'docs': lista_datos} y lo hace un solo post.
