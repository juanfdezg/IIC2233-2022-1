import parametros
from datetime import datetime
from tabulate import tabulate


# Función sacada de AF1
def get_input(op):
    inp = input("Indique su opción: ")
    if inp not in {str(i) for i in range(1, op + 1)}:
        print("\nDebes ingresar una opción válida.\n")
        inp = get_input(op)
    return str(inp)


# Función con la misma finalidad que la anterior, pero esta si acepta el input "0". Se utiliza en
# la función actualizar_encomiendas()
def get_input2(op):
    inp = input("Indique su opción: ")
    if inp not in {str(i) for i in range(op)}:
        print("\nDebes ingresar una opción válida.\n")
        inp = get_input2(op)
    return str(inp)


# Función que recibe un string y revisa si contiene algún tilde
def revisar_tildes(str):
    if ("á" in str) or ("Á" in str):
        return True
    if ("é" in str) or ("É" in str):
        return True
    if ("í" in str) or ("Í" in str):
        return True
    if ("ó" in str) or ("Ó" in str):
        return True
    if ("ú" in str) or ("Ú" in str):
        return True
    return False


# Función que crea un diccionario donde las keys son los nombres de usario y los values sus claves
def crear_diccionario_usuarios():
    dict_usuarios = {}
    with open("usuarios.csv", "r", encoding="utf-8") as usuarios:
        next(usuarios)
        for linea in usuarios:
            linea = linea.strip().split(",")
            dict_usuarios[linea[0]] = linea[1]
    return dict_usuarios


# Función que recibe un nombre de usuario y contraseña, verifica que existan correctamente
# en 'usuarios.csv'
def verificar_usuario(nombre_usuario, contraseña_usuario):
    dict_usuarios = crear_diccionario_usuarios()
    datos_correctos = True

    if nombre_usuario not in dict_usuarios.keys():
        print("\n Usuario incorrecto")
        datos_correctos = False
    elif contraseña_usuario != dict_usuarios[nombre_usuario]:
        print("\n Contraseña incorrecta")
        datos_correctos = False
    return datos_correctos


# Función que define si se continua o cancela la encomienda, se utiliza en ingresar_encomiendas()
def continuar_cancelar_encomienda():
    print("[1] Continuar\n[2] Cancelar encomienda\n")
    opcion_elegida = get_input(2)
    if opcion_elegida == "1":
        continuar = True
    elif opcion_elegida == "2":
        continuar = False
    return continuar


# Función que define si se continua o cancela el registro de un nuevo usuario, se utiliza
# en registrar_usuario
def continuar_cancelar_usuario():
    print(" [1] Reintentar con otro nombre de usuario\n [2] Volver al menú\n")
    opcion_elegida = get_input(2)
    if opcion_elegida == "1":
        continuar = True
    elif opcion_elegida == "2":
        continuar = False
    return continuar


