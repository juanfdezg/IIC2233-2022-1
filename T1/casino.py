import jugadores
import bebestibles
import juego
import parametros as p
import random

class Casino():

    def __init__(self, jugador):
        self.jugador = jugador
    
    @property
    def dinero_faltante(self):
        if (p.DEUDA_TOTAL - self.jugador.dinero) >= 0:
            return int((p.DEUDA_TOTAL - self.jugador.dinero))
        else:
            return int(0)
    @property
    def bebestibles(self):
        lista_bebestibles = []
        with open('bebestibles.csv', 'r', encoding='utf-8') as bebestiblescsv:
            header = bebestiblescsv.readline().strip().split(",")
            indice_nombre = header.index('nombre')
            indice_tipo = header.index('tipo')
            indice_precio = header.index('precio')
            for linea in bebestiblescsv:
                linea = linea.strip().split(",")
                nombre = linea[indice_nombre]
                tipo = linea[indice_tipo]
                precio = linea[indice_precio]
                dict_clases_bebestibles = {
            "Jugo": bebestibles.Jugo,
            "Gaseosa": bebestibles.Gaseosa,
            "Brebaje mágico": bebestibles.BrebajeMagico,
        }
                bebestible = dict_clases_bebestibles[tipo](nombre.capitalize(), tipo, precio)
                lista_bebestibles.append(bebestible)
        return lista_bebestibles

    @property
    def juegos(self):
        lista_juegos = []
        with open('juegos.csv', 'r', encoding='utf-8') as juegoscsv:
            header = juegoscsv.readline().strip().split(",")
            indice_nombre = header.index('nombre')
            indice_esperanza = header.index('esperanza')
            indice_apuesta_min = header.index('apuesta minima')
            indice_apuesta_max = header.index('apuesta maxima')
            for linea in juegoscsv:
                linea = linea.strip().split(",")
                nombre = linea[indice_nombre]
                esperanza = linea[indice_esperanza]
                apuesta_minima = linea[indice_apuesta_min]
                apuesta_maxima = linea[indice_apuesta_max]
                juego_objeto = juego.Juego(nombre, esperanza, apuesta_minima, apuesta_maxima)
                lista_juegos.append(juego_objeto)
        return lista_juegos

    def evento_especial(self):
        if random.random() <= p.PROBABILIDAD_EVENTO:
            indice_aleatorio = random.randint(0, len(self.bebestibles) - 1)
            bebestible_evento = self.bebestibles[indice_aleatorio]
            print(f'¡¡¡EVENTO ESPECIAL!!!\n{self.jugador.nombre} recibe el bebestible\
 {bebestible_evento.nombre} gratis!!!\n')
            bebestible_evento.consumir(self.jugador)
            bebestible_evento.accion_especial(self.jugador)
        else:
            print(f'No hay evento especial :(\n')

        

    def jugar(self, juego, dinero_apostado):
        if self.jugador.dinero >= dinero_apostado:
            if dinero_apostado >= juego.apuesta_minima and dinero_apostado <= juego.apuesta_maxima:
                self.jugador.apostar(juego, dinero_apostado)
            else:
                print("\nValor no se encuentra entre los valores establecidos\n")
        else:
            print("\nNo tienes el dinero suficiente para realizar la apuesta\n")
