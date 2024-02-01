# Keylogger
Keylogger básico en Python.
Es un script python que usa el módulo pynput para registrar las teclas pulsadas por un usuario, filtrando con una lista lo que quiero registrar, en este caso cualquier cosa que no sea una hotkey, en un archivo de texto que se envía a través de un socket al atacante.
Por otro lado, inicio una conexión socket entre el cliente y el servidor (atacante) para enviar cada dos minutos el contenido del archivo
