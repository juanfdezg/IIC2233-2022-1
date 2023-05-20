import sys

sys.path.append("../T2")
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class Mira(QObject):
    senal_mover_mira = pyqtSignal(tuple)
    senal_disparar = pyqtSignal()
    senal_mira_original = pyqtSignal()
    senal_restar_bala = pyqtSignal()
    senal_disparo_hecho = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.__posicionX = 370
        self.__posicionY = 230
        self.pausa_mira = False

    @property
    def posicionX(self):
        return self.__posicionX

    @posicionX.setter
    def posicionX(self, valor):
        if valor > 840:
            self.__posicionX = 840
        elif valor < -125:
            self.__posicionX = -125
        else:
            self.__posicionX = valor

    @property
    def posicionY(self):
        return self.__posicionY

    @posicionY.setter
    def posicionY(self, valor):
        if valor > 570:
            self.__posicionY = 570
        elif valor < -80:
            self.__posicionY = -80
        else:
            self.__posicionY = valor

    def avanzar(self, direccion):
        if not self.pausa_mira:
            if direccion in "URDL":
                if direccion == "U":
                    self.posicionY -= p.VELOCIDAD_MIRA

                elif direccion == "R":
                    self.posicionX += p.VELOCIDAD_MIRA

                elif direccion == "D":
                    self.posicionY += p.VELOCIDAD_MIRA

                elif direccion == "L":
                    self.posicionX -= p.VELOCIDAD_MIRA

                self.senal_mover_mira.emit((self.posicionX, self.posicionY))

            elif direccion == "S":
                self.disparar()

    def disparar(self):
        self.senal_disparar.emit()
        self.senal_restar_bala.emit()
        self.timer = QTimer()
        self.timer.timeout.connect(self.mira_original)
        self.timer.setInterval(1000)
        self.timer.setSingleShot(True)
        self.timer.start()
        self.senal_disparo_hecho.emit()

    def mira_original(self):
        self.senal_mira_original.emit()

    def pausar_mira(self):
        self.pausa_mira = not self.pausa_mira


class Alien(QObject):
    def __init__(self, x, y):
        super().__init__()
        self.__x = x
        self.__y = y
        self.alto = 80
        self.ancho = 300
        self.velocidad_x = p.VELOCIDAD_ALIEN[0]
        self.velocidad_y = p.VELOCIDAD_ALIEN[1]
        self.activo = True

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        if valor > 900:
            self.__x = 900
        elif valor < 0:
            self.__x = 0
        else:
            self.__x = valor

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        if valor > 580:
            self.__y = 580
        elif valor < 0:
            self.__y = 0
        else:
            self.__y = valor
