from unicodedata import name
import parametros as p
import jugadores
import bebestibles
import juego
from casino import Casino


def get_input(op):
    inp = input("Indique su opción: ")
    if inp not in {str(i) for i in range(1, op + 1)}:
        print("\nDebes ingresar una opción válida.\n")
        inp = get_input(op)
    return str(inp)


def get_input2(op):
    inp = input("Indique su opción: ")
    if inp not in {str(i) for i in range(op)}:
        print("\nDebes ingresar una opción válida.\n")
        inp = get_input2(op)
    return str(inp)


def menu_inicio():
    print(
        "\n*** Menú de inicio *** \n----------------------\n[1] Iniciar partida \n[2] Salir\n"
    )
    opcion_elegida1 = get_input(2)
    dict_clases_jugadores = {
        "Ludopata": jugadores.Ludopata,
        "Tacano": jugadores.Tacaño,
        "Bebedor": jugadores.Bebedor,
        "Casual": jugadores.Casual,
    }
    if opcion_elegida1 == "1":
        lista_jugadores = []
        with open("jugadores.csv", "r", encoding="utf-8") as jugadorescsv:
            header = jugadorescsv.readline().strip().split(",")
            indice_nombre = header.index("nombre")
            indice_personalidad = header.index("personalidad")
            indice_energia = header.index("energia")
            indice_suerte = header.index("suerte")
            indice_dinero = header.index("dinero")
            indice_frustracion = header.index("frustracion")
            indice_ego = header.index("ego")
            indice_carisma = header.index("carisma")
            indice_confianza = header.index("confianza")
            indice_juego_favorito = header.index("juego favorito")
            for linea in jugadorescsv:
                linea = linea.strip().split(",")
                nombre = linea[indice_nombre]
                personalidad = linea[indice_personalidad]
                energia = int(linea[indice_energia])

                suerte = int(linea[indice_suerte])
                dinero = int(linea[indice_dinero])
                frustracion = int(linea[indice_frustracion])
                ego = int(linea[indice_ego])
                carisma = int(linea[indice_carisma])
                confianza = int(linea[indice_confianza])
                juego_favorito = linea[indice_juego_favorito]

                jugador_objeto = dict_clases_jugadores[personalidad](
                    nombre,
                    energia,
                    suerte,
                    dinero,
                    frustracion,
                    ego,
                    carisma,
                    confianza,
                    juego_favorito,
                )
                lista_jugadores.append(jugador_objeto)

        print("\n  *** Opciones de Jugador ***   \n------------------------------")
        for i in range(len(lista_jugadores)):
            print(
                f"[{i + 1}] {lista_jugadores[i].nombre}: {lista_jugadores[i].personalidad}"
            )

        print(
            f"\n[{len(lista_jugadores) + 1}] Volver\n[{len(lista_jugadores) + 2}] Salir"
        )
        opcion_elegida2 = int(get_input(len(lista_jugadores) + 2))

        if opcion_elegida2 <= len(lista_jugadores):
            jugador = lista_jugadores[opcion_elegida2 - 1]
            menu_principal(jugador)
        elif opcion_elegida2 == len(lista_jugadores) + 1:
            menu_inicio()
        elif opcion_elegida2 == len(lista_jugadores) + 2:
            print("\nHAS SALIDO DEL DCCASINO\n")

    elif opcion_elegida1 == "2":
        print("\nHAS SALIDO DEL DCCASINO\n")


