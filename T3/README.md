# Tarea 3: DCCasillas :school_satchel:

## Consideraciones generales :octocat:

Para que el programa comience basta con ejecutar los archivos main.py de las carpetas servidor y cliente por separado, en consolas distintas.  El servidor y los clientes se logran conectar de forma correcta, interactuando entre si mediante mensajes encriptados y codificados como se pedía en el enunciado. Se utilizó 'localhost' para el servidor. El programa funciona de mejor manera si los clientes se conectan de a uno a la sala de espera, es decir, se ejecuta el archivo main.py del cliente en la consola, se ingresa un nombre de usuario y entra en la sala de espera. Luego se abre otra consola, se ejecuta main.py, el cliente entra a la sala de espera, etc... De todas formas, el programa también funciona si es que se ejecutan los 4 clientes primero con su archivo main.py, y luego cada uno ingresa a la sala de espera, sin embargo, haciéndolo de esta manera aparecen ciertos bugs o errores en casos muy específicos, los cuales no supe identificar bien. Los clientes nunca se comunican directamente entre sí, el servidor siempre es el intermediario. Logré implementar correctamente la ventana de inicio, donde se puede ingresar a la ventana de espera solo si es que se ingresa un nombre de usuario que cumpla con el formato pedido, que no se repita con un nombre de usuario ya existente, y que la sala no esté llena (4 jugadores máximo). Tampoco te deja entrar a la sala de espera si es que ya hay una partida/juego en proceso.
La sala de espera funciona correctamente, a medida que los clientes se van conectando e ingresando a la sala, la interfaz se va actualizando para todos los clientes, mostrando todos los jugadores en la sala. De la misma manera, si se desconecta un cliente, se le retira de la sala de espera y la interfaz de los demás clientes se actualiza también, quitando al jugador que se desconectó. Solamente el administrador puede iniciar la partida, el cual corresponde al primer jugador en entrar, y si es que hay un mínimo de 2 jugadores. La sala de espera puede tener un máximo de 4 jugadores, si otro jugador intenta entrar no se le permite. El orden en que se les designan los colores a los jugadores siempre es el mismo, el primer jugador es azul, el segundo es verde, el tercero amarillo y el cuarto es rojo.
Por temas de tiempo no logré implementar las funciones pedidas en el juego. Sin embargo, cree la ventana de juego donde se muestran los jugadores en partida, y sus fichas correspondientes. Solamente se muestran las fichas de los jugadores conectados. También hice funcional el botón de tirar el dado, mostrando un valor aleatorio entre 1 y 3, luego de tirar el dado se pasa al turno del siguiente jugador, mostrándolo en pantalla. Si bien todo esto está implementado, no alcancé a programar los movimientos de las fichas ni más. Por lo tanto, no existe Ventana Final.
La encriptación, desencriptación, codificación y decodificación fueron implementados correctamente. Si es que se cierra el servidor, se les notifica a los clientes, y después de 3 segundos se cierran sus ventanas.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Networking: 23 pts (18%)
##### ✅ Protocolo <Se aplica un correcto uso de TCP/IP.\>
##### ✅ Correcto uso de sockets <Se instancian y conectan correctamente los sockets, en donde varios clientes pueden trabajar al mismo tiempo sin bloquearse.\>
##### ✅ Conexión <La conexión perdura durante el tiempo y sirve para mandar mensajes con cualquier propósito.\>
##### 🟠 Manejo de clientes <Se pueden conectar y desconectar clientes de manera correcta. Hay casos muy específicos en los que se genera un error, pero no supe identificar bien cuándo ocurre.\>
#### Arquitectura Cliente - Servidor: 31 pts (25%)
##### ✅ Roles <Roles bien definidos. El servidor realiza toda la lógica del programa, recibe mensajes del cliente, los procesa,  y le envía una respuesta. Las responsabilidades son consistentes con el enunciado.\>
##### 🟠 Consistencia <La información se mantiene actualizada en todos los clientes y en el servidor. Si no me equivoco, no utilicé locks.\>
##### ✅ Logs <Se implementan los logs correctamente.\>
#### Manejo de Bytes: 26 pts (21%)
##### ✅ Codificación <La codificación se implementa correctamente, cumpliendo detalladamente con lo pedido en el enunciado.\>
##### ✅ Decodificación <La decodificación se implementa correctamente, cumpliendo detalladamente con lo pedido en el enunciado.\>
##### ✅ Encriptación <La encriptación se implementa correctamente, cumpliendo detalladamente con lo pedido en el enunciado.\>
##### ✅ Desencriptación <La desencriptación se implementa correctamente, cumpliendo detalladamente con lo pedido en el enunciado.\>
##### ✅ Integración <Se utiliza correctamente el protocolo pedido para envíar mensajes.\>
#### Interfaz: 23 pts (18%)
##### ✅ Ventana inicio <Se visualizan correctamente los elementos solicitados, un usuario solo puede entrar si su nombre cumple con los requisitos del enunciado, y si es que la sala no está llena y no hay una partida en proceso.\>
##### 🟠 Sala de Espera <Se visualizan y actualizan correctamente los elementos de la ventana. Sin embargo, el juego no inicia automáticamente si es que hay 4 jugadores, hay que presionar el botón de iniciar partida manualmente.\>
##### 🟠 Sala de juego <Se visualizan correctamente la mayoría de los elementos. Al tirar el dado se genera un número aleatorio entre 1 y 3 se pasa al siguiente turno, esto es visible para todos los clientes. No existe movimiento de las fichas ni un ganador.\>
##### ❌ Ventana final <No fue implementada.\>
#### Reglas de DCCasillas: 18 pts (14%)
##### 🟠 Inicio del juego <Se le asignan correctamente los turnos a los jugadores segun su orden de llegada, sin embargo los colores no se entregan de manera aleatoria, siempre se sigue un orden preestablecido.\>
##### 🟠 Ronda <Se puede tirar el dado y los turnos pasan correctamente visualmente, sin embargo cualquier jugador puede tirar del dado en cualquier momento. El movimiento de las fichas y el juego en sí no fue implementado.\>
##### ❌ Termino del juego <No fue implementado.\>
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON) <Los parámetros se encuentran en los archivos parametros.json y se utilizan correctamente.\>
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode <No fue implementado.\>
##### ❌ Turnos con tiempo <No fue implementado.\>
##### ❌ Rebote <No fue implementado.\>

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` de las carpetas servidor y cliente. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```cliente.py``` en ```cliente/backend```
2. ```funciones.py``` en ```cliente/backend```
3. ```interfaz.py``` en ```cliente/backend```
4. ```ventana_inicio.py``` en ```cliente/frontend```
5. ```ventana_espera.py``` en ```cliente/frontend```
6. ```ventana_juego.py``` en ```cliente/frontend```
7. ```ventana_inicio.ui``` en ```cliente/frontend```
8. ```ventana_espera.ui``` en ```cliente/frontend```
9. ```ventana_juego.ui``` en ```cliente/frontend```
10. ```parametros.json``` en ```cliente/```
11. ```utils.py``` en ```cliente/```
12. ```funciones.py``` en ```servidor/```
13. ```logica.py``` en ```servidor/```
14. ```paramatros.json``` en ```servidor/```
15. ```servidor.py``` en ```servidor/```
16. ```utils.py``` en ```servidor/```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```
2. ```PyQt5```: ``QtWidgets, QtGui, Qtimer, QtCore (debe instalarse)
3. ```random```: ``randint
4. ```threading```: ``threading
5. ```socket```: ``socket
6. ```json```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```logica.py```: Contiene a ```Logica```,  clase utilizada para recibir y procesar mensajes, y más.
2. ```funciones.py```:  contiene las funciones para encriptar, desencriptar, y codificar.
3. ```interfaz.py```:  se utilizó para manejar las respuestas enviadas por el servidor.
4. ```utils.py```:  contiene las funciones para manejar los archivos .json

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <No cuento con supuestos./a> 



## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. AF3 y ejemplo final de Ayudantía 8, me basé en ese código para conectar el servidor con los clientes, ademas de ver la manera y formato de los mensajes.
