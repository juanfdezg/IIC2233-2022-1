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
    QRadioButton,
    QMessageBox,
    QButtonGroup,
)


class VentanaPrincipal(QWidget):
    senal_enviar_usuario_nivel = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

        self.setGeometry(540, 100, 900, 600)
        self.setMaximumSize(900, 600)
        self.setMinimumSize(900, 600)
        self.setWindowTitle("Ventana Principal")
        self.setStyleSheet("background-color: rgb(33, 30, 47);")
        self.crear_elementos()

    def crear_elementos(self):
        self.nombre_nivel = ""

        self.elegir_ambiente = QLabel("Elige el ambiente de caza espacial", self)
        self.elegir_ambiente.setStyleSheet("color: white; font-size: 18pt")

        self.fondo_tutorial_lunar = QLabel(self)
        pixeles1 = QPixmap(p.RUTA_TUTORIAL_LUNAR)
        self.fondo_tutorial_lunar.setPixmap(pixeles1)
        self.fondo_tutorial_lunar.setScaledContents(True)
        self.fondo_tutorial_lunar.setMaximumSize(200, 200)

        self.fondo_jupiter = QLabel(self)
        pixeles2 = QPixmap(p.RUTA_JUPITER)
        self.fondo_jupiter.setPixmap(pixeles2)
        self.fondo_jupiter.setScaledContents(True)
        self.fondo_jupiter.setMaximumSize(200, 200)

        self.fondo_invasion = QLabel(self)
        pixeles3 = QPixmap(p.RUTA_INVASION)
        self.fondo_invasion.setPixmap(pixeles3)
        self.fondo_invasion.setScaledContents(True)
        self.fondo_invasion.setMaximumSize(200, 200)

        self.alien1 = QLabel(self)
        pixeles4 = QPixmap(p.RUTA_ALIEN1)
        self.alien1.setPixmap(pixeles4)
        self.alien1.setScaledContents(True)
        self.alien1.setMaximumSize(50, 50)

        self.alien2 = QLabel(self)
        pixeles5 = QPixmap(p.RUTA_ALIEN2)
        self.alien2.setPixmap(pixeles5)
        self.alien2.setScaledContents(True)
        self.alien2.setMaximumSize(50, 50)

        self.alien3 = QLabel(self)
        pixeles6 = QPixmap(p.RUTA_ALIEN3)
        self.alien3.setPixmap(pixeles6)
        self.alien3.setScaledContents(True)
        self.alien3.setMaximumSize(50, 50)

        self.rboton1 = QRadioButton("Tutorial lunar")
        self.rboton1.setStyleSheet("color: white")
        self.rboton2 = QRadioButton("Entrenamiento en Júpiter")
        self.rboton2.setStyleSheet("color: white")
        self.rboton3 = QRadioButton("Invasión Intergaláctica")
        self.rboton3.setStyleSheet("color: white")

        self.rboton1.toggled.connect(self.onClicked)
        self.rboton2.toggled.connect(self.onClicked)
        self.rboton3.toggled.connect(self.onClicked)

        self.ingresar_usuario = QLabel("Nombre de astronauta", self)
        self.ingresar_usuario.setStyleSheet("color: white")
        self.usuario_form = QLineEdit("", self)
        self.usuario_form.setStyleSheet("color: white")

        self.boton_cazar = QPushButton("Cazar aquí", self)
        self.boton_cazar.setStyleSheet("color: white")
        self.boton_cazar.clicked.connect(self.enviar_usuario_nivel)

        self.dog1 = QLabel(self)
        pixeles7 = QPixmap(p.RUTA_DOG1)
        self.dog1.setPixmap(pixeles7)
        self.dog1.setScaledContents(True)
        self.dog1.setMaximumSize(150, 150)

        # CREAMOS LOS LAYOUTS

        caja_elegir_ambiente = QHBoxLayout()
        caja_elegir_ambiente.addStretch(1)
        caja_elegir_ambiente.addWidget(self.elegir_ambiente)
        caja_elegir_ambiente.addStretch(1)

        caja_fondos = QHBoxLayout()
        caja_fondos.addWidget(self.fondo_tutorial_lunar)
        caja_fondos.addWidget(self.fondo_jupiter)
        caja_fondos.addWidget(self.fondo_invasion)

        caja_aliens = QHBoxLayout()
        caja_aliens.addStretch(1)
        caja_aliens.addWidget(self.alien1)
        caja_aliens.addStretch(1)
        caja_aliens.addWidget(self.alien2)
        caja_aliens.addStretch(1)
        caja_aliens.addWidget(self.alien3)
        caja_aliens.addStretch(1)

        caja_rbotones = QHBoxLayout()
        caja_rbotones.addStretch(1)
        caja_rbotones.addWidget(self.rboton1)
        caja_rbotones.addStretch(1)
        caja_rbotones.addWidget(self.rboton2)
        caja_rbotones.addStretch(1)
        caja_rbotones.addWidget(self.rboton3)
        caja_rbotones.addStretch(1)

        caja_usuario = QVBoxLayout()
        caja_usuario.addWidget(self.ingresar_usuario)
        caja_usuario.addWidget(self.usuario_form)
        caja_usuario.addStretch(1)

        caja_usuario2 = QHBoxLayout()
        caja_usuario2.addStretch(1)
        caja_usuario2.addLayout(caja_usuario)
        caja_usuario2.addStretch(3)

        caja_cazar_dog1 = QHBoxLayout()
        caja_cazar_dog1.addWidget(self.boton_cazar)
        caja_cazar_dog1.addWidget(self.dog1)
        caja_cazar_dog1.addStretch(2)

        caja_abajo = QHBoxLayout()
        caja_abajo.addLayout(caja_usuario2)
        caja_abajo.addLayout(caja_cazar_dog1)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(caja_elegir_ambiente)
        vbox1.addStretch(1)
        vbox1.addLayout(caja_fondos)
        vbox1.addLayout(caja_aliens)
        vbox1.addStretch(1)
        vbox1.addLayout(caja_rbotones)
        vbox1.addStretch(2)
        vbox1.addLayout(caja_abajo)

        self.setLayout(vbox1)

    def mostrar_ventana(self):
        self.show()

    def enviar_usuario_nivel(self):
        usuario = self.usuario_form.text()
        if not self.nombre_nivel:
            mensaje_alerta = QMessageBox()
            mensaje_alerta.setWindowTitle("Mensaje de alerta")
            mensaje_alerta.setText("Debes seleccionar un nivel para poder jugar!")
            pop_up = mensaje_alerta.exec_()

        else:
            self.senal_enviar_usuario_nivel.emit(usuario, self.nombre_nivel)

    # Método inspirado en AS3
    def recibir_validacion(self, valido):
        if valido:
            self.hide()
        else:
            self.usuario_form.setText("")
            self.usuario_form.setPlaceholderText("Usuario inválido!")

    def onClicked(self):
        boton_radio = self.sender()
        if boton_radio.isChecked():
            nivel = str(boton_radio.text())
            self.nombre_nivel = nivel

    def reiniciar_ventana(self):
        self.usuario_form.setText("")
