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


class VentanaInicio(QWidget):
    senal_abrir_ventana_principal = pyqtSignal()
    senal_abrir_ventana_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 700)
        self.setMaximumSize(700, 700)
        self.setMinimumSize(700, 700)
        self.setWindowTitle("Ventana de Inicio")
        self.setStyleSheet("background-color: rgb(33, 30, 47);")
        self.crear_elementos()

    def crear_elementos(self):
        self.logo = QLabel(self)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMaximumSize(350, 350)

        self.boton_jugar = QPushButton("Jugar", self)
        self.boton_jugar.setStyleSheet("background-color: rgb(125, 158, 181);")
        self.boton_jugar.clicked.connect(self.abrir_ventana_principal)

        self.boton_ranking = QPushButton("Ranking", self)
        self.boton_ranking.setStyleSheet("background-color: rgb(125, 158, 181);")
        self.boton_ranking.clicked.connect(self.abrir_ventana_ranking)

        caja_botones = QVBoxLayout()
        caja_botones.addWidget(self.boton_jugar)
        caja_botones.addWidget(self.boton_ranking)

        caja_logo = QHBoxLayout()
        caja_logo.addWidget(self.logo)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addLayout(caja_botones)
        hbox1.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(caja_logo)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox)

        self.setLayout(hbox2)

    def abrir_ventana_principal(self):
        self.hide()
        self.senal_abrir_ventana_principal.emit()

    def abrir_ventana_ranking(self):
        self.hide()
        self.senal_abrir_ventana_ranking.emit()

    def mostrar_ventana(self):
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.show()
    sys.exit(app.exec_())
