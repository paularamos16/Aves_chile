import requests
import json

#esta función entrega todos los datos de la Api para ser manejados en un diccionario
def request_get(url):
    response = requests.get(url)
    datos = json.loads(requests.get(url).text) # transforma en dirección para iterar
    return datos