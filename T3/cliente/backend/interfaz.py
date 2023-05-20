from PyQt5.QtCore import pyqtSignal, QObject, QTimer

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_juego import VentanaJuego


class Interfaz(QObject):
    senal_preparar_ventana_espera = pyqtSignal(list)
    senal_preparar_ventana_juego = pyqtSignal(list)
    senal_abrir_ventana_espera = pyqtSignal(str)
    senal_login_rechazado = pyqtSignal(str)
    senal_iniciar_partida = pyqtSignal()
    senal_actualizar_dado = pyqtSignal(int)
    senal_partida_rechazada = pyqtSignal(str)
    senal_servidor_caido = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.ventana_inicio = VentanaInicio()
        self.ventana_espera = VentanaEspera()
        self.ventana_juego = VentanaJuego()

        # --- SEÑALES ---

        # - VENTANA INICIO -
        self.ventana_inicio.senal_enviar_usuario.connect(parent.enviar)
        self.ventana_inicio.senal_abrir_ventana_espera.connect(parent.enviar)

        # - VENTANA ESPERA -
        self.ventana_espera.senal_iniciar_partida.connect(parent.enviar)

        # - VENTANA JUEGO -
        self.ventana_juego.senal_tirar_dado.connect(parent.enviar)

        # - INTERFAZ -
        self.senal_preparar_ventana_espera.connect(self.ventana_espera.preparar_ventana)
        self.senal_abrir_ventana_espera.connect(self.abrir_ventana_espera)
        self.senal_login_rechazado.connect(self.ventana_inicio.mostrar_error)
        self.senal_iniciar_partida.connect(self.abrir_ventana_juego)
        self.senal_preparar_ventana_juego.connect(self.ventana_juego.preparar_ventana)
        self.senal_actualizar_dado.connect(self.ventana_juego.actualizar_dado)
        self.senal_partida_rechazada.connect(self.ventana_espera.mostrar_error)
        self.senal_servidor_caido.connect(self.servidor_caido)

    def abrir_ventana_espera(self, nombre):
        self.ventana_inicio.hide()
        self.ventana_espera.mostrar_ventana(nombre)

    def abrir_ventana_juego(self):
        self.ventana_espera.hide()
        self.ventana_juego.mostrar_ventana()

    def servidor_caido(self):
        self.ventana_inicio.servidor_caido()
        self.ventana_espera.servidor_caido()
        self.ventana_juego.servidor_caido()
        self.timer_servidor_caido = QTimer()
        self.timer_servidor_caido.setInterval(3000)
        self.timer_servidor_caido.setSingleShot(True)
        self.timer_servidor_caido.timeout.connect(self.cerrar_ventanas)
        self.timer_servidor_caido.start()

    def cerrar_ventanas(self):
        self.ventana_inicio.hide()
        self.ventana_espera.hide()
        self.ventana_juego.hide()

    def manejar_mensaje(self, mensaje):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}

        if comando == "respuesta_validacion_usuario":
            if mensaje["estado"] == "aceptado":
                jugadores = mensaje["jugadores"].split(",")
                self.senal_preparar_ventana_espera.emit(jugadores)
            else:
                self.senal_login_rechazado.emit(mensaje["error"])

        elif comando == "abrir_ventana_espera":
            if mensaje["estado"] == "aceptado":
                nombre_usuario = mensaje["nombre_usuario"]
                self.senal_abrir_ventana_espera.emit(nombre_usuario)

        elif comando == "iniciar_partida":
            if mensaje["estado"] == "aceptado":
                self.senal_preparar_ventana_juego.emit(mensaje["jugadores"])
                self.senal_iniciar_partida.emit()
            elif mensaje["estado"] == "rechazado":
                self.senal_partida_rechazada.emit(mensaje["error"])

        elif comando == "actualizar_interfaz":
            jugadores = mensaje["jugadores"].split(",")
            self.senal_preparar_ventana_espera.emit(jugadores)

        elif comando == "numero_dado":
            self.senal_actualizar_dado.emit(mensaje["numero"])
        elif comando == "servidor_caido":
            self.senal_servidor_caido.emit()

    def mostrar_ventana_inicio(self):
        self.ventana_inicio.show()
