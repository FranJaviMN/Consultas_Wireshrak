# Importamos las librerias que vamos a necesitar, como se especifica en el README, es necesario tener la libreria scapy instalada.

from scapy.all import PcapNgReader
from scapy.layers.inet import IP, TCP, UDP

# Agregamos la función del programa llamada leer_pcapng a la lista de funciones disponibles, 
# que toma como parametros de entrada el archivo .pcapng, el protocolo a filtrar, el puerto destino y la IP destino.

def leer_pcapng(archivo, protocolo, ip_destino=None, puerto_destino=None):
    try:
        with PcapNgReader(archivo) as pcap_reader:
            for pkt in pcap_reader:
                # Filtrar paquetes por el protocolo proporcionado
                if protocolo == 'IP' and IP in pkt:
                    if ip_destino is None or pkt[IP].dst == ip_destino:
                        # Imprimir el paquete si coincide con el protocolo y la dirección IP de destino (si se proporciona)
                        print(pkt)
    # Manejar el caso en el que el archivo no se encuentre
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
    # Manejar cualquier otra excepción que ocurra durante la lectura del archivo
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo '{archivo}': {e}")



# Reemplaza 'archivo.pcapng' con la ruta y nombre de tu archivo .pcapng
nombre_archivo = r"C:\Users\franciscojavier.mart\Documents\Scripts\Consultas_Wireshrak-1\fichero_prueba.pcapng"
protocolo_filtrar = 'IP'  # Puedes cambiar esto a 'IP' o 'UDP' según lo necesites
ip_destino_filtrar = None  # Reemplaza con la IP de destino deseada (o déjalo como None)
puerto_destino_filtrar = None # Reemplaza con el puerto de destino deseado (o déjalo como None)

# Llamar a la función para leer el archivo .pcapng y aplicar los filtros especificados
leer_pcapng(nombre_archivo, protocolo_filtrar, ip_destino_filtrar, puerto_destino_filtrar)