# Leer archivo .pcapng con Python

Este es un script en Python que te permite leer un archivo con extensión .pcapng y filtrar los paquetes según el protocolo, la dirección IP de destino y el puerto de destino que especifiques.

## Requisitos

- Python 3.x
- Scapy (puedes instalarlo con `pip install scapy`)

## Uso

```python
from leer_pcapng import leer_pcapng

# Reemplaza 'archivo.pcapng' con la ruta y nombre de tu archivo .pcapng
nombre_archivo = 'archivo.pcapng'
protocolo_filtrar = 'TCP'  # Puedes cambiar esto a 'IP' o 'UDP' según lo necesites
ip_destino_filtrar = '192.168.0.1'  # Reemplaza con la IP de destino deseada (o déjalo como None)
puerto_destino_filtrar = 80  # Reemplaza con el puerto de destino deseado (o déjalo como None)