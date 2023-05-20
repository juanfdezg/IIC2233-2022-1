import socket
import json
import threading
from backend.interfaz import Interfaz
from backend.funciones import traspasar_chunks, encriptar_mensaje, desencriptar_mensaje


class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Interfaz(self)
        self.iniciar_cliente()

    def iniciar_cliente(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
            self.interfaz.mostrar_ventana_inicio()
        except ConnectionError:
            self.log(f"Error de conexión")
            self.socket_cliente.close()
        pass

    def comenzar_a_escuchar(self):
        thread_escuchar = threading.Thread(target=self.escuchar_servidor, daemon=True)
        thread_escuchar.start()
        pass

    def escuchar_servidor(self):
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje != "":
                    self.log(f"Mensaje recibido: {mensaje}")
                    print("")
                    self.interfaz.manejar_mensaje(mensaje)
                else:
                    self.log("Error de conexión")
        except ConnectionResetError:
            self.log("Error de conexión")
            self.socket_cliente.close()
            self.servidor_caido()

    def recibir(self):
        cantidad_bloques_bytes = self.socket_cliente.recv(4)
        cantidad_bloques = int.from_bytes(cantidad_bloques_bytes, byteorder="little")
        bytes_mensaje = bytearray()
        for i in range(cantidad_bloques):
            resto = self.socket_cliente.recv(6)
            bytes_mensaje += self.socket_cliente.recv(20)
        mensaje_desencriptado = desencriptar_mensaje(bytes_mensaje)
        mensaje = self.decodificar_mensaje(mensaje_desencriptado)
        return mensaje

    def enviar(self, mensaje):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        mensaje_encriptado = encriptar_mensaje(bytes_mensaje)
        mensaje_final = traspasar_chunks(mensaje_encriptado)

        self.socket_cliente.sendall(mensaje_final)
        self.log(f"Enviando mensaje: {mensaje_final}")
        print("")

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            bytes_mensaje = mensaje_json.encode("utf-8")
            return bytes_mensaje
        except json.JSONDecodeError:
            print("No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return ""

    def servidor_caido(self):
        mensaje = {"comando": "servidor_caido"}
        self.interfaz.manejar_mensaje(mensaje)

    def log(self, mensaje: str):
        print("|" + mensaje.center(80, " ") + "|")
