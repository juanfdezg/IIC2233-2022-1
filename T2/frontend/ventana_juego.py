import sys

sys.path.append("../T2")

from PyQt5 import uic
from PyQt5.QtMultimedia import QSound
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
)

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):
    senal_tecla = pyqtSignal(str)
    senal_iniciar_juego = pyqtSignal(str, bool)
    senal_abrir_ventana_postnivel = pyqtSignal()
    senal_volver_ventana_inicio = pyqtSignal()
    senal_pausa_juego = pyqtSignal()
    senal_pausa_mira = pyqtSignal()
    senal_guardar_usuario = pyqtSignal(str)
    senal_guardar_puntaje = pyqtSignal()
    senal_cheatcode_balas = pyqtSignal()
    senal_cheatcode_nivel = pyqtSignal()
    senal_reiniciar_backend = pyqtSignal()
    senal_reiniciar_frontend = pyqtSignal()
    senal_reiniciar_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.sonido_disparo = QSound(p.RUTA_SONIDO_DISPARO)
        self.sonido_risa = QSound(p.RUTA_SONIDO_RISA)
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_salir.clicked.connect(self.salir)
        self.boton_pausa.clicked.connect(self.pausar_juego)
        self.salir_desde_postnivel = False
        self.mira.move(370, 230)
        self.setWindowTitle("Ventana de juego")
        self.labels_aliens = []
        self.teclas_presionadas = ""
        self.nivel_superado = QLabel("", self)

        self.disparo1 = QLabel(self)
        pixeles = QPixmap(p.RUTA_DISPARO_F1)
        self.disparo1.setPixmap(pixeles)
        self.disparo1.setScaledContents(True)
        self.disparo1.setStyleSheet("background-color: transparent")
        self.disparo1.hide()

        self.disparo2 = QLabel(self)
        pixeles = QPixmap(p.RUTA_DISPARO_F2)
        self.disparo2.setPixmap(pixeles)
        self.disparo2.setScaledContents(True)
        self.disparo2.setStyleSheet("background-color: transparent")
        self.disparo2.hide()

        self.disparo3 = QLabel(self)
        pixeles = QPixmap(p.RUTA_DISPARO_F3)
        self.disparo3.setPixmap(pixeles)
        self.disparo3.setScaledContents(True)
        self.disparo3.setStyleSheet("background-color: transparent")
        self.disparo3.hide()

    def mostrar_ventana(self, usuario, nivel):
        self.show()
        self.senal_guardar_usuario.emit(usuario)
        self.contador_puntaje.setText(f"{str(p.PUNTAJE_INICIAL)} puntos")
        self.contador_nivel.setText(str(p.NIVEL_INICIAL))
        self.aliens_destruidos.setText(f"Aliens destruidos: 0")
        self.cargar_fondo(usuario, nivel)

    def actualizar_nivel(self, nivel):
        self.contador_nivel.setText(str(nivel))

    def actualizar_puntaje(self, puntaje):
        self.contador_puntaje.setText(f"{str(puntaje)} puntos")

    def actualizar_balas(self, balas):
        self.contador_balas.setText(f"X {str(balas)}")

    def actualizar_tiempo(self, tiempo):
        self.barra_tiempo.setValue(tiempo)

    def actualizar_nivel(self, nivel):
        self.contador_nivel.setText(f"{str(nivel)}")

    def actualizar_aliens_restantes(self, aliens):
        self.aliens_restantes.setText(f"Aliens restantes: {aliens}")

    def actualizar_aliens_destruidos(self, aliens):
        self.aliens_destruidos.setText(f"Aliens destruidos: {aliens}")

    def cargar_fondo(self, usuario, nivel):
        if nivel == "Tutorial lunar":
            pixeles = QPixmap(p.RUTA_FONDO_LUNA)
            self.fondo.setPixmap(pixeles)
            self.fondo.setScaledContents(True)
            self.pixeles_alien = QPixmap(p.RUTA_ALIEN1)
            self.senal_iniciar_juego.emit("TUTORIAL", False)

        if nivel == "Entrenamiento en Júpiter":
            pixeles = QPixmap(p.RUTA_FONDO_JUPITER)
            self.fondo.setPixmap(pixeles)
            self.fondo.setScaledContents(True)
            self.pixeles_alien = QPixmap(p.RUTA_ALIEN2)
            self.senal_iniciar_juego.emit("ENTRENAMIENTO", False)

        elif nivel == "Invasión Intergaláctica":
            pixeles = QPixmap(p.RUTA_FONDO_GALAXIA)
            self.fondo.setPixmap(pixeles)
            self.fondo.setScaledContents(True)
            self.pixeles_alien = QPixmap(p.RUTA_ALIEN3)
            self.senal_iniciar_juego.emit("INVASION", False)

        self.terminator_dog = QLabel(self)
        pixeles = QPixmap(p.RUTA_DOG1)
        self.terminator_dog.setPixmap(pixeles)
        self.terminator_dog.setScaledContents(True)
        self.terminator_dog.setStyleSheet("background-color: transparent")
        self.terminator_dog.move(700, 521)
        self.terminator_dog.setMaximumSize(150, 150)
        self.terminator_dog.show()

    def keyPressEvent(self, event):
        # COMPLETAR

        if event.text() == p.TECLA_IZQUIERDA:
            self.senal_tecla.emit("L")

        if event.text() == p.TECLA_ARRIBA:
            self.senal_tecla.emit("U")

        if event.text() == p.TECLA_DERECHA:
            self.senal_tecla.emit("R")

        if event.text() == p.TECLA_ABAJO:
            self.senal_tecla.emit("D")

        if event.text() == p.TECLA_DISPARAR:
            self.senal_tecla.emit("S")

        if event.text() == p.TECLA_PAUSA:
            self.pausar_juego()

        self.teclas_presionadas += event.text()
        if len(self.teclas_presionadas) >= 4:
            if (
                self.teclas_presionadas[-1] == "i"
                and self.teclas_presionadas[-2] == "n"
                and self.teclas_presionadas[-3] == "v"
                and self.teclas_presionadas[-4] == "o"
            ):
                self.senal_cheatcode_balas.emit()
        if len(self.teclas_presionadas) >= 3:
            if (
                self.teclas_presionadas[-1] == "a"
                and self.teclas_presionadas[-2] == "i"
                and self.teclas_presionadas[-3] == "c"
            ):
                self.senal_cheatcode_nivel.emit()

    def pausar_juego(self):
        self.senal_pausa_juego.emit()
        self.senal_pausa_mira.emit()

    def avanzar_mira(self, posicion):
        self.mira.move(posicion[0], posicion[1])

    def disparar(self):
        pixeles = QPixmap(p.RUTA_DISPARADOR_ROJO)
        self.mira.setPixmap(pixeles)
        self.mira.setScaledContents(True)
        self.sonido_disparo.play()

    def mira_original(self):
        pixeles = QPixmap(p.RUTA_DISPARADOR_NEGRO)
        self.mira.setPixmap(pixeles)
        self.mira.setScaledContents(True)

    def agregar_alien(self, x1, y1, x2, y2):
        for alien in self.labels_aliens:
            alien.hide()
        self.labels_aliens = []
        self.alien1_label = QLabel(self)
        self.alien1_label.setPixmap(self.pixeles_alien)
        self.alien1_label.setScaledContents(True)
        self.alien1_label.setGeometry(x1, y1, p.ANCHO_ALIEN, p.ALTO_ALIEN)
        self.alien1_label.setStyleSheet("background-color: transparent")
        self.alien1_label.show()
        self.alien1_label.stackUnder(self.mira)

        self.alien2_label = QLabel(self)
        self.alien2_label.setPixmap(self.pixeles_alien)
        self.alien2_label.setScaledContents(True)
        self.alien2_label.setGeometry(x2, y2, p.ANCHO_ALIEN, p.ALTO_ALIEN)
        self.alien2_label.setStyleSheet("background-color: transparent")
        self.alien2_label.show()
        self.alien2_label.stackUnder(self.mira)

        self.labels_aliens.append(self.alien1_label)
        self.labels_aliens.append(self.alien2_label)

    def mover_alien(self, x1, y1, x2, y2):
        self.alien1_label.move(x1, y1)
        self.alien2_label.move(x2, y2)

    def abrir_ventana_postnivel(self):
        self.hide()
        self.senal_abrir_ventana_postnivel.emit()

    def desaparecer_alien(self, id_alien):
        self.labels_aliens[id_alien].hide()

    def aparecer_explosion(self, x, y, disparo):
        if disparo == 1:
            self.disparo1.move(x, y)
            self.disparo1.show()
        if disparo == 2:
            self.disparo2.move(x, y)
            self.disparo2.show()
            self.disparo1.stackUnder(self.disparo2)
        if disparo == 3:
            self.disparo3.move(x, y)
            self.disparo3.show()

    def desaparecer_explosion(self, disparo):
        if disparo == 1:
            self.disparo1.hide()
        if disparo == 2:
            self.disparo2.hide()
        if disparo == 3:
            self.disparo3.hide()

    def mover_dog1(self, nivel_escogido, secuencia):
        if secuencia == 1:
            self.sonido_risa.play()
            self.terminator_dog2 = QLabel(self)
            if nivel_escogido == "TUTORIAL":
                pixeles = QPixmap(p.RUTA_DOG_ALIEN_1)
            if nivel_escogido == "ENTRENAMIENTO":
                pixeles = QPixmap(p.RUTA_DOG_ALIEN_2)
            if nivel_escogido == "INVASION":
                pixeles = QPixmap(p.RUTA_DOG_ALIEN_3)

            self.terminator_dog2.setPixmap(pixeles)
            self.terminator_dog2.setScaledContents(True)
            self.terminator_dog2.setStyleSheet("background-color: transparent")
            self.terminator_dog2.move(700, 505)
            self.terminator_dog2.setMaximumSize(200, 150)
            self.terminator_dog2.show()
            self.terminator_dog.hide()

        if secuencia == 2:
            self.terminator_dog.show()
            self.terminator_dog2.hide()

    def nivel_superado_aparecer(self):
        self.nivel_superado = QLabel("¡Nivel superado!", self)
        self.nivel_superado.setStyleSheet(
            "background-color: transparent; color: white;\
             font-size: 26pt"
        )
        self.nivel_superado.move(600, 200)
        self.nivel_superado.show()

    def nivel_superado_desaparecer(self):
        self.nivel_superado.hide()

    def salir(self):
        self.close()
        self.salir_desde_postnivel = False
        self.senal_guardar_puntaje.emit()
        self.senal_reiniciar_backend.emit()
        self.senal_reiniciar_frontend.emit()
        self.senal_reiniciar_juego.emit()
        self.senal_volver_ventana_inicio.emit()