def menu_principal(jugador):
    seguir = True
    opcion_elegida = "0"
    casinito = Casino(jugador)
    if casinito.dinero_faltante == 0:
        seguir = False
        print("\nHAS SALDADO TU CUENTA CON BIGCAT:)\n")
    if jugador.dinero == 0:
        seguir = False
        print("\nTE HAS QUEDADO SIN DINERO :(\n")

    if seguir:
        print("\n  *** Menú Principal ***\n--------------------------")
        print(f"¡Bienvenido {jugador.nombre}!\n")
        print(
            "[1] Opciones de juegos \n[2] Comprar bebestible \n[3] Habilidades jugador \n[4] \
Volver \n[5] Salir\n"
        )

        opcion_elegida = get_input(5)
    if opcion_elegida == "1" and seguir:
        print("\n   *** Opciones de Juegos ***\n--------------------------------\n")
        for i in range(len(casinito.juegos)):
            print(f"[{i + 1}] {casinito.juegos[i].nombre.capitalize()}")
        print(
            f"\n[{len(casinito.juegos) + 1}] Volver\n[{len(casinito.juegos) + 2}] Salir\n"
        )

        opcion_elegida2 = get_input(len(casinito.juegos) + 2)
        if opcion_elegida2 == str(len(casinito.juegos) + 1):
            menu_principal(jugador)
        elif opcion_elegida2 == str(len(casinito.juegos) + 2):
            print("\nHAS SALIDO DEL DCCASINO\n")
        else:
            dinero_apostado = int(input("\nIngrese la cantidad a apostar: "))
            dinero_antes_apuesta = jugador.dinero
            casinito.jugar(casinito.juegos[int(opcion_elegida2) - 1], dinero_apostado)
            dinero_despues_apuesta = jugador.dinero
            if dinero_antes_apuesta != dinero_despues_apuesta:
                casinito.evento_especial()
            menu_principal(jugador)

    if opcion_elegida == "2" and seguir:
        print("\n  *** Bebestibles ***\n-------------------------")
        print("N°  |  Nombre   |  Tipo   |   Precio")
        for i in range(len(casinito.bebestibles)):
            print(
                f"[{i}] {casinito.bebestibles[i].nombre}    {casinito.bebestibles[i].tipo}     \
{casinito.bebestibles[i].precio}"
            )
        print(
            f"\n[{len(casinito.bebestibles)}] VOLVER\n[{len(casinito.bebestibles) + 1}] SALIR\n"
        )

        opcion_elegida3 = int(get_input2(len(casinito.bebestibles) + 2))
        if opcion_elegida3 == len(casinito.bebestibles):
            menu_principal(jugador)
        elif opcion_elegida3 == (len(casinito.bebestibles) + 1):
            print("\nHAS SALIDO DEL DCCASINO\n")
        else:
            bebestible = casinito.bebestibles[opcion_elegida3]

            if jugador.dinero >= int(bebestible.precio):
                jugador.comprar_bebestible(bebestible)
                menu_principal(jugador)

            else:
                print(
                    f"\nNo tienes el dinero suficiente para comprar {bebestible.nombre}\n"
                )
                menu_principal(jugador)

    if opcion_elegida == "3" and seguir:
        print(
            "\n   *** Ver estado del Jugador ***\n------------------------------------\n"
        )
        print(
            f"Nombre: {jugador.nombre}\nPersonalidad: {jugador.personalidad}\nEnergía: \
{jugador.energia}\nSuerte: {jugador.suerte}\nDinero: ${jugador.dinero}\nFrustración: \
{jugador.frustracion}\nEgo: {jugador.ego}\nCarisma: {jugador.carisma}\nConfianza: \
{jugador.confianza}\nJuego favorito: {jugador.juego_favorito}\nDinero faltante: \
${p.DEUDA_TOTAL - jugador.dinero}"
        )
        print("\n[0] Volver\n[1] Salir\n")
        opcion_elegida4 = get_input2(2)
        if opcion_elegida4 == "0":
            menu_principal(jugador)
        elif opcion_elegida4 == "1":
            print("\nHAS SALIDO DEL DCCASINO\n")
    if opcion_elegida == "4" and seguir:
        menu_inicio()
    if opcion_elegida == "5" and seguir:
        print("\nHAS SALIDO DEL DCCASINO\n")


if __name__ == "__main__":
    menu_inicio()
