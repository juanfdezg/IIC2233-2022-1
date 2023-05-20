from threading import Lock
from os.path import join
from random import randint
from utils import data_json


class Logica:
    lock1 = Lock()

    def __init__(self, parent):
        self.parent = parent
        self.partida_iniciada = False

        self.clientes_nombres = {}
        self.cliente_sockets = {}

    def validar_usuario(self, nombre, socket_cliente):
        self.valido = False
        largo = False
        alfanum = False
        if 1 <= len(nombre) <= 10:
            largo = True
        if nombre.isalnum():
            alfanum = True
        if (
            nombre not in self.clientes_nombres.values()
            and len(self.clientes_nombres) < data_json("MAXIMO_JUGADORES")
            and largo
            and alfanum
            and not self.partida_iniciada
        ):
            self.parent.id_cliente += 1
            self.clientes_nombres[self.parent.id_cliente - 1] = nombre
            self.cliente_sockets[nombre] = socket_cliente
            self.valido = True
            self.log(
                f"Ha ingresado exitosamente el jugador con el nombre válido: {nombre}"
            )
            print("")

            return {
                "comando": "respuesta_validacion_usuario",
                "estado": "aceptado",
                "nombre_usuario": nombre,
                "jugadores": ",".join(self.clientes_nombres.values()),
                "receptor": "grupal",
            }
        elif not largo:
            error = "largo_invalido"
            self.log(
                "Jugador ingresa nombre inválido, no cumple con el largo adecuado."
            )
            print("")
        elif not alfanum:
            error = "no_alfanumerico"
            self.log("Jugador ingresa nombre no alfanumérico.")
            print("")

        elif nombre in self.clientes_nombres.values():
            error = "usuario_ya_existente"
            self.log(f"El jugador ingresa nombre ya existente: {nombre} ")
            print("")
        elif self.partida_iniciada:
            error = "partida_iniciada"
            self.log("Jugador intenta entrar a partida en proceso, no es posible.")
            print("")
        elif len(self.clientes_nombres) == data_json("MAXIMO_JUGADORES"):
            error = "maximo_de_jugadores"
            self.log(
                f"Jugador con nombre válido no puede ingresar, sala de espera llena. "
            )
            print("")

        return {
            "comando": "respuesta_validacion_usuario",
            "estado": "rechazado",
            "error": error,
            "receptor": "individual",
        }

    def abrir_ventana_espera(self, nombre):
        if self.valido:
            return {
                "comando": "abrir_ventana_espera",
                "estado": "aceptado",
                "nombre_usuario": nombre,
                "receptor": "individual",
            }
        else:
            return {
                "comando": "abrir_ventana_espera",
                "estado": "rechazado",
                "receptor": "individual",
            }

    def iniciar_partida(self, jugadores, usuario_actual):
        if usuario_actual == jugadores[0] and (
            data_json("MINIMO_JUGADORES")
            <= len(jugadores)
            < (data_json("MAXIMO_JUGADORES") + 1)
        ):
            print((data_json("MAXIMO_JUGADORES") + 1))
            self.log(
                f'Se ha iniciado la partida con los siguientes jugadores: \
#{",".join(jugadores)}'
            )
            print("")
            self.partida_iniciada = True
            return {
                "comando": "iniciar_partida",
                "estado": "aceptado",
                "jugadores": jugadores,
                "receptor": "grupal",
            }

        elif usuario_actual != jugadores[0]:
            error = "no_admin"
        elif len(jugadores) < 2:
            error = "minimo_jugadores"
        return {
            "comando": "iniciar_partida",
            "estado": "rechazado",
            "error": error,
            "receptor": "individual",
        }

    def procesar_mensaje(self, mensaje, socket_cliente):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "validar_usuario":
            respuesta = self.validar_usuario(mensaje["nombre_usuario"], socket_cliente)

        elif comando == "abrir_ventana_espera":
            respuesta = self.abrir_ventana_espera(mensaje["nombre_usuario"])

        elif comando == "iniciar_partida":
            respuesta = self.iniciar_partida(
                mensaje["jugadores"], mensaje["usuario_actual"]
            )

        elif comando == "desconectar":
            self.eliminar_nombre(mensaje["id"])
            return None

        elif comando == "actualizar_interfaz":
            self.parent.enviar_mensaje_todos(
                {
                    "comando": "actualizar_interfaz",
                    "jugadores": ",".join(self.clientes_nombres.values()),
                    "receptor": "grupal",
                }
            )
            return None

        elif comando == "tirar_dado":
            respuesta = self.tirar_dado()
        return respuesta

    def tirar_dado(self):
        return {"comando": "numero_dado", "numero": randint(1, 3), "receptor": "grupal"}

    def eliminar_nombre(self, id):
        nombre = self.clientes_nombres.pop(id, None)
        self.cliente_sockets.pop(nombre, None)

    def log(self, mensaje: str):
        print("|" + mensaje.center(80, " ") + "|")
