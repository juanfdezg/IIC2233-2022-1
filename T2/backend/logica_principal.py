import sys

sys.path.append("../T2")
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal


class LogicaPrincipal(QObject):
    senal_respuesta_validacion = pyqtSignal(bool)
    senal_abrir_ventana_juego = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

    # Método basado en AS3
    def comprobar_usuario_nivel(self, usuario, nivel):
        usuario_correcto = True
        vacio = False
        if not usuario.strip(""):
            vacio = True

        if (not usuario.isalnum()) or vacio or (len(usuario) > p.MAX_CARACTERES):
            usuario_correcto = False

        if usuario_correcto:
            self.senal_abrir_ventana_juego.emit(usuario, nivel)

        self.senal_respuesta_validacion.emit(usuario_correcto)
