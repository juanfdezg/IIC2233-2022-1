# Tarea 1:  DCCorreos :school_satchel:

## Consideraciones generales :octocat:
Para que el programa comience basta con ejecutar el archivo ´´main.py´´. Todas las funciones del programa fueron implementadas correctamente, se puede navegar a través de los menús, apostar y comprar bebestibles de manera correcta. Sin embargo, hay detalles que se podrían mejorar en mi tarea. En mi código, cuando intentas comprar un bebestible pero no tienes el dinero suficiente, se te devuelve al menú principal del usuario en vez de volver a mostrar la lista de bebestibles disponibles. De la misma forma, cuando seleccionas la opción de "Volver" estando en el menú principal, se te devuelve al menú de inicio en vez de mostrar la lista de jugadores de nuevo, esto se podría mejorar.
Cuando el programa te pide la cantidad de dinero a apostar, este se cae completamente si es que se ingresa un input no válido, como un str. Este problema lo tuve también la tarea pasada y sigo sin saber bien como solucionarlo. Mi diagrama de clases la verdad no sé si quedó muy bien, tuve dudas sobre las relaciones entre clases.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️
#### Programación Orientada a Objetos: 38 pts (28%)
##### 🟠  Diagrama <Entregué el diagrama respetando el formato solicitado, sin embargo, no se si está totalmente bien hecho.  El diagrama contiene todas las clases que usé en mi código, y las relaciones de herencia entre ellas están bien mostradas. Sin embargo, las otras relaciones no se si están bien representadas. Cada clase tiene sus atributos y sus métodos respectivos.\>
##### 🟠 Definición de clases, atributos, métodos y properties <Las clases Casino, Juego, Bebestible y Jugador están bien definidas, con sus respectivos parámetros y métodos. La acción/método "cliente_recurrente" de la clase Bebedor realmente no hace mucho en mi código, implementé la funcionalidad de otra manera sin definirlo como un método, eso no se si cuenta como error o si está bien así también.\>
##### ✅ Relaciones entre clases <Las clases se relacionan perfectamente entre si, utilizando las relaciones pedidas. Herencias, agregación y composición.\>
#### Simulaciones: 10 pts (7%)
##### ✅ Crear partida <Se pueden crear partidas sin ningún problema en DCCasino, instanciando correctamente los juegos, personajes y bebestibles. No lo probé en el código, pero no debería tener problema al leer los archivos si es que cambian el orden de los atributos.\>
#### Acciones: 35 pts (26%)
##### 🟠 Jugador <Todo funciona correctamente menos algo que pensé que había hecho, pero escribiendo este ReadMe acabo de darme cuenta que no hice. La energía no afecta la capacidad del jugador para apostar, si bien esta se le descuenta cada vez que logra apostar correctamente. En el fondo, el jugador puede apostar si y solo si tiene el dinero suficiente para hacerlo, pero podría tener 0 de energía y esto no sería un problema. Se me olvidó agregar la restricción de la energía para poder apostar.\>
##### ✅ Juego <Se implementa de forma correcta el cálculo de probabilidades y se modifican las características del jugador dependiendo del resultado obtenido.\>
##### ✅ Bebestible <Todo funciona correctamente, los bebestibles solo se pueden comprar si es que el dinero del jugador es suficiente y se modifican las características del jugador después de beberlo, considerando las cualidades especiales de cada jugador.\>
##### ✅ Casino <Funciona correctamente\>
#### Consola: 41 pts (30%)
##### ✅  Menú de Inicio <Menú implementado correctamente.\>
##### ✅ Opciones de jugador <Todo funciona correctamente y se muestra correctamente la lista de jugadores y sus personalidades.\>
##### 🟠 Menú principal <Se puede navegar a través del menú, pero como expliqué más arriba, podría estar mejor hecha la opción de "Volver".\>
##### ✅ Opciones de juegos <Implementado correctamente, las opciones de juegos se muestran y se pueden escoger correctamente. Las probabilidades se calculan correctamente. Si es que una probabilidad de ganar da un valor negativo, opté por dejarla en 0.\>
##### 🟠 Carta de bebestibles <Lo que me faltó fue que cuando el usuario no tenga el dinero suficiente para comprar un bebestible, se le devuelva a la lista de bebestibles. En mi programa se devuelve al menú principal.\>
##### ✅ Ver estado del Jugador <Implementado correctamente, se puede ver el estado del jugador y volver sin problemas.\>
##### 🟠 Robustez <Los menús no generan ningún tipo de problema, solo se genera un inconveniente cuando se pide el dinero a apostar, ya que si recibe un str el programa se cae.\>
#### Manejo de archivos: 13 pts (9%)
##### ✅ Archivos CSV  <Se trabaja correctamente con todos los archivos.\>
##### ✅ parametros.py <Se implementa correctamente el archivo parametros.py y contiene todos los parámetros pedidos.\>
#### Bonus: 3 décimas máximo
##### ❌ Ver Show <No fue implementado.\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```bebestibles.py``` en ```T1```
2. ```parámetros.py``` en ```T1```
3. ```jugadores.py``` en ```T1```
4. ```juego.py``` en ```T1```
5. ```casino.py``` en ```T1```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```abc```: ```ABC, abstractmethod```
2. ```random```: ```random``` (si no me equivoco no deben instalarse)
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```bebestibles```: Contiene a ```Bebestible```, ```Jugo```,  ```Gaseosa```, ```BrebajeMagico``` Se utilizó para poder guardar cada bebestible como un objeto de la clase Bebestible y trabajar con sus atributos y métodos.
2. ```juego```: Contiene a ```Juego``` Se utilizó para guardar cada juego como un objeto de la clase Juego y poder trabajar con sus atributos y métodos.
3.  ```jugadores```: Contiene a ```Jugador```, ```Ludopata```,  ```Tacaño```, ```Bebedor```, ```Casual``` Se utilizó para guardar cada jugador como un objeto de la clase padre Jugador y poder trabajar con sus atributos y métodos.
4. ```casino```: Contiene a ```Casino```, Casino almacena todos los bebestibles y juegos, y desde esta clase se crea instancia de casino para comenzar el programa.
5. ```parametros``: contiene todos los parámetros que se utilizan a lo largo de la tarea.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <No se ingresarán strings en el input de dinero apostado, ya que si esto ocurre se crashea el programa./a> 
 
## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.programiz.com/python-programming/methods/list/index>: esto lo utilicé para leer los índices de las listas y poder leer correctamente los archivos csv. Está implementado en el archivo <casino.py> en las líneas <23-25, 45-48>, y en el archivo <main.py> en las líneas <35-44 >

