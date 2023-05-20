import sys
from backend.clases_objetos import Alien, Mira

sys.path.append("../T2")
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from random import randint, choice


class Juego(QObject):
    senal_aparecer_alien = pyqtSignal(int, int, int, int)
    senal_moverse_alien = pyqtSignal(int, int, int, int)
    senal_actualizar_balas_label = pyqtSignal(int)
    senal_actualizar_puntaje = pyqtSignal(int)
    senal_disparo_efectivo = pyqtSignal(int)
    senal_actualizar_tiempo = pyqtSignal(int)
    senal_aparecer_explosion = pyqtSignal(int, int, int)
    senal_desaparecer_explosion = pyqtSignal(int)
    senal_tiempo_agotado = pyqtSignal()
    senal_actualizar_nivel = pyqtSignal(int)
    senal_animacion_dog = pyqtSignal(str, int)
    senal_iniciar_nivel = pyqtSignal(str, bool)
    senal_nivel_superado = pyqtSignal()
    senal_nivel_superado_desaparecer = pyqtSignal()
    senal_ventana_postnivel = pyqtSignal(int, int, int, int, int, bool)
    senal_aliens_restantes = pyqtSignal(int)
    senal_aliens_destruidos = pyqtSignal(int)

    def __init__(self, mira):
        super().__init__()
        self.mira = mira
        self.x_max = 900
        self.y_max = 600
        self.nivel_actual = p.NIVEL_INICIAL
        self.cantidad_aliens = self.nivel_actual * 2
        self.cantidad_balas = self.cantidad_aliens * 2
        self.puntaje = p.PUNTAJE_INICIAL
        self.aliens_destruidos_total = 0
        self.aliens_destruidos_nivel = 0
        ponderadores = (1, -1)
        direccion_aleatoria_x = choice(ponderadores)
        direccion_aleatoria_y = choice(ponderadores)
        self.velocidadx_nivel_anterior = p.VELOCIDAD_ALIEN[0] * direccion_aleatoria_x
        self.velocidady_nivel_anterior = p.VELOCIDAD_ALIEN[1] * direccion_aleatoria_y
        self.duracion_nivel_anterior = p.DURACION_NIVEL_INICIAL
        self.contador_primer_nivel = 1
        self.contador_primer_nivel_tiempo = 1
        self.pausa_juego = False

    def iniciar_juego(self, nivel_escogido, nivel_completado):
        if nivel_completado:
            self.aliens_destruidos_contador = 0
            self.aliens_restantes_contador = self.nivel_actual * 2
            self.senal_aliens_restantes.emit(self.aliens_restantes_contador)
            self.senal_aliens_destruidos.emit(self.aliens_destruidos_contador)
        if self.contador_primer_nivel == 1:
            self.senal_actualizar_balas_label.emit(self.cantidad_balas)
            self.aliens_destruidos_contador = 0
            self.aliens_restantes_contador = 2
            self.senal_aliens_restantes.emit(self.aliens_restantes_contador)
            self.contador_primer_nivel += 1
        self.nivel_escogido = nivel_escogido
        self.puntaje_nivel = 0
        self.aparecer_alien()
        if nivel_completado:
            self.cantidad_aliens = self.nivel_actual * 2
            self.cantidad_balas = self.cantidad_aliens * 2
            self.senal_actualizar_balas_label.emit(self.cantidad_balas)
        if nivel_escogido == "TUTORIAL":
            if nivel_completado:
                for i in range(len(self.aliens)):
                    self.aliens[i].velocidad_x = (
                        self.velocidadx_nivel_anterior / p.PONDERADOR_TUTORIAL
                    )
                    self.aliens[i].velocidad_y = (
                        self.velocidady_nivel_anterior / p.PONDERADOR_TUTORIAL
                    )
                self.velocidadx_nivel_anterior = self.aliens[0].velocidad_x
                self.velocidady_nivel_anterior = self.aliens[0].velocidad_y
            if not nivel_completado:
                for alien in self.aliens:
                    alien.velocidad_x = self.velocidadx_nivel_anterior
                    alien.velocidad_y = self.velocidady_nivel_anterior
            if self.contador_primer_nivel_tiempo == 1:
                self.duracion_nivel = int(
                    self.duracion_nivel_anterior * p.PONDERADOR_TUTORIAL
                )
                self.duracion_nivel_timer = self.duracion_nivel
                self.duracion_nivel_anterior = self.duracion_nivel
                self.contador_primer_nivel_tiempo += 1
            if nivel_completado:
                self.duracion_nivel = int(
                    self.duracion_nivel_anterior * p.PONDERADOR_TUTORIAL
                )
                self.duracion_nivel_timer = self.duracion_nivel
                self.duracion_nivel_anterior = self.duracion_nivel
                self.nivel_completado = False

        if nivel_escogido == "ENTRENAMIENTO":
            if nivel_completado:
                for i in range(len(self.aliens)):
                    self.aliens[i].velocidad_x = (
                        self.velocidadx_nivel_anterior / p.PONDERADOR_ENTRENAMIENTO
                    )
                    self.aliens[i].velocidad_y = (
                        self.velocidady_nivel_anterior / p.PONDERADOR_ENTRENAMIENTO
                    )
                self.velocidadx_nivel_anterior = self.aliens[0].velocidad_x
                self.velocidady_nivel_anterior = self.aliens[0].velocidad_y
            if not nivel_completado:
                for alien in self.aliens:
                    alien.velocidad_x = self.velocidadx_nivel_anterior
                    alien.velocidad_y = self.velocidady_nivel_anterior
            if self.contador_primer_nivel_tiempo == 1:
                self.duracion_nivel = int(
                    self.duracion_nivel_anterior * p.PONDERADOR_ENTRENAMIENTO
                )
                self.duracion_nivel_timer = self.duracion_nivel
                self.duracion_nivel_anterior = self.duracion_nivel
                self.contador_primer_nivel_tiempo += 1
            if nivel_completado:
                self.duracion_nivel = int(
                    self.duracion_nivel_anterior * p.PONDERADOR_ENTRENAMIENTO
                )
                self.duracion_nivel_timer = self.duracion_nivel
                self.duracion_nivel_anterior = self.duracion_nivel
                self.nivel_completado = False

        if nivel_escogido == "INVASION":
            if nivel_completado:
                for i in range(len(self.aliens)):
                    self.aliens[i].velocidad_x = (
                        self.velocidadx_nivel_anterior / p.PONDERADOR_INVASION
                    )
                    self.aliens[i].velocidad_y = (
                        self.velocidady_nivel_anterior / p.PONDERADOR_INVASION
                    )
                self.velocidadx_nivel_anterior = self.aliens[0].velocidad_x
                self.velocidady_nivel_anterior = self.aliens[0].velocidad_y
            if not nivel_completado:
                for alien in self.aliens:
                    alien.velocidad_x = self.velocidadx_nivel_anterior
                    alien.velocidad_y = self.velocidady_nivel_anterior
            if self.contador_primer_nivel_tiempo == 1:
                self.duracion_nivel = int(
                    self.duracion_nivel_anterior * p.PONDERADOR_INVASION
                )
                self.duracion_nivel_timer = self.duracion_nivel
                self.duracion_nivel_anterior = self.duracion_nivel
                self.contador_primer_nivel_tiempo += 1
            if nivel_completado:
                self.duracion_nivel = int(
                    self.duracion_nivel_anterior * p.PONDERADOR_INVASION
                )
                self.duracion_nivel_timer = self.duracion_nivel
                self.duracion_nivel_anterior = self.duracion_nivel
                self.nivel_completado = False
        self.nivel_completado = False
        self.actualizar_tiempo()

    def restar_balas(self):
        self.cantidad_balas -= 1
        self.senal_actualizar_balas_label.emit(self.cantidad_balas)
        if self.cantidad_balas == 0 and not self.nivel_completado:
            self.nivel_completado = False
            self.abrir_ventana_postnivel()

    def sumar_puntaje(self, nivel_escogido):
        self.puntaje_nivel = 0
        if nivel_escogido == "TUTORIAL":
            ponderador = p.PONDERADOR_TUTORIAL
        if nivel_escogido == "ENTRENAMIENTO":
            ponderador = p.PONDERADOR_ENTRENAMIENTO
        if nivel_escogido == "INVASION":
            ponderador = p.PONDERADOR_INVASION
        puntaje_nivel = int(
            (
                self.cantidad_aliens * 100
                + (self.duracion_nivel_timer * 30 + self.cantidad_balas * 70)
                * (self.nivel_actual - 1)
            )
            / ponderador
        )
        self.puntaje_nivel = puntaje_nivel
        self.puntaje += puntaje_nivel
        self.senal_actualizar_puntaje.emit(self.puntaje)

    def actualizar_tiempo(self):
        self.senal_actualizar_tiempo.emit(self.duracion_nivel_timer)
        self.timer_tiempo = QTimer()
        self.timer_tiempo.setInterval(1000)
        self.timer_tiempo.timeout.connect(self.enviar_senal_tiempo)
        self.timer_tiempo.start()

    def enviar_senal_tiempo(self):
        self.duracion_nivel_timer -= 1
        self.senal_actualizar_tiempo.emit(self.duracion_nivel_timer)
        if self.duracion_nivel_timer == 0:
            self.abrir_ventana_postnivel()

    def aparecer_alien(self):
        self.aliens = []
        ponderadores = (1, -1)
        direccion_aleatoria_x1 = choice(ponderadores)
        direccion_aleatoria_y1 = choice(ponderadores)
        direccion_aleatoria_x2 = choice(ponderadores)
        direccion_aleatoria_y2 = choice(ponderadores)
        x1 = randint(1, self.x_max - 1)
        y1 = randint(1, self.y_max - 1)
        alien1 = Alien(x1, y1)
        alien1.velocidad_x = alien1.velocidad_x * direccion_aleatoria_x1
        alien1.velocidad_y = alien1.velocidad_y * direccion_aleatoria_y1
        self.aliens.append(alien1)
        x2 = randint(1, self.x_max - 1)
        y2 = randint(1, self.y_max - 1)
        alien2 = Alien(x2, y2)
        alien2.velocidad_x = alien2.velocidad_x * direccion_aleatoria_x2
        alien2.velocidad_y = alien2.velocidad_y * direccion_aleatoria_y2
        self.aliens.append(alien2)
        self.senal_aparecer_alien.emit(x1, y1, x2, y2)
        self.ciclo_movimiento_alien()

    def ciclo_movimiento_alien(self):
        self.timer_moverse = QTimer()
        self.timer_moverse.timeout.connect(self.moverse_alien)
        self.timer_moverse.setInterval(30)
        self.timer_moverse.start()

    def explosion_1(self, x, y):
        self.explosion_x = x
        self.explosion_y = y
        self.senal_aparecer_explosion.emit(self.explosion_x, self.explosion_y, 1)
        self.timer_explosion1 = QTimer()
        self.timer_explosion1.setSingleShot(True)
        self.timer_explosion1.setInterval(300)
        self.timer_explosion1.timeout.connect(self.explosion_2)
        self.timer_explosion1.start()

    def explosion_2(self):
        self.senal_desaparecer_explosion.emit(1)
        self.senal_aparecer_explosion.emit(self.explosion_x, self.explosion_y, 2)
        self.timer_explosion2 = QTimer()
        self.timer_explosion2.setSingleShot(True)
        self.timer_explosion2.setInterval(300)
        self.timer_explosion2.timeout.connect(self.explosion_3)
        self.timer_explosion2.start()

    def explosion_3(self):
        self.senal_desaparecer_explosion.emit(2)
        self.senal_aparecer_explosion.emit(self.explosion_x, self.explosion_y, 3)
        self.timer_explosion3 = QTimer()
        self.timer_explosion3.setSingleShot(True)
        self.timer_explosion3.setInterval(300)
        self.timer_explosion3.timeout.connect(self.desaparecer_explosion_3)
        self.timer_explosion3.start()

    def desaparecer_explosion_3(self):
        self.senal_desaparecer_explosion.emit(3)

    def moverse_alien(self):
        max_x = 900
        max_y = 580
        min_x = 0
        min_y = 0
        # ALIEN 1
        if self.aliens[0].x == max_x or self.aliens[0].x == min_x:
            self.aliens[0].velocidad_x = self.aliens[0].velocidad_x * -1
        if self.aliens[0].y == max_y or self.aliens[0].y == min_y:
            self.aliens[0].velocidad_y = self.aliens[0].velocidad_y * -1
        self.aliens[0].x += self.aliens[0].velocidad_x
        self.aliens[0].y += self.aliens[0].velocidad_y
        # ALIEN 2
        if self.aliens[1].x == max_x or self.aliens[1].x == min_x:
            self.aliens[1].velocidad_x = self.aliens[1].velocidad_x * -1
        if self.aliens[1].y == max_y or self.aliens[1].y == min_y:
            self.aliens[1].velocidad_y = self.aliens[1].velocidad_y * -1
        self.aliens[1].x += self.aliens[1].velocidad_x
        self.aliens[1].y += self.aliens[1].velocidad_y
        self.senal_moverse_alien.emit(
            self.aliens[0].x, self.aliens[0].y, self.aliens[1].x, self.aliens[1].y
        )

    # Métodos de colisiones basados en juego de vaquero visto en clases
    def chequear_colision(self, alien):
        if self.mira.posicionX + 90 > alien.x + p.ANCHO_ALIEN:
            return False
        if self.mira.posicionX + p.ANCHO_MIRA < alien.x + 90:
            return False
        if self.mira.posicionY > alien.y + p.ALTO_ALIEN - 50:
            return False
        if self.mira.posicionY + p.ALTO_MIRA < alien.y + 50:
            return False
        return True

    def chequear_colisiones(self):
        for i in range(len(self.aliens)):
            if self.chequear_colision(self.aliens[i]) and self.aliens[i].activo:
                self.explosion_1(self.aliens[i].x, self.aliens[i].y)
                self.aliens[i].activo = False
                self.senal_disparo_efectivo.emit(i)
                self.aliens_destruidos_contador += 1
                self.aliens_restantes_contador -= 1
                self.senal_aliens_destruidos.emit(self.aliens_destruidos_contador)
                self.senal_aliens_restantes.emit(self.aliens_restantes_contador)
        if not self.revisar_activos():
            self.aliens_destruidos_nivel += 2
            self.aliens_destruidos_total += 2
            # NIVEL COMPLETADO
            if self.aliens_destruidos_nivel == self.cantidad_aliens:
                self.nivel_completado = True
                self.nivel_actual += 1
                self.aliens_destruidos_nivel = 0
                self.senal_actualizar_nivel.emit(self.nivel_actual)
                self.animacion_dog1()
                self.senal_nivel_superado.emit()
                self.duracion_nivel_timer += 1
                self.sumar_puntaje(self.nivel_escogido)
                self.mira.pausar_mira()
                self.pausa()
                self.timer_nivel = QTimer()
                self.timer_nivel.setInterval(1000)
                self.timer_nivel.setSingleShot(True)
                self.timer_nivel.timeout.connect(self.abrir_ventana_postnivel)
                self.timer_nivel.start()
            else:
                self.senal_iniciar_nivel.emit(
                    self.nivel_escogido, self.nivel_completado
                )

    def revisar_activos(self):
        for alien in self.aliens:
            if alien.activo:
                return True
        return False

    def abrir_ventana_postnivel(self):
        self.senal_ventana_postnivel.emit(
            self.nivel_actual - 1,
            self.cantidad_balas,
            self.duracion_nivel_timer,
            self.puntaje,
            self.puntaje_nivel,
            self.nivel_completado,
        )

    def enviar_senal_nivel(self):
        self.mira.pausar_mira()
        self.pausa()
        self.senal_nivel_superado_desaparecer.emit()
        self.senal_iniciar_nivel.emit(self.nivel_escogido, self.nivel_completado)

    def animacion_dog1(self):
        self.senal_animacion_dog.emit(self.nivel_escogido, 1)
        self.timer_animacion_dog1 = QTimer()
        self.timer_animacion_dog1.setSingleShot(True)
        self.timer_animacion_dog1.setInterval(1000)
        self.timer_animacion_dog1.timeout.connect(self.animacion_dog2)
        self.timer_animacion_dog1.start()

    def animacion_dog2(self):
        self.senal_animacion_dog.emit(self.nivel_escogido, 2)

    def pausa(self):
        self.pausa_juego = not self.pausa_juego
        if self.pausa_juego:
            self.timer_tiempo.stop()
            self.timer_moverse.stop()
        elif not self.pausa_juego:
            self.timer_tiempo.start()
            self.timer_moverse.start()

    def almacenar_usuario(self, usuario):
        self.usuario = usuario

    def guardar_puntaje(self):
        informacion = f"\n{self.usuario},{self.puntaje}"
        with open("puntajes.txt", "a") as puntajes:
            puntajes.write(informacion)

    def cheatcode_balas(self):
        self.cantidad_balas = 10000
        self.senal_actualizar_balas_label.emit(self.cantidad_balas)

    def cheatcode_nivel(self):
        self.nivel_actual += 1
        self.aliens_destruidos_nivel = 0
        self.senal_actualizar_nivel.emit(self.nivel_actual)
        self.nivel_completado = True
        self.animacion_dog1()
        self.senal_nivel_superado.emit()
        self.duracion_nivel_timer += 1
        self.sumar_puntaje(self.nivel_escogido)
        self.mira.pausar_mira()
        self.pausa()
        self.timer_nivel = QTimer()
        self.timer_nivel.setInterval(1000)
        self.timer_nivel.setSingleShot(True)
        self.timer_nivel.timeout.connect(self.abrir_ventana_postnivel)
        self.timer_nivel.start()

    def reiniciar_juego(self):
        self.nivel_actual = 1
        self.nivel_completado = False
        self.nivel_actual = p.NIVEL_INICIAL
        self.cantidad_aliens = self.nivel_actual * 2
        self.cantidad_balas = self.cantidad_aliens * 2
        self.puntaje = p.PUNTAJE_INICIAL
        self.aliens_destruidos_total = 0
        self.aliens_destruidos_nivel = 0
        self.velocidadx_nivel_anterior = p.VELOCIDAD_ALIEN[0]
        self.velocidady_nivel_anterior = p.VELOCIDAD_ALIEN[1]
        self.duracion_nivel_anterior = p.DURACION_NIVEL_INICIAL
        self.pausa_juego = False
        self.senal_actualizar_balas_label.emit(self.cantidad_balas)
        self.aliens_destruidos_contador = 0
        self.aliens_restantes_contador = 2
        self.senal_aliens_restantes.emit(self.aliens_restantes_contador)
        self.senal_aliens_destruidos.emit(self.aliens_destruidos_contador)
        self.contador_primer_nivel += 1
        self.duracion_nivel = int(self.duracion_nivel_anterior * p.PONDERADOR_TUTORIAL)
        self.duracion_nivel_timer = self.duracion_nivel
        self.duracion_nivel_anterior = self.duracion_nivel
        self.contador_primer_nivel_tiempo += 1
