import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from os.path import join
from utils import data_json
from PyQt5.QtMultimedia import QSound

window_name, base_class = uic.loadUiType(join(*data_json("RUTA_PANTALLA_INICIO")))


class VentanaInicio(window_name, base_class):
    senal_enviar_usuario = pyqtSignal(dict)
    senal_abrir_ventana_espera = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_jugar.clicked.connect(self.enviar_usuario)

    def enviar_usuario(self):
        nombre_usuario = self.barra_usuario.text()
        diccionario1 = {"comando": "validar_usuario", "nombre_usuario": nombre_usuario}

        diccionario2 = {
            "comando": "abrir_ventana_espera",
            "nombre_usuario": nombre_usuario,
        }
        self.senal_enviar_usuario.emit(diccionario1)
        self.senal_abrir_ventana_espera.emit(diccionario2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.enviar_usuario()

    def mostrar_error(self, error):
        if error == "largo_invalido":
            self.label_error.setText(
                "¡El nombre debe tener un largo entre 1 y 10 caracteres!"
            )
        elif error == "no_alfanumerico":
            self.label_error.setText(
                "                 ¡El nombre debe ser alfanumérico!"
            )
        elif error == "usuario_ya_existente":
            self.label_error.setText(
                "             ¡Usuario ya existente! Prueba con otro."
            )
        elif error == "maximo_de_jugadores":
            self.label_error.setText(
                "              Sala de espera llena, debes esperar un poco."
            )
        elif error == "partida_iniciada":
            self.label_error.setText(
                " Hay una partida en progreso, debes esperar a que termine."
            )

    def servidor_caido(self):
        self.label_error.setText(
            "           Servidor caído, ventana se cerrará en 3, 2, 1..."
        )

    def mostrar_ventana(self):
        self.show()
