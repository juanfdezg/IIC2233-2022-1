import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from os.path import join
from utils import data_json
from PyQt5.QtMultimedia import QSound

window_name, base_class = uic.loadUiType(join(*data_json("RUTA_PANTALLA_ESPERA")))


class VentanaEspera(window_name, base_class):
    senal_iniciar_partida = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_iniciar_partida.clicked.connect(self.iniciar_partida)
        self.label_ficha1.hide()
        self.label_ficha2.hide()
        self.label_ficha3.hide()
        self.label_ficha4.hide()

    def iniciar_partida(self):
        diccionario = {
            "comando": "iniciar_partida",
            "jugadores": self.jugadores,
            "usuario_actual": self.usuario_actual,
        }
        self.senal_iniciar_partida.emit(diccionario)

    def mostrar_error(self, error):
        if error == "no_admin":
            self.label_error.setText(
                "       Solo el administrador puede iniciar la partida"
            )
        elif error == "minimo_jugadores":
            self.label_error.setText(
                "Se necesitan mínimo 2 jugadores para iniciar la partida"
            )

    def preparar_ventana(self, jugadores):
        self.jugadores = jugadores
        if len(self.jugadores) == 1:
            self.label_jugador1.setText(f"{self.jugadores[0]} (admin)")
            self.label_color1.setText("Azul")
            self.label_ficha1.show()
            self.eliminar_jugadores(1)
        elif len(self.jugadores) == 2:
            self.label_jugador1.setText(f"{self.jugadores[0]} (admin)")
            self.label_jugador2.setText(self.jugadores[1])
            self.label_color1.setText("Azul")
            self.label_color2.setText("Verde")
            self.label_ficha1.show()
            self.label_ficha2.show()
            self.eliminar_jugadores(2)
        elif len(self.jugadores) == 3:
            self.label_jugador1.setText(f"{self.jugadores[0]} (admin)")
            self.label_jugador2.setText(self.jugadores[1])
            self.label_jugador3.setText(self.jugadores[2])
            self.label_color1.setText("Azul")
            self.label_color2.setText("Verde")
            self.label_color3.setText("Amarillo")
            self.label_ficha1.show()
            self.label_ficha2.show()
            self.label_ficha3.show()
            self.eliminar_jugadores(3)
        elif len(self.jugadores) == 4:
            self.label_jugador1.setText(f"{self.jugadores[0]} (admin)")
            self.label_jugador2.setText(self.jugadores[1])
            self.label_jugador3.setText(self.jugadores[2])
            self.label_jugador4.setText(self.jugadores[3])
            self.label_color1.setText("Azul")
            self.label_color2.setText("Verde")
            self.label_color3.setText("Amarillo")
            self.label_color4.setText("Rojo")
            self.label_ficha1.show()
            self.label_ficha2.show()
            self.label_ficha3.show()
            self.label_ficha4.show()

    def eliminar_jugadores(self, cantidad):
        if cantidad == 1:
            self.label_jugador2.setText("")
            self.label_color2.setText("")
            self.label_ficha2.hide()
            self.label_jugador3.setText("")
            self.label_color3.setText("")
            self.label_ficha3.hide()
            self.label_jugador4.setText("")
            self.label_color4.setText("")
            self.label_ficha4.hide()
        if cantidad == 2:
            self.label_jugador3.setText("")
            self.label_color3.setText("")
            self.label_ficha3.hide()
            self.label_jugador4.setText("")
            self.label_color4.setText("")
            self.label_ficha4.hide()
        if cantidad == 3:
            self.label_jugador4.setText("")
            self.label_color4.setText("")
            self.label_ficha4.hide()

    def servidor_caido(self):
        self.label_error.setText(
            "           Servidor caído, ventana se cerrará en 3, 2, 1..."
        )

    def abrir_ventana_juego(self):
        self.hide()

    def mostrar_ventana(self, nombre):
        self.usuario_actual = nombre
        self.show()
        if len(self.jugadores) == 4:
            self.iniciar_partida()
