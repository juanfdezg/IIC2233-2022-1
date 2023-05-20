import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from os.path import join
from utils import data_json
from PyQt5.QtMultimedia import QSound

window_name, base_class = uic.loadUiType(join(*data_json("RUTA_PANTALLA_JUEGO")))


class VentanaJuego(window_name, base_class):
    senal_tirar_dado = pyqtSignal(dict)
    senal_mover_ficha = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.turno = 0
        self.boton_dado.clicked.connect(self.tirar_dado)
        self.ocultar_elementos()

    def ocultar_elementos(self):
        self.label_error.hide()
        self.ficha_azul1.hide()
        self.ficha_azul2.hide()
        self.ficha_rojo1.hide()
        self.ficha_rojo2.hide()
        self.ficha_verde1.hide()
        self.ficha_verde2.hide()
        self.ficha_amarillo1.hide()
        self.ficha_amarillo2.hide()
        # ocultar el resto

    def tirar_dado(self):
        diccionario = {"comando": "tirar_dado"}
        self.senal_tirar_dado.emit(diccionario)
        self.senal_mover_ficha.emit()

    def actualizar_dado(self, numero):
        self.contador_numero.setText(f"Número obtenido: {numero}")
        self.turno += 1
        if self.turno == len(self.jugadores):
            self.turno = 0
        self.label_jugador_turno.setText(
            f" Jugador de turno: {self.jugadores[self.turno]}"
        )

    def preparar_ventana(self, jugadores):
        self.jugadores = jugadores
        if len(self.jugadores) == 2:
            self.label_jugador1.setText(f"{self.jugadores[0]}")
            self.label_jugador2.setText(self.jugadores[1])
            self.eliminar_jugadores(2)
        elif len(self.jugadores) == 3:
            self.label_jugador1.setText(f"{self.jugadores[0]}")
            self.label_jugador2.setText(self.jugadores[1])
            self.label_jugador3.setText(self.jugadores[2])
            self.eliminar_jugadores(3)
        elif len(self.jugadores) == 4:
            self.label_jugador1.setText(f"{self.jugadores[0]}")
            self.label_jugador2.setText(self.jugadores[1])
            self.label_jugador3.setText(self.jugadores[2])
            self.label_jugador4.setText(self.jugadores[3])

    def eliminar_jugadores(self, cantidad):
        if cantidad == 2:
            self.label_jugador3.setText("")
            self.ficha_amarillo3.hide()
            self.contador_turno3.hide()
            self.label_fichas_base3.hide()
            self.label_fichas_color3.hide()
            self.label_fichas_victoria3.hide()
            self.fichas_dobles_amarillo.hide()

            self.label_jugador4.setText("")
            self.ficha_rojo3.hide()
            self.contador_turno4.hide()
            self.label_fichas_base4.hide()
            self.label_fichas_color4.hide()
            self.label_fichas_victoria4.hide()
            self.fichas_dobles_rojo.hide()
        if cantidad == 3:
            self.label_jugador4.setText("")
            self.ficha_rojo3.hide()
            self.contador_turno4.hide()
            self.label_fichas_base4.hide()
            self.label_fichas_color4.hide()
            self.label_fichas_victoria4.hide()
            self.fichas_dobles_rojo.hide()

    def servidor_caido(self):
        self.label_error.show()

    def abrir_ventana_juego(self):
        self.hide()

    def mostrar_ventana(self):
        self.label_jugador_turno.setText(
            f" Jugador de turno: {self.jugadores[self.turno]}"
        )
        self.show()

    """
    def mostrar_ventana(self, nombre):
        self.usuario_actual = nombre
        self.show()
    """
