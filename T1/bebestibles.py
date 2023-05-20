import jugadores
from abc import ABC, abstractmethod
import random
import parametros as p

class Bebestible(ABC):

    def __init__(self, nombre, tipo, precio, *args, **kwargs):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def consumir(self, jugador):
        energia_recuperada = random.randint(p.MIN_ENERGIA_BEBESTIBLE, p.MAX_ENERGIA_BEBESTIBLE)
        if jugador.personalidad == "Bebedor":
            jugador.cliente_recurrente()
            print(f'¡{jugador.nombre} recibe una bonificación en los beneficios de la bebida!\n')
            energia_recuperada = energia_recuperada * p.MULTIPLICADOR_BONIFICACION_BEBEDOR
        jugador.energia += energia_recuperada

    @abstractmethod
    def accion_especial(self, jugador):
        pass

class Jugo(Bebestible):

    def __init__(self, nombre, tipo, precio, *args, **kwargs):
        super().__init__(nombre, tipo, precio, *args, **kwargs)

    def accion_especial(self, jugador):
        if len(self.nombre) <= p.JUGO_LARGO_1:
            if jugador.personalidad == "Bebedor":
                valor_ego = (p.JUGO_EGO_LARGO_1 * p.MULTIPLICADOR_BONIFICACION_BEBEDOR)
            else:
                valor_ego = p.JUGO_EGO_LARGO_1
            jugador.ego += valor_ego
            print(f'Aumenta la energía y el ego...\n')
        elif len(self.nombre) >= p.JUGO_LARGO_2 and len(self.nombre) <= p.JUGO_LARGO_3:
            if jugador.personalidad == "Bebedor":
                valor_suerte = (p.JUGO_SUERTE_LARGO2_3 *p.MULTIPLICADOR_BONIFICACION_BEBEDOR)
            else:
                valor_suerte = p.JUGO_SUERTE_LARGO2_3
            jugador.suerte += valor_suerte
            print(f'Aumenta la energía y la suerte...\n')
        elif len(self.nombre) >= p.JUGO_LARGO_4:
            if jugador.personalidad == "Bebedor":
                valor_frustracion = (p.JUGO_FRUSTRACION_LARGO_4 * 
                p.MULTIPLICADOR_BONIFICACION_BEBEDOR)
                valor_ego = (p.JUGO_EGO__LARGO_4 * p.MULTIPLICADOR_BONIFICACION_BEBEDOR)
            else:
                valor_frustracion = p.JUGO_FRUSTRACION_LARGO_4
                valor_ego = p.JUGO_EGO__LARGO_4
            jugador.frustracion -= valor_frustracion
            jugador.ego += valor_ego
            print(f'Aumenta la energía y el ego y disminuye la frustración...\n')


class Gaseosa(Bebestible):

    def __init__(self, nombre, tipo, precio, *args, **kwargs):
        super().__init__(nombre, tipo, precio, *args, **kwargs)

    def accion_especial(self, jugador):
        if jugador.personalidad == "Ludopata" or jugador.personalidad == "Tacano":
            jugador.frustracion -= p.GASEOSA_FRUSTRACION_TACAÑO_LUDOPATA
            print(f'Aumenta la energía y el ego y disminuye la frustracion...\n')
        elif jugador.personalidad == "Casual":
            jugador.frustracion += p.GASEOSA_FRUSTRACION_BEBEDOR_CASUAL
            print(f'Aumenta la energía, la frustración y el ego...\n')
        elif jugador.personalidad == "Bebedor":
            jugador.frustracion += (p.GASEOSA_FRUSTRACION_BEBEDOR_CASUAL * 
            p.MULTIPLICADOR_BONIFICACION_BEBEDOR)
            print(f'Aumenta la energía, la frustracion y el ego...\n')
        jugador.ego += p.GASEOSA_EGO


class BrebajeMagico(Gaseosa, Jugo):

    def __init__(self, nombre, tipo, precio, *args, **kwargs):
        super().__init__(nombre, tipo, precio, *args, **kwargs)

    def accion_especial(self, jugador):
        Gaseosa.accion_especial(self, jugador)
        Jugo.accion_especial(self, jugador)
        jugador.carisma += p.BREBAJE_MAGICO_CARISMA



