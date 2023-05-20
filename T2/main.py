import sys

from PyQt5.QtWidgets import QApplication

from backend.logica_principal import LogicaPrincipal
from backend.clases_objetos import Mira
from backend.logica_juego import Juego
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_postnivel import VentanaPostnivel


if __name__ == "__main__":

    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])


# Instanciación de ventanas
ventana_inicio = VentanaInicio()
ventana_principal = VentanaPrincipal()
ventana_juego = VentanaJuego()
ventana_ranking = VentanaRanking()
ventana_postnivel = VentanaPostnivel()

# Instanciación de lógica
logica_principal = LogicaPrincipal()
mira = Mira()
juego = Juego(mira)


# --Conexiónes de señales--

# -VENTANA INICIO-
ventana_inicio.senal_abrir_ventana_principal.connect(ventana_principal.mostrar_ventana)

ventana_inicio.senal_abrir_ventana_ranking.connect(ventana_ranking.mostrar_ventana)

# -VENTANA PRINCIPAL-
ventana_principal.senal_enviar_usuario_nivel.connect(
    logica_principal.comprobar_usuario_nivel
)

# -VENTANA JUEGO-
ventana_juego.senal_tecla.connect(mira.avanzar)

ventana_juego.senal_iniciar_juego.connect(juego.iniciar_juego)

ventana_juego.senal_abrir_ventana_postnivel.connect(ventana_postnivel.mostrar_ventana)

ventana_juego.senal_pausa_juego.connect(juego.pausa)

ventana_juego.senal_pausa_mira.connect(mira.pausar_mira)

ventana_juego.senal_guardar_usuario.connect(juego.almacenar_usuario)

ventana_juego.senal_guardar_puntaje.connect(juego.guardar_puntaje)

ventana_juego.senal_cheatcode_balas.connect(juego.cheatcode_balas)

ventana_juego.senal_cheatcode_nivel.connect(juego.cheatcode_nivel)

ventana_juego.senal_reiniciar_backend.connect(juego.reiniciar_juego)

ventana_juego.senal_reiniciar_frontend.connect(ventana_principal.reiniciar_ventana)

ventana_juego.senal_reiniciar_juego.connect(juego.enviar_senal_nivel)

ventana_juego.senal_volver_ventana_inicio.connect(ventana_inicio.mostrar_ventana)

# -VENTANA POSTNIVEL-
ventana_postnivel.senal_siguiente_nivel.connect(juego.enviar_senal_nivel)

ventana_postnivel.senal_cerrar_juego.connect(ventana_juego.salir)


# -VENTANA RANKING-
ventana_ranking.senal_volver_ventana_inicio.connect(ventana_inicio.mostrar_ventana)


# -LÓGICA PRINCIPAL-
logica_principal.senal_respuesta_validacion.connect(
    ventana_principal.recibir_validacion
)

logica_principal.senal_abrir_ventana_juego.connect(ventana_juego.mostrar_ventana)

# -LÓGICA JUEGO-
juego.senal_aparecer_alien.connect(ventana_juego.agregar_alien)

juego.senal_moverse_alien.connect(ventana_juego.mover_alien)

juego.senal_actualizar_balas_label.connect(ventana_juego.actualizar_balas)

juego.senal_actualizar_puntaje.connect(ventana_juego.actualizar_puntaje)

juego.senal_tiempo_agotado.connect(ventana_juego.abrir_ventana_postnivel)

juego.senal_disparo_efectivo.connect(ventana_juego.desaparecer_alien)

juego.senal_actualizar_tiempo.connect(ventana_juego.actualizar_tiempo)

juego.senal_aparecer_explosion.connect(ventana_juego.aparecer_explosion)

juego.senal_desaparecer_explosion.connect(ventana_juego.desaparecer_explosion)

juego.senal_actualizar_nivel.connect(ventana_juego.actualizar_nivel)

juego.senal_animacion_dog.connect(ventana_juego.mover_dog1)

juego.senal_iniciar_nivel.connect(juego.iniciar_juego)

juego.senal_nivel_superado.connect(ventana_juego.nivel_superado_aparecer)

juego.senal_nivel_superado_desaparecer.connect(ventana_juego.nivel_superado_desaparecer)

juego.senal_ventana_postnivel.connect(ventana_postnivel.mostrar_ventana)

juego.senal_aliens_restantes.connect(ventana_juego.actualizar_aliens_restantes)

juego.senal_aliens_destruidos.connect(ventana_juego.actualizar_aliens_destruidos)

mira.senal_mover_mira.connect(ventana_juego.avanzar_mira)

mira.senal_disparar.connect(ventana_juego.disparar)

mira.senal_mira_original.connect(ventana_juego.mira_original)

mira.senal_restar_bala.connect(juego.restar_balas)

mira.senal_disparo_hecho.connect(juego.chequear_colisiones)

ventana_inicio.show()
app.exec()