# Función que recibe un nombre de usuario y una lista de encomiendas, permite ingresar encomiendas
# y guardarlas en 'encomiendas.csv'. La lista de encomiendas recibida se utiliza para almacenar las
# encomiendas hechas por el usuario en su sesión actual
def ingresar_encomiendas(nombre_usuario, lista_encomiendas_usuario):
    lista_encomiendas_usuario = lista_encomiendas_usuario
    print("* Ingresa los datos de tu encomienda a continuación *\n")
    nombre_articulo = input("- Nombre del artículo: ")
    nombre_con_comas = "," in nombre_articulo
    while nombre_con_comas:
        print("\n¡Dato ingresado en Nombre incumple las políticas! Desea:\n")
        continuar = continuar_cancelar_encomienda()
        if continuar:
            nombre_articulo = input("\n- Reingresar Nombre del artículo: ")
            nombre_con_comas = "," in nombre_articulo
        else:
            nombre_con_comas = False
            return True

    nombre_destinatario = input("- Nombre del destinatario: ")
    usuarios = crear_diccionario_usuarios()
    while nombre_destinatario not in usuarios.keys():
        print(
            "\n¡Dato ingresado en Nombre del destinatario incumple las políticas! Desea:\n"
        )
        continuar = continuar_cancelar_encomienda()
        if continuar:
            nombre_destinatario = input("\n- Reingresar Nombre del destinatario: ")
        else:
            return True

    peso_encomienda = float(input("- Peso (kg): "))
    peso_superado = peso_encomienda > parametros.MAX_PESO

    while peso_superado:
        print(
            f"\n¡Dato ingresado en Peso incumple las políticas, no puede superar los \
{parametros.MAX_PESO} kilos! Desea:\n"
        )
        continuar = continuar_cancelar_encomienda()
        if continuar:
            peso_encomienda = float(input("\n- Reingresar Peso (kg): "))
            peso_superado = peso_encomienda > parametros.MAX_PESO
        else:
            peso_superado = False
            return True

    destino = input("- Destino: ")
    destino_con_comas = "," in destino
    while destino_con_comas:
        print("\n¡Dato ingresado en Destino incumple las políticas! Desea:\n")
        continuar = continuar_cancelar_encomienda()
        if continuar:
            destino = input("\n- Reingresar Destino del artículo: ")
            destino_con_comas = "," in destino
        else:
            destino_con_comas = False
            return True
    fecha = datetime.now().strftime("%Y/%m/%d %H:%M:%S")  # citar
    datos_encomienda = (
        f"\n{nombre_articulo},{nombre_destinatario},{peso_encomienda},{destino},\
{fecha}"
        + ",Emitida"
    )
    datos_para_revisar = (
        nombre_usuario
        + ","
        + (datos_encomienda.strip().split(","))[0]
        + ","
        + (datos_encomienda.strip().split(","))[5]
    )

    lista_encomiendas_usuario.append(datos_para_revisar)
    with open("encomiendas.csv", "a", encoding="utf-8") as encomiendas:
        encomiendas.write(datos_encomienda)
    print("\n¡Registro exitoso de encomienda!\n")

    return False


# Función que permite registrar un nuevo usuario junto a su contraseña y guardar estos datos
# en 'usuarios.csv'
def registrar_usuario():
    continuar = False
    print("\n- Ingrese sus datos para registrarse -\n")
    nombre_usuario = input(" Indique su nombre de usuario deseado: ")
    while len(nombre_usuario) < parametros.MIN_CARACTERES:
        print(
            "\n ¡El nombre de usuario debe tener mínimo "
            + str(parametros.MIN_CARACTERES)
            + " caracteres!\n"
        )
        continuar = continuar_cancelar_usuario()
        if continuar:
            nombre_usuario = input("\n Indique su nombre de usuario deseado: ")
        else:
            return True
    nombre_alfabetico = nombre_usuario.isalpha()
    nombre_con_tildes = revisar_tildes(nombre_usuario)
    while (not nombre_alfabetico) or (nombre_con_tildes):
        print(
            "\n ¡El nombre de usuario solo debe contener caracteres alfabeticos y sin tildes!\n"
        )
        continuar = continuar_cancelar_usuario()
        if continuar:
            nombre_usuario = input("\n Indique su nombre de usuario deseado: ")
        else:
            return True
        nombre_alfabetico = nombre_usuario.isalpha()
        nombre_con_tildes = revisar_tildes(nombre_usuario)

    usuarios = crear_diccionario_usuarios()
    while nombre_usuario in usuarios.keys():
        print("\n ¡Este usuario ya existe! Desea:\n")
        continuar = continuar_cancelar_usuario()
        if continuar:
            nombre_usuario = input("\n Indique su nombre de usuario deseado: ")
        else:
            return True
    print("\n¡Usuario disponible!\n")
    contraseña_usuario = input(" Indique su contraseña deseada: ")
    contraseña_alfanumerica = contraseña_usuario.isalnum()
    contraseña_con_tildes = revisar_tildes(contraseña_usuario)
    while (
        (len(contraseña_usuario) < parametros.LARGO_CONTRASENA)
        or (not contraseña_alfanumerica)
        or (contraseña_con_tildes)
    ):
        print(
            "\n ¡La contraseña debe tener mínimo "
            + str(parametros.LARGO_CONTRASENA)
            + " caracteres alfanuméricos sin tildes!"
        )
        print("\n [1] Reintentar con otra contraseña\n [2] Volver al menú\n")
        opcion_elegida = get_input(2)
        if opcion_elegida == "1":
            continuar = True
        elif opcion_elegida == "2":
            continuar = False

        if continuar:
            contraseña_usuario = input("\n Indique su contraseña deseada: ")
            contraseña_alfanumerica = contraseña_usuario.isalnum()
            contraseña_con_tildes = revisar_tildes(contraseña_usuario)

        else:
            return True

    datos_usuario = f"\n{nombre_usuario},{contraseña_usuario}"
    with open("usuarios.csv", "a", encoding="utf-8") as usuarios:
        usuarios.write(datos_usuario)
    print("\n¡Usuario registrado exitosamente!")

    return nombre_usuario


