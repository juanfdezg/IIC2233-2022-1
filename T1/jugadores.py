from abc import ABC, abstractmethod
import random
import parametros as p

#Creamos la clase abstracta Jugador

class Jugador(ABC):
    def __init__(self, nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
    juego_favorito, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.__energia = int(energia)
        self.__suerte = int(suerte)
        self.__dinero = int(dinero)
        self.__frustracion = int(frustracion)
        self.__ego = int(ego)
        self.__carisma = int(carisma)
        self.__confianza = int(confianza)
        self.juego_favorito = juego_favorito
        self.juegos_jugados = 0

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        if valor > p.MAX_ENERGIA_JUGADOR:
            self.__energia = p.MAX_ENERGIA_JUGADOR
        elif valor < p.MIN_ENERGIA_JUGADOR:
            self.__energia = p.MIN_ENERGIA_JUGADOR
        else:
            self.__energia = valor

    @property
    def suerte(self):
        return self.__suerte
    
    @suerte.setter
    def suerte(self, valor):
        if valor > p.MAX_SUERTE_JUGADOR:
            self.__suerte = p.MAX_SUERTE_JUGADOR
        elif valor < p.MIN_SUERTE_JUGADOR:
            self.__suerte = p.MIN_SUERTE_JUGADOR
        else:
            self.__suerte = valor

    @property
    def dinero(self):
        return self.__dinero
    
    @dinero.setter
    def dinero(self, valor):
        if valor < 0:
            self.__dinero = 0
        else:
            self.__dinero = valor

    @property
    def frustracion(self):
        return self.__frustracion
    
    @frustracion.setter
    def frustracion(self, valor):
        if valor > p.MAX_FRUSTRACION_JUGADOR:
            self.__frustracion = p.MAX_FRUSTRACION_JUGADOR
        elif valor < p.MIN_FRUSTRACION_JUGADOR:
            self.__frustracion = p.MIN_FRUSTRACION_JUGADOR
        else:
            self.__frustracion = valor
    
    @property
    def ego(self):
        return self.__ego
    
    @ego.setter
    def ego(self, valor):
        if valor > p.MAX_EGO_JUGADOR:
            self.__ego = p.MAX_EGO_JUGADOR
        elif valor < p.MIN_EGO_JUGADOR:
            self.__ego = p.MIN_EGO_JUGADOR
        else:
            self.__ego = valor

    @property
    def carisma(self):
        return self.__carisma
    
    @carisma.setter
    def carisma(self, valor):
        if valor > p.MAX_CARISMA_JUGADOR:
            self.__carisma = p.MAX_CARISMA_JUGADOR
        elif valor < p.MIN_CARISMA_JUGADOR:
            self.__carisma = p.MIN_CARISMA_JUGADOR
        else:
            self.__carisma = valor

    @property
    def confianza(self):
        return self.__confianza
    
    @confianza.setter
    def confianza(self, valor):
        if valor > p.MAX_CONFIANZA_JUGADOR:
            self.__confianza = p.MAX_CONFIANZA_JUGADOR
        elif valor < p.MIN_CONFIANZA_JUGADOR:
            self.__confianza = p.MIN_CONFIANZA_JUGADOR
        else:
            self.__confianza = valor

    
    def comprar_bebestible(self, bebestible):
        self.dinero -= int(bebestible.precio)
        bebestible.consumir(self)
        bebestible.accion_especial(self)

        
    
    @abstractmethod
    def apostar(self, juego, dinero_apostado):
        pass

    def probabilidad_ganar_jugador(self, juego, dinero_apostado):
        if self.juego_favorito == juego.nombre:
            favorito = int(1)
        else:
            favorito = int(0)
        valor = min(1, max(0, ((self.suerte * p.MULTIPLICADOR_SUERTE_PROB_JUGADOR) - 
        (dinero_apostado * p.MULTIPLICADOR_APUESTA_PROB_JUGADOR) + 
        (self.confianza * p.MULTIPLICADOR_CONFIANZA_PROB_JUGADOR * favorito) + 
        (self.carisma * p.MULTIPLICADOR_CARISMA_PROB_JUGADOR))/p.DIVISOR_PROB_JUGADOR))
        
        return valor






class Ludopata(Jugador):

    def __init__(self, nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
    juego_favorito, *args, **kwargs):
        self.personalidad = "Ludopata"
        super().__init__(nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
        juego_favorito, *args, **kwargs)

    def ludopatia(self, ganar):
        print("Aplicando efectos de ser un jugador ludópata...")
        print("Aumenta el ego y la suerte...\n")
        self.ego += 2
        self.suerte +=3
        if not ganar:
            self.frustracion += 5

    def apostar(self, juego, dinero_apostado):
        prob_ganar_jugador = self.probabilidad_ganar_jugador(juego, dinero_apostado)
        probabilidad_de_ganar = juego.probabilidad_de_ganar(prob_ganar_jugador,self, 
        dinero_apostado)
        print(f'\nLa probabilidad de ganar es: {probabilidad_de_ganar}\n')
        
        if random.random() <= probabilidad_de_ganar:
            ganar = True
        else:
            ganar = False

        juego.entregar_resultados(self, ganar, dinero_apostado)
        self.ludopatia(ganar)


    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)





