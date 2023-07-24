# Importamos las librerias que vamos a necesitar, como se especifica en el README, es necesario tener la libreria scapy instalada.

from scapy.all import PcapNgReader
from scapy.layers.inet import IP, TCP, UDP

# Reemplaza 'archivo.pcapng' con la ruta y nombre de tu archivo .pcapng
nombre_archivo = r"C:\Users\franciscojavier.mart\Documents\Scrips\Leer_wireshark\fichero_prueba.pcapng"
protocolo_filtrar = 'TCP'  # Puedes cambiar esto a 'IP' o 'UDP' según lo necesites
ip_destino_filtrar = None  # Reemplaza con la IP de destino deseada (o déjalo como None)
puerto_destino_filtrar = None # Reemplaza con el puerto de destino deseado (o déjalo como None)