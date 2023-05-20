import random
import parametros as p
import jugadores

class Juego():

    def __init__(self, nombre, esperanza, apuesta_minima, apuesta__maxima, *args, **kwargs):
        self.nombre = nombre
        self.esperanza = int(esperanza)
        self.apuesta_minima = int(apuesta_minima)
        self.apuesta_maxima = int(apuesta__maxima)

    def entregar_resultados(self, jugador, ganar, dinero_apostado):
        valor_energia = round((jugador.ego + jugador.frustracion) * 0.15)
        jugador.energia -= valor_energia
        if ganar:
            jugador.ego += p.EGO_GANAR
            jugador.carisma += p.CARISMA_GANAR
            jugador.frustracion -= p.FRUSTRACION_GANAR
            jugador.dinero += dinero_apostado
            print(f'¡{jugador.nombre} gana la apuesta!\n')
            print(f'{jugador.nombre} aumenta su ego en {p.EGO_GANAR}')
            print(f'{jugador.nombre} aumenta su carisma en {p.CARISMA_GANAR}')
            print(f'{jugador.nombre} disminuye su frustración en {p.FRUSTRACION_GANAR}\n')
            print(f'{jugador.nombre} ha ganado ${dinero_apostado * 2} \
y ahora tiene ${jugador.dinero}\n')
        if not ganar:
            jugador.frustracion += p.FRUSTRACION_PERDER
            jugador.confianza -= p.CONFIANZA_PERDER
            jugador.dinero -= dinero_apostado
            print(f'¡{jugador.nombre} pierde la apuesta!\n')
            print(f'{jugador.nombre} aumenta su frustración en {p.FRUSTRACION_PERDER}')
            print(f'{jugador.nombre} pierde {p.CONFIANZA_PERDER} de confianza...\n')
            print(f'{jugador.nombre} ha perdido ${dinero_apostado} \
y ahora tiene ${jugador.dinero}\n')
        print(f'{jugador.nombre} pierde {valor_energia} de energía...\n')
        print(f'Dinero faltante: ${p.DEUDA_TOTAL - jugador.dinero}\n')

    def probabilidad_de_ganar(self, prob_ganar_jugador, jugador, dinero_apostado):
        if jugador.juego_favorito == self.nombre:
            favorito = int(1)
        else:
            favorito = int(0)
        
        valor = min(1, prob_ganar_jugador - ((dinero_apostado - 
        (favorito * p.MULTIPLICADOR_FAVORITO_PROB_JUEGO - 
        (self.esperanza * p.MULTIPLICADOR_ESPERANZA_PROB_JUEGO)))/p.DIVISOR_PROB_JUEGO))
        if valor < 0:
            valor = 0
    
        return valor

