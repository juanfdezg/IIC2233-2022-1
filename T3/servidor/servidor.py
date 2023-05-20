import socket
import threading
import json
from logica import Logica
from funciones import traspasar_chunks, encriptar_mensaje, desencriptar_mensaje


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.conectado = False
        self.logica = Logica(self)
        self.id_cliente = 0
        self.numero_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.iniciar_servidor()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.conectado = True
        self.log(
            f"El host corresponde a: {self.host} y se está escuchando desde el puerto \
{self.port}"
        )
        self.comenzar_a_aceptar()

    def comenzar_a_aceptar(self):
        thread = threading.Thread(target=self.aceptar_clientes)
        thread.start()

    def aceptar_clientes(self):
        while self.conectado:
            try:
                socket_cliente, adress = self.socket_servidor.accept()
                self.log(f"Jugador con dirección {adress} se ha conectado al servidor")
                thread_cliente = threading.Thread(
                    target=self.escuchar_cliente,
                    args=(
                        self.numero_cliente,
                        socket_cliente,
                    ),
                    daemon=True,
                )
                thread_cliente.start()
                # self.id_cliente += 1
                self.numero_cliente += 1

            except ConnectionError as error:
                self.log("La conexión ha fallado")
                thread_cliente.close()

    def escuchar_cliente(self, id_cliente, socket_cliente):
        self.log(f"Comenzando a escuchar a jugador {id_cliente}")
        print("")
        try:
            while True:
                mensaje_recibido = self.recibir_mensaje(socket_cliente)
                if mensaje_recibido == "":
                    self.log("Error de conexión, mensaje vacío")
                    self.eliminar_cliente(self.id_cliente, socket_cliente)
                else:
                    self.log(f"Mensaje recibido: {mensaje_recibido}")
                    print("")
                    mensaje_procesado = self.logica.procesar_mensaje(
                        mensaje_recibido, socket_cliente
                    )

                    if mensaje_procesado != {}:
                        if mensaje_procesado["receptor"] == "grupal":
                            self.enviar_mensaje_todos(mensaje_procesado)
                        elif mensaje_procesado["receptor"] == "individual":
                            self.enviar_mensaje(mensaje_procesado, socket_cliente)
                    else:
                        self.log("Error de conexión")
                        self.eliminar_cliente(self.id_cliente, socket_cliente)

        except ConnectionResetError:
            self.log("Error de conexión con el cliente")
            self.eliminar_cliente(id_cliente, socket_cliente)

    def recibir_mensaje(self, socket_cliente):
        cantidad_bloques_bytes = socket_cliente.recv(4)
        cantidad_bloques = int.from_bytes(cantidad_bloques_bytes, byteorder="little")
        bytes_mensaje = bytearray()
        for i in range(cantidad_bloques):
            resto = socket_cliente.recv(6)
            bytes_mensaje += socket_cliente.recv(20)
        mensaje_desencriptado = desencriptar_mensaje(bytes_mensaje)
        mensaje = self.decodificar_mensaje(mensaje_desencriptado)
        return mensaje

    def enviar_mensaje(self, mensaje, socket_cliente):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        mensaje_encriptado = encriptar_mensaje(bytes_mensaje)
        mensaje_final = traspasar_chunks(mensaje_encriptado)

        socket_cliente.sendall(mensaje_final)
        self.log(f"Enviando respuesta: {mensaje_final}")
        print("")

    def enviar_mensaje_todos(self, mensaje):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        mensaje_encriptado = encriptar_mensaje(bytes_mensaje)
        mensaje_final = traspasar_chunks(mensaje_encriptado)

        for cliente in self.logica.cliente_sockets.values():
            cliente.sendall(mensaje_final)
        self.log(f"Enviando respuesta: {mensaje_final}")
        print("")

    def eliminar_cliente(self, id_cliente, socket_cliente):
        try:
            self.log(f"Borrando el socket del cliente {id_cliente}.")
            self.logica.procesar_mensaje(
                {"comando": "desconectar", "id": id_cliente}, socket_cliente
            )
            self.logica.procesar_mensaje(
                {"comando": "actualizar_interfaz"}, socket_cliente
            )
            socket_cliente.close()
        except KeyError as e:
            self.log(f"Error: {e}")

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

    def log(self, mensaje: str):
        print("|" + mensaje.center(80, " ") + "|")
