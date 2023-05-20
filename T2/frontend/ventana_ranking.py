import sys

sys.path.append("../T2")
import parametros as p
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
)


class VentanaRanking(QWidget):
    senal_volver_ventana_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 600, 500)
        self.setMaximumSize(600, 500)
        self.setMinimumSize(600, 500)
        self.setWindowTitle("Ventana de Ranking")
        self.setStyleSheet("background-color: rgb(33, 30, 47);")
        self.crear_elementos()
        self.leer_puntajes()

    def crear_elementos(self):
        self.titulo_ranking = QLabel("RANKING DE PUNTAJES", self)
        self.titulo_ranking.setStyleSheet("color: white; font-size: 16pt")

    def sort_seleccionar_puntaje(self, valor):
        return valor[1]

    def leer_puntajes(self):
        lista_puntajes = []
        with open(p.RUTA_PUNTAJES, "r") as puntajes:
            for linea in puntajes:
                linea = linea.strip().split(",")
                usuario = linea[0]
                puntaje = int(linea[1])
                lista_puntajes.append([usuario, puntaje])

        lista_puntajes.sort(key=self.sort_seleccionar_puntaje, reverse=True)
        lista_puntajes = lista_puntajes[0:5]

        self.usuario1 = QLabel(f"1. {lista_puntajes[0][0]}", self)
        self.usuario1.setStyleSheet("color: white; font-size: 11pt")
        self.usuario1.setMaximumSize(200, 100)
        self.puntaje1 = QLabel(f"{lista_puntajes[0][1]} puntos", self)
        self.puntaje1.setStyleSheet("color: white; font-size: 11pt;")
        self.puntaje1.resize(300, 100)

        self.usuario2 = QLabel(f"2. {lista_puntajes[1][0]}", self)
        self.usuario2.setStyleSheet("color: white; font-size: 11pt")
        self.usuario2.setMaximumSize(200, 100)
        self.puntaje2 = QLabel(f"{lista_puntajes[1][1]} puntos", self)
        self.puntaje2.setStyleSheet("color: white; font-size: 11pt;")
        self.puntaje2.resize(300, 100)

        self.usuario3 = QLabel(f"3. {lista_puntajes[2][0]}", self)
        self.usuario3.setStyleSheet("color: white; font-size: 11pt")
        self.usuario3.setMaximumSize(200, 100)
        self.puntaje3 = QLabel(f"{lista_puntajes[2][1]} puntos", self)
        self.puntaje3.setStyleSheet("color: white; font-size: 11pt;")
        self.puntaje3.resize(300, 100)

        self.usuario4 = QLabel(f"4. {lista_puntajes[3][0]}", self)
        self.usuario4.setStyleSheet("color: white; font-size: 11pt")
        self.usuario4.setMaximumSize(200, 100)
        self.puntaje4 = QLabel(f"{lista_puntajes[3][1]} puntos", self)
        self.puntaje4.setStyleSheet("color: white; font-size: 11pt")
        self.puntaje4.resize(300, 100)

        self.usuario5 = QLabel(f"5. {lista_puntajes[4][0]}", self)
        self.usuario5.setStyleSheet("color: white; font-size: 11pt")
        self.usuario5.setMaximumSize(200, 100)
        self.puntaje5 = QLabel(f"{lista_puntajes[4][1]} puntos", self)
        self.puntaje5.setStyleSheet("color: white; font-size: 11pt;")
        self.puntaje5.resize(300, 100)

        self.boton_volver = QPushButton("Volver", self)
        self.boton_volver.setStyleSheet("background-color: rgb(125, 158, 181);")
        self.boton_volver.clicked.connect(self.volver_ventana_inicio)

        # --LAYOUTS--

        caja_titulo = QHBoxLayout()
        caja_titulo.addStretch(1)
        caja_titulo.addWidget(self.titulo_ranking)
        caja_titulo.addStretch(1)

        caja1 = QHBoxLayout()
        caja1.addStretch(1)
        caja1.addWidget(self.usuario1)
        caja1.addStretch(1)
        caja1.addWidget(self.puntaje1)
        caja1.addStretch(1)

        caja2 = QHBoxLayout()
        caja2.addStretch(1)
        caja2.addWidget(self.usuario2)
        caja2.addStretch(1)
        caja2.addWidget(self.puntaje2)
        caja2.addStretch(1)

        caja3 = QHBoxLayout()
        caja3.addStretch(1)
        caja3.addWidget(self.usuario3)
        caja3.addStretch(1)
        caja3.addWidget(self.puntaje3)
        caja3.addStretch(1)

        caja4 = QHBoxLayout()
        caja4.addStretch(1)
        caja4.addWidget(self.usuario4)
        caja4.addStretch(1)
        caja4.addWidget(self.puntaje4)
        caja4.addStretch(1)

        caja5 = QHBoxLayout()
        caja5.addStretch(1)
        caja5.addWidget(self.usuario5)
        caja5.addStretch(1)
        caja5.addWidget(self.puntaje5)
        caja5.addStretch(1)

        caja_boton_volver = QHBoxLayout()
        caja_boton_volver.addStretch(1)
        caja_boton_volver.addWidget(self.boton_volver)
        caja_boton_volver.addStretch(1)

        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addLayout(caja_titulo)
        vbox1.addStretch(1)
        vbox1.addLayout(caja1)
        vbox1.addLayout(caja2)
        vbox1.addLayout(caja3)
        vbox1.addLayout(caja4)
        vbox1.addLayout(caja5)
        vbox1.addStretch(1)
        vbox1.addLayout(caja_boton_volver)
        vbox1.addStretch(2)

        self.setLayout(vbox1)

    def mostrar_ventana(self):
        self.show()

    def volver_ventana_inicio(self):
        self.hide()
        self.senal_volver_ventana_inicio.emit()
