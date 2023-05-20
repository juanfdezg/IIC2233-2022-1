import funciones
import parametros

def menu_administrador():
    print("\n** Menú de administrador ** \n \n [1] Actualizar encomiendas \n [2] Revisar reclamos\
 \n [3] Cerrar sesión \n")
    opcion_elegida = funciones.get_input(3)

    if opcion_elegida == "1":
        funciones.actualizar_encomiendas()
        menu_administrador()

    if opcion_elegida == "2":
        volver = funciones.revisar_reclamos()
        if volver:
            menu_administrador()

    if opcion_elegida == "3":
        menu_inicio()

def menu_usuario(nombre_usuario, lista_encomiendas_usuario):
    lista_encomiendas_usuario = lista_encomiendas_usuario
    print("\nUsuario actual en sesión: " + nombre_usuario)
    print("\n** Menú de usuario ** \n \n [1] Hacer encomienda \n [2] Revisar estado de encomiendas\
 realizadas \n [3] Realizar reclamos \n [4] Ver el estado de los pedidos personales \n \
[5] Cerrar sesión \n")
    opcion_elegida = funciones.get_input(5)
    if opcion_elegida == "1":
        volver = funciones.ingresar_encomiendas(nombre_usuario, lista_encomiendas_usuario)
        if volver:
            menu_usuario(nombre_usuario, lista_encomiendas_usuario)
        elif not volver:
            menu_usuario(nombre_usuario, lista_encomiendas_usuario)

    if opcion_elegida == "2":
        volver = funciones.revisar_estado_encomiendas(nombre_usuario, lista_encomiendas_usuario)
        if volver:
            menu_usuario(nombre_usuario, lista_encomiendas_usuario)

    if opcion_elegida == "3":
        volver = funciones.realizar_reclamo(nombre_usuario)
        if volver:
            menu_usuario(nombre_usuario, lista_encomiendas_usuario)

    if opcion_elegida == "4":
        volver = funciones.ver_estado_pedidos(nombre_usuario)
        if volver:
            menu_usuario(nombre_usuario, lista_encomiendas_usuario)

    if opcion_elegida == "5":
        menu_inicio()

def menu_inicio():
    lista_encomiendas_usuario = []
    mensaje_menu_inicio = "\n---- Bienvenid@ a DCCorreos de Chile ---- \n \n ** Menú de Inicio **\
    \n\n Selecciona una de las siguientes opciones:\n \n [1] Iniciar sesión como usuario \n [2] \
Registrarse como usuario \n [3] Iniciar sesión como administrador \n [4] Salir del programa \n"
    print(mensaje_menu_inicio)
    opcion_elegida = funciones.get_input(4)

    if opcion_elegida == "1":
        nombre_usuario = input(" Nombre de usuario: ")
        contraseña_usuario = input(" Contraseña: ")
        usuario_registrado = funciones.verificar_usuario(nombre_usuario, contraseña_usuario)
        if usuario_registrado == True:
            print("\nInicio de sesión exitoso")
            menu_usuario(nombre_usuario, lista_encomiendas_usuario)

            #Aquí llamamos a la función "menu_usuario"
        if usuario_registrado == False:
            menu_inicio()

    if opcion_elegida == "2":
        volver = funciones.registrar_usuario()
        if volver is True:
            menu_inicio()
        else:
            menu_usuario(volver, lista_encomiendas_usuario)

    if opcion_elegida == "3":
        contraseña_admin_ingresada = input("\nIngresar contraseña de administrador: ")
        if contraseña_admin_ingresada == parametros.CONTRASENA_ADMIN:
            menu_administrador()
        else:
            print("\nContraseña incorrecta")
            menu_inicio()
            
    if opcion_elegida == "4":
        print("\n¡Gracias por utilizar nuestra plataforma!\n")

if __name__ == '__main__':
    menu_inicio()