import json
import pandas as pd
from argovisHelpers import helpers as avh

API_KEY = '7f8d3cf6ecbf39891eca1273dda99216809e8fa0'  # Crear cuenta en ARGOVIS
API_PREFIX = 'https://argovis-api.colorado.edu/'   # URL base de la API de Argovis

# Definir el área del Perú como una lista de listas de coordenadas
#polygon = [[-180, -20], [-80, -20], [-80, 20], [-180, 20], [-180, -20]]
#polygon = [[180, -20], [160, -20], [160, 20], [180, 20], [180, -20]]
polygon = [[-90, -20], [-75, -20], [-75, -8], [-90, -8], [-90, -20]]

# Configuración de los parámetros para la consulta
params = {
    'startDate': '2019-09-01T00:00:00Z',
    'endDate': '2019-12-31T00:00:00Z',
    'source': 'argo_core',  # Opciones: argo_core, argo_deep, argo_bgc
    'polygon': polygon,
    'data': 'all'
}

# Realizar la consulta a la API de Argovis
d = avh.query('argo', options=params, apikey=API_KEY, apiroot=API_PREFIX)

# Guardar los datos en un archivo JSON
with open('data_pota_2.json', 'w') as data:
    data.write(json.dumps(d))