# Función que recibe el nombre de usuario en sesión y permite realizar un reclamo, almacenándolo
# en 'reclamos.csv'
def realizar_reclamo(nombre_usuario):
    reclamo = print(
        "\nPara realizar un reclamo, por favor completar los siguientes casilleros: \n"
    )
    titulo_reclamo = input("Título de reclamo: ")
    titulo_reclamo_comas = "," in titulo_reclamo
    while titulo_reclamo_comas:
        print("\n¡El título del reclamo no puede contener comas (,)!\n")
        print(" [1] Reintentar con otro título\n [2] Volver al menú\n")
        opcion_elegida = get_input(2)
        if opcion_elegida == "1":
            continuar = True
        elif opcion_elegida == "2":
            continuar = False
        if continuar:
            titulo_reclamo = input("\n Título de reclamo: ")
            titulo_reclamo_comas = "," in titulo_reclamo
        else:
            return True

    descripcion_reclamo = input("Descripción del reclamo: ")
    datos_reclamo = f"\n{nombre_usuario},{titulo_reclamo},{descripcion_reclamo}"
    with open("reclamos.csv", "a", encoding="utf-8") as reclamos:
        reclamos.write(datos_reclamo)
    print("\n¡Reclamo ingresado correctamente!\n")

    return True


# Función que permite que el administrador revise los reclamos hechos
def revisar_reclamos():
    lista_reclamos = []
    with open("reclamos.csv", "r", encoding="utf-8") as reclamos:
        next(reclamos)
        for linea in reclamos:
            linea = linea.strip().split(",", 2)
            reclamo_lista = [linea[1], linea[2]]
            lista_reclamos.append(reclamo_lista)
    print("\n** Buzón de Reclamos **\n")
    print("* Elija uno de los siguientes reclamos para visualizar su descripción *\n")

    for numero in range(len(lista_reclamos)):
        print(f"[{numero + 1}] {lista_reclamos[numero][0]}")
    print(f"\n[{len(lista_reclamos) + 1}] Volver\n")

    respuesta = get_input(len(lista_reclamos) + 1)
    if respuesta == str(len(lista_reclamos) + 1):
        return True
    else:
        print("\n* Reclamo *\n")
        print(f"-Título: {lista_reclamos[int(respuesta) - 1][0]}")
        print(f"-Descripción: {lista_reclamos[int(respuesta) - 1][1]}\n")

    print("\n [1] Visualizar otro reclamo\n [2] Volver al menú anterior\n")
    visualizar_o_volver = get_input(2)
    if visualizar_o_volver == "1":
        revisar_reclamos()
    if visualizar_o_volver == "2":
        return True

    return True


# Función que permite que el usuario revise el estado de sus encomiendas hechas en
# su sesión actual
def revisar_estado_encomiendas(nombre_usuario, lista_encomiendas_usuario):
    encomiendas_hechas = True
    if len(lista_encomiendas_usuario) == 0:
        encomiendas_hechas = False
    if not encomiendas_hechas:
        print("\n*No tienes encomiendas realizadas en la sesión actual*")
        print("\n [1] Volver\n")
        respuesta = get_input(1)
        if respuesta == "1":
            return True

    print("\n")
    for linea in lista_encomiendas_usuario:
        linea = linea.strip().split(",")
        print(f"Nombre artículo: {linea[1]}\nEstado: {linea[2]}\n")
    print("\n [1] Volver\n")
    respuesta = get_input(1)
    if respuesta == "1":
        return True


# Función que permite al usuario revisar las encomiendas que lo tienen a él como destinatario
def ver_estado_pedidos(nombre_usuario):
    pedidos_hechos = False
    with open("encomiendas.csv", "r", encoding="utf-8") as encomiendas:
        next(encomiendas)
        for linea in encomiendas:
            linea = linea.strip().split(",")
            if linea[1] == nombre_usuario:
                print(
                    f"\nDestinatario: {linea[1]}\nNombre artículo: {linea[0]}\n\
Peso: {linea[2]}\nDestino: {linea[3]}\nFecha: {linea[4]}\nEstado: {linea[5]} \n"
                )
                pedidos_hechos = True

    if not pedidos_hechos:
        print("\n* No tienes pedidos personales *")
        print("\n [1] Volver\n")
        respuesta = get_input(1)
        if respuesta == "1":
            return True
    print("\n [1] Volver\n")
    respuesta = get_input(1)
    if respuesta == "1":
        return True


# Función que permite al administrador actualizar el estado de las encomiendas
def actualizar_encomiendas():
    lista_encomiendas = []
    with open("encomiendas.csv", "r", encoding="utf-8") as encomiendas:
        next(encomiendas)
        for linea in encomiendas:
            linea = linea.strip().split(",")
            lista_encomiendas.append(linea)

    print("\n* Encomiendas registradas *\n")
    print(
        tabulate(
            lista_encomiendas,
            headers=[
                "Nombre artículo",
                "Receptor",
                "Peso",
                "Destino",
                "Fecha",
                "Estado",
            ],
            showindex=True,
        )
    )

    print(f"\n{len(lista_encomiendas)} *VOLVER*\n")
    opcion_elegida = int(get_input2(len(lista_encomiendas) + 1))  # LARGO LISTA = 16

    if opcion_elegida == len(lista_encomiendas):
        return True

    elif lista_encomiendas[opcion_elegida][5] == "Emitida":
        lista_encomiendas[opcion_elegida][5] = "Revisada por agencia"
        print("\n¡Actualización de encomienda exitosa!\n")

    elif lista_encomiendas[opcion_elegida][5] == "Revisada por agencia":
        lista_encomiendas[opcion_elegida][5] = "En camino"
        print("\n¡Actualización de encomienda exitosa!\n")

    elif lista_encomiendas[opcion_elegida][5] == "En camino":
        lista_encomiendas[opcion_elegida][5] = "Llegada al destino"
        print("\n¡Actualización de encomienda exitosa!\n")

    elif lista_encomiendas[opcion_elegida][5] == "Llegada al destino":
        print("\nOpción inválida\n")

    with open("encomiendas.csv", "w", encoding="utf-8") as encomiendas:
        encomiendas.write("nombre_articulo,receptor,peso,destino,fecha,estado\n")
        for numero in range(len(lista_encomiendas)):
            if numero == len(lista_encomiendas) - 1:
                encomiendas.write(
                    f"{lista_encomiendas[numero][0]},{lista_encomiendas[numero][1]},\
{lista_encomiendas[numero][2]},{lista_encomiendas[numero][3]},{lista_encomiendas[numero][4]},\
{lista_encomiendas[numero][5]}"
                )
            else:
                encomiendas.write(
                    f"{lista_encomiendas[numero][0]},{lista_encomiendas[numero][1]},\
{lista_encomiendas[numero][2]},{lista_encomiendas[numero][3]},{lista_encomiendas[numero][4]},\
{lista_encomiendas[numero][5]}\n"
                )

    # Hacemos esta diferenciación en el print de la última linea de encomiendas para evitar
    # que quede una linea vacía al final por el "\n".
