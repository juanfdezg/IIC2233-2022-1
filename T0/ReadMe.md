# Tarea 0: DCCorreos de Chile   :school_satchel:


## Consideraciones generales :octocat:
Todas las funciones del programa fueron correctamente implementadas, menos una en la que tengo dudas. Para que el programa comience basta con ejecutar el archivo ´´main.py´´. 
La función que me genera dudas en su funcionamiento es [2] Revisar estado de encomiendas, del menú de usuario. En el transcurso de la tarea había creado un archivo de extensión .txt para almacenar el usuario junto a los datos de las encomiendas que este hubiese realizado, para luego poder acceder a esta información en cualquier momento. Sin embargo, me di cuenta que no se podían utilizar archivos externos de esta forma, por lo que busqué otra forma de hacerlo.
No fui capaz de encontrar una forma de guardar la información de la forma en que quería sin utilizar archivos externos .txt  o variables globales. De esta forma, la función finalmente retorna el estado de las encomiendas hechas por el usuario solamente en la sesión actual en que se encuentra, por lo que si cierra sesión e inicia de nuevo, no podrá revisar el estado de las encomiendas hechas en la sesión anterior.
No estoy seguro de qué funcionalidad buscaban en esta parte de la tarea, pero solamente logré implementar la función de la manera en que mencioné anteriormente.
Un error que noté es que si se ingresa un string cuando te piden el Peso al ingresar una encomienda, el programa se cae completamente, no supe solucionar esto.
Me queda poco tiempo para subir el ReadMe pero me acabo de dar cuenta de otro error: puse sin querer dos veces el comando next() en las lineas 302 y 303, el next() de la línea 303 no debiese estar. Esto implica que el usuario Maxy15 no puede ver el estado de su pedido personal con nombre "III Guerra Mundial ilustrada", ya que el código se salta esa línea.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️
#### Menú de Inicio (18pts) (18%)
##### ✅ Requisitos <El menú se llama al iniciar ´´main.py´´ y contiene todas las funciones pedidas. Se ejecuta un print() con todas las opciones y se pide un input. Dependiendo del input entregado, se ejecuta cierta función.>
##### ✅ Iniciar sesión <Se lee el archivo 'usuarios.csv' y se guarda la información en forma de diccionario. De esta forma, al intentar iniciar sesión se revisa este diccionario, para verificar que el usuario exista y su clave sea la correcta, si es que alguna de las condiciones falla, se le informa al usuario y se devuelve al menú de inicio. >
##### ✅ Ingresar como administrador <Se pide un input() para ingresar la clave de administrador, se revisa que el input entregado sea idéntico al parámetro CONTRASEÑA_ADMIN, y si esto se cumple se inicia el menu_administrador. En caso contrario, se le informa al usuario y se devuelve al menú de inicio.\>
##### ✅ Registrar usuario <Se pide un input() para el nombre de usuario deseado y se verifica que cumpla con las condiciones pedidas, además se revisa que este nombre de usuario no exista en el archivo 'usuarios.csv', ya que no se permiten nombres de usuario repetidos. Si alguna condición falla, se le informa al usuario y se le ofrece intentar con un nuevo nombre de usuario, o volver al menú de inicio. Si el nombre de usuario está permitido, se pide un nuevo input() para la contraseña deseada, si es que esta cumple con los requisitos el usuario se registra y se almacena en el archivo 'usuarios.csv'.  A pesar de leer el enunciado y las issues, no me quedó claro si el nombre de usuario podía o no aceptar tildes, por lo que dejé implementado que no puede.\>
##### ✅ Salir <Si el usuario selecciona el input() pedido para "Salir", se finaliza el programa y se imprime un mensaje de despedida. Se finaliza el programa ya que se printea el mensaje y no corre más codigo después de eso.\>
#### Flujo del programa (31pts) (31%) 
##### 🟠 Menú de Usuario <Todas las funciones están bien implementadas y funcionan correctamente, menos la de "Revisar estado de encomiendas". Como mencioné anteriormente, esta función solo muestra las encomiendas hechas por el usuario en la sesión actual en la que se encuentra, por lo que si cierra sesión, esta información se pierde. Es importante considerar que debido a esto, el estado de la encomienda impreso en pantalla siempre va a ser "Emitida", ya que para poder actualizarlo se tendría que cerrar sesión e iniciar como Administrador. Todas las demás funciones funcionan perfectamente, verificando que los inputs cumplan con las condiciones, restándole el momento en que se pide un input() para el Peso de la encomienda. Si se ingresa algún carácter que no sea un número, el programa tira error y no se puede seguir utilizando, en ese caso hay que correrlo de nuevo.\>
##### ✅ Menú de Administrador <Todas las opciones del menú totalmente funcionales. El estado de encomienda se actualiza correctamente y se guarda en el archivo 'encomiendas.csv'. Esto se logró mediante la lectura del archivo, guardando su información en una lista de listas. De esta forma fue más sencillo editar el atributo de "estado" cuando el administrador quisiese cambiarlo. Luego de editarlo en la lista de listas, se procede a reescribir por completo el archivo 'encomiendas.csv' , con la información actualizada. De esta forma, un usuario en sesión luego puede revisar sus pedidos personales con el estado actualizado, ya que esta información se encuentra en el archivo 'encomiendas.csv'.\>
#### Entidades 15pts (15%)
##### ✅ Usuarios <Se diferencia correctamente entre usuario y administrador. Cuando ya has iniciado con algún usuario en el programa, arriba del menú de usuario se muestra el nombre del usuario actual en sesión y las opciones ofrecidas para escoger. Estas opciones no se le muestran al administrador, ya que él tiene sus propias funciones.\>
##### ✅ Encomiendas <La información de las encomiendas se actualiza y guarda correctamente en el archivo 'encomiendas.csv'. No es necesario reiniciar el programa. \>
##### ✅ Reclamos <El archivo 'reclamos.csv' se actualiza correctamente y el administrador puede acceder a esta información de la manera pedida mediante una lista de listas. Se lee el archivo y se guarda la información en una lista de listas, de esta forma el administrador fácilmente puede navegar por los títulos de los reclamos, y escoger alguno para ver su descripción.\>
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos <Se manejan de forma correcta los archivos, respetando el formato original. Tuve un problema constante cuando trabajaba con el archivo 'encomiendas.csv' ya que este archivo se sobrescribía con la información actualizada, y al hacer esto, me quedaba una línea vacía al inicio o al final del archivo. Esto me causaba bastantes problemas luego al intentar ingresar o actualizar una encomienda ya que el formato había cambiado. Finalmente me di cuenta que era muy sencillo de solucionar, diferenciando la última línea de las demás. De esta forma, a la línea final que se iba a escribir en el archivo, le quité el "\n" del final, para evitar esa línea vacía final en el archivo. Cada vez que se abrió un archivo, se procuró utilizar correctamente el encoding = 'utf - 8'. La librería datetime() se utilizó correctamente para indicar la fecha de emisión de las encomiendas.\>
#### General: 21 pts (21%)
##### 🟠 Menús <Él único momento en que el programa se cae es cuando se ingresa un string al input() Peso de las encomiendas, como expliqué anteriormente. A parte de eso, el programa es a prueba de todo tipo de errores.>
##### ✅ Parámetros <Los parámetros se utilizan correctamente en el programa y los módulos se importan correctamente. \>
##### ✅ Módulos <Solamente utilicé 2 diferentes archivos.py para realizar la tarea. En el principal, ´´main.py´´, están definidos los menús de inicio, usuario y administrador, aquí se piden los inputs para decidir la opción elegida. En el otro archivo, ´´funciones.py´´, están definidas todas las funciones para hacer funcional el programa.\>
##### ✅ PEP8 <Se respeta correctamente la guía de estilo y PEP8. \>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```funciones.py``` en ```T0``


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```datetime``` (no recuerdo bien si debe instalarse, creo que no)
2. ```tabulate```: ```tabulate``` (debe instalarse)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones.```: Contiene las funciones necesarias para el correcto funcionamiento de los menús. Funciones tanto para cargar archivos, como para trabajar con ellos.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Al momento de ingresar el nombre de un usuario nuevo al registrarse, el programa no permite tildes. No me quedó claro si se debían aceptar o no, por lo que decidí que no.
-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row>: esto hace que al leer las líneas de un archivo, se salte la primera línea y empiece con la segunda. Esto lo hice para evitar la primera línea de los archivos donde vienen los nombres de los atributos. Está implementado en el archivo <funciones.py> en las líneas 41, 245, 302, 303 y  326.
2. https://stackoverflow.com/questions/16286991/converting-yyyy-mm-dd-hhmmss-date-time: lo utilicé para indicar la fecha de las encomiendas en el formato pedido. Está en la linea 136 en el archivo <funciones.py>.
3. https://stackoverflow.com/questions/14235638/python-split-by-number-of-times-specified lo utilicé en <funciones.py> en la línea 247 para no hacer split(",") a la descripción de los reclamos.