class Tacaño(Jugador):

    def __init__(self, nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
    juego_favorito, *args, **kwargs):
        self.personalidad = "Tacano"
        super().__init__(nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
        juego_favorito, *args, **kwargs)

    def tacano_extremo(self, ganar, dinero_apostado):
        if ganar:
            if dinero_apostado < (p.PORCENTAJE_APUESTA_TACAÑO * self.dinero):
                print("\nAplicando efectos de ser un jugador tacaño...")
                self.dinero += p.BONIFICACION_TACAÑO
                print(f'!{self.nombre} recibe una bonificación de ${p.BONIFICACION_TACAÑO} y \
ahora tiene {self.dinero}!\n')

    def apostar(self, juego, dinero_apostado):
        prob_ganar_jugador = self.probabilidad_ganar_jugador(juego, dinero_apostado)
        probabilidad_de_ganar = juego.probabilidad_de_ganar(prob_ganar_jugador,self,
         dinero_apostado)
        print(f'\nLa probabilidad de ganar es: {probabilidad_de_ganar}\n')
        
        if random.random() <= probabilidad_de_ganar:
            ganar = True
        else:
            ganar = False
        
        juego.entregar_resultados(self, ganar, dinero_apostado)
        self.tacano_extremo(ganar, dinero_apostado)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)





class Bebedor(Jugador):

    def __init__(self, nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
    juego_favorito, *args, **kwargs):
        self.personalidad = "Bebedor"
        super().__init__(nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
        juego_favorito, *args, **kwargs)

    def apostar(self, juego, dinero_apostado):
        prob_ganar_jugador = self.probabilidad_ganar_jugador(juego, dinero_apostado)
        probabilidad_de_ganar = juego.probabilidad_de_ganar(prob_ganar_jugador,self, 
        dinero_apostado)
        print(f'\nLa probabilidad de ganar es: {probabilidad_de_ganar}\n')
        if random.random() <= probabilidad_de_ganar:
            ganar = True
        else:
            ganar = False
        
        juego.entregar_resultados(self, ganar, dinero_apostado)

    def cliente_recurrente(self):
        print("\nAplicando efectos de ser un jugador bebedor...")
        pass

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)





class Casual(Jugador):

    def __init__(self, nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza, 
    juego_favorito, *args, **kwargs):
        self.personalidad = "Casual"
        super().__init__(nombre, energia, suerte, dinero, frustracion, ego, carisma, confianza,
         juego_favorito, *args, **kwargs)

    def suerte_principiante(self, juegos_jugados):
        print("\nAplicando efectos de ser un jugador casual...")
        if juegos_jugados == 0:
            self.suerte += p.BONIFICACION_SUERTE_CASUAL
            print(f'\n¡La suerte de {self.nombre} ha aumentado en\
 {p.BONIFICACION_SUERTE_CASUAL}!\n')

    def apostar(self, juego, dinero_apostado):
        self.suerte_principiante(self.juegos_jugados)
        prob_ganar_jugador = self.probabilidad_ganar_jugador(juego, dinero_apostado)
        probabilidad_de_ganar = juego.probabilidad_de_ganar(prob_ganar_jugador,self, 
        dinero_apostado)
        print(f'\nLa probabilidad de ganar es: {probabilidad_de_ganar}\n')
        
        if random.random() <= probabilidad_de_ganar:
            ganar = True
        else:
            ganar = False
        
        juego.entregar_resultados(self, ganar, dinero_apostado)
        self.juegos_jugados += 1

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)






