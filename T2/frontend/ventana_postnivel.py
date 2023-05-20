import sys

sys.path.append("../T2")

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QRadioButton,
    QMessageBox,
)

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POSTNIVEL)


class VentanaPostnivel(window_name, base_class):
    senal_siguiente_nivel = pyqtSignal()
    senal_desaparecer_aliens = pyqtSignal()
    senal_cerrar_juego = pyqtSignal()
    senal_guardar_puntaje = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def mostrar_ventana(
        self, nivel, balas, tiempo, puntaje_total, puntaje_nivel, nivel_completado
    ):
        self.nivel = nivel
        self.balas = balas
        self.tiempo = tiempo
        self.puntaje_total = puntaje_total
        self.puntaje_nivel = puntaje_nivel
        self.nivel_completado = nivel_completado
        self.cambiar_elementos()

        self.show()

    def init_gui(self):
        self.boton_siguiente_nivel.clicked.connect(self.siguiente_nivel)
        self.boton_salir.clicked.connect(self.salir)

    def cambiar_elementos(self):
        if self.nivel == 0:
            self.contador_nivel.setText(f"1")
        else:
            self.contador_nivel.setText(f"{self.nivel}")
        self.contador_balas_restantes.setText(f"{self.balas}")
        self.contador_tiempo_restante.setText(f"{self.tiempo} segundos")
        self.contador_puntaje_total.setText(f"{self.puntaje_total} puntos")
        self.contador_puntaje_nivel.setText(f"{self.puntaje_nivel} puntos")

        if self.nivel_completado:
            self.mensaje_nivel.setText(f"!Puedes dominar el siguiente nivel!")
            self.mensaje_nivel.setStyleSheet(
                "background-color: green; color: white; font-size: \
                12pt;border.radius: 10"
            )

        else:
            self.mensaje_nivel.setText(f"!Perdiste! No puedes seguir jugando :(")
            self.mensaje_nivel.setStyleSheet(
                "background-color: red; color: white; font-size: 12pt;\
            border.radius: 10"
            )
            self.boton_siguiente_nivel.setStyleSheet(
                "background-color: black; border-radius: 20;\
                color: white; font-size: 14pt"
            )

    def siguiente_nivel(self):
        if self.nivel_completado:
            self.senal_siguiente_nivel.emit()
            self.hide()
        elif not self.nivel_completado:
            self.siguiente_inhabilitado()

    def siguiente_inhabilitado(self):
        mensaje_alerta = QMessageBox()
        mensaje_alerta.setWindowTitle("Mensaje de alerta")
        mensaje_alerta.setText("Esta opción se encuentra bloqueada :(")
        pop_up = mensaje_alerta.exec_()

    def salir(self):
        self.close()
        self.senal_cerrar_juego.emit()
