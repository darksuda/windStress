import requests as rq
import re

# Hacer la solicitud GET
data = rq.get('https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices')

# Guardar el contenido en un archivo de texto
with open('tabla.txt', 'wb') as file:
    file.write(data.content)

# Leer el archivo de texto
with open('tabla.txt', 'r') as file:
    lines = file.readlines()

# Procesar cada línea para reemplazar espacios múltiples con comas
processed_lines = []
for line in lines:
    # Reemplazar espacios múltiples (o tabulaciones) con una coma
    processed_line = re.sub(r'\s+', ',', line.strip())
    processed_lines.append(processed_line)

# Guardar el resultado en un archivo CSV
with open('tabla.csv', 'w') as file:
    for line in processed_lines:
        file.write(line + '\n')

print("El archivo 'tabla.txt' ha sido convertido y guardado como 'tabla.csv'")
