# Tarea 2: DCComando Espacial :school_satchel:


## Consideraciones generales :octocat:

Para que el programa comience basta con ejecutar el archivo ´´main.py´´. Todas las funciones del juego fueron implementadas correctamente, se puede jugar en cualquiera de los 3 mapas, pasando correctamente de nivel y guardando bien los puntajes. Los aliens se mueven y rebotan de forma correcta, su velocidad y el tiempo de nivel se adecuan al nivel en cuestión. 
Si bien el juego funciona correctamente, hay ciertos errores o vacíos que habría que mejorar. Los aliens no rebotan entre sí, solamente con las paredes. El juego no se preocupa de que los aliens se superpongan al aparecer en la pantalla, por lo que puede ocurrir. Intenté implementar un factor de aleatoriedad para que los aliens se muevan en direcciones distintas cada vez que aparezcan, pero esto no funcionó muy bien, ya que se terminan moviendo siempre en la misma dirección inicial. No hice la precisión de la mira tan prolija para que fuese más fácil dispararle a los aliens. A veces se produce un bug en el juego cuando se selecciona la opción de 'Salir', estando este bug relacionado con la función de 'Pausa'. Cuando se vuelve al menú inicial mediante el botón 'Salir' y se inicia una nueva partida, hay veces que no se puede mover la mira pero si se mueven los aliens, al apretar el botón de pausa, se logra mover la mira y disparar, pero se congelan los aliens, de esta forma el juego no queda funcionando correctamente ya que o los aliens o la mira se encuentran en pausa. Hay otros casos en que solo basta pausar y despausar el juego una vez y funciona sin problemas. Cuando se le dispara al último alien del nivel con la última bala, aparece la ventana de que perdiste el nivel, pero rápidamente se cambia a la ventana de victoria como corresponde. Los cheatcodes están implementados correctamente, en donde hay que presionar las teclas secuencialmente, no al mismo tiempo. Para mover la mira se utilizan las teclas 'awsd' en minúsculas y se dispara con la letra 'h' minúscula también. Para pausar el juego se puede presionar el botón 'Salir' o utilizar la tecla 'p', la barra espaciadora también pausa el juego pero no se por qué, no fue una funcionalidad intencionada.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Ventana de Inicio: 4 pts (4%)
#### Ventana de Ranking: 5 pts (5%)
#### Ventana principal: 7 pts (7%)
#### Ventana de juego: 14 pts (13%)
#### Ventana de post-nivel: 5 pts (5%)
#### Mecánicas de juego: 47 pts (45%)
##### ✅ Arma <La mira del arma y su funcionamiento fueron implementadas correctamente. Se definió una clase Mira donde se definieron métodos para implementar sus funcionalidades como el movimiento, el disparo y la pausa. También se definieron properties para la posición de la mira, de esta forma se fijaban los límites de su movimiento, para no salirse de la ventana. Se genera una instancia de Mira y esta se le entrega a la clase Juego, para trabajar en conjunto con la lógica del juego en sí. Para que funcione correctamente, se implementaron distintas señales. Cuando se dispara se reproduce el sonido y la mira cambia de color por un segundo, y cuando el disparo es efectivo se genera la explosión. Si las balas se agotan, el juego acaba.\>
##### 🟠 Aliens y Escenario de Juego <Los aliens  van apareciendo en pares de a 2 de forma aleatoria como se pide, su movimiento no tiene problemas y rebotan correctamente con las paredes. No se implementó que los aliens no se puedan superponer entre sí, esto se podría mejorar. Los aliens tampoco rebotan entre sí. La velocidad de los aliens va acorde al nivel y al mapa escogido. La duración se ajusta correctamente de igual forma, todo esto mediante señales. Mientras se juega, se puede visualizar cuántos aliens se han destruido en el nivel y cuantos faltan para pasar al siguiente.\>
##### ✅ Fin de Nivel <Los niveles finalizan correctamente, si es que se agotan las balas, el tiempo, o se destruyen todos los aliens. Los puntajes se van actualizando correctamente, el puntaje solo se suma si es que se gana el nivel. Cada vez que se acaba un nivel, ya sea con una victoria o derrota, se abre la ventana postnivel con las estadísticas y mensaje correspondiente.\>
##### ✅ Fin del juego <El puntaje se guarda correctamente junto al nombre de usuario. La animación de Terminator-dog solo aparece si es que se gana el nivel. Si se pierde el nivel, no se puede seguir jugando, a menos a que se inicie una nueva partida. Si se gana el nivel se puede seguir jugando sin ningún problema.\>
#### Cheatcodes: 8 pts (8%)
##### 🟠 Pausa <La pausa congela el movimiento de los aliens y de la mira, quedando inhabilitados, no se puede mover ni disparar. El tiempo también deja de correr. Se puede pausar el juego mediante el botón 'Pausa', la letra 'p' y la barra espaciadora. La función de pausar puede presentar problemas cuando se inicia una nueva partida al 'Salir' de una partida en juego. Puede pasar que la mira quede pausada pero los aliens no, o al revés. Quitando este último problema, la pausa funciona perfectamente.\>
##### ✅ O + V+ N + I <Al presionar las teclas secuencialmente, no al mismo tiempo, se otorgan 'infinitas' balas exclusivamente en el nivel que se está jugando. No son realmente balas infinitas, pero es una cantidad muy alta. Cuando se utiliza este cheatcode y se pasa al siguiente nivel, el puntaje aumenta muchísimo debido a la gran cantidad de balas, la cual se utiliza en la fórmula de cálculo de puntaje.\>
##### ✅  C + I + A <Al presionar las teclas secuencialmente, no al mismo tiempo, se pasa inmediatamente al siguiente nivel sin ningún problema.\>
#### General: 14 pts (13%)
##### ✅ Modularización <Se implementa correctamente un back-end y un front-end, donde interactúan entre si mediante numerosas señales. El front-end se encarga de las ventanas y su interfaz, donde no hay procesamiento o métodos muy complejos, esto último se le delega al back-end. En el back-end se implementan las funciones más importantes del juego, mediante las clases Juego, Alien y Mira.\>
##### ✅ Modelación <El programa cuenta con un bajo acoplamiento y una alta cohesión.\>
##### ✅ Archivos  <Se trabaja correctamente con el archivo de puntajes.txt, con los parámetros y los assets.\>
##### ✅ Parametros.py <El archivo contiene todos los parámetros pedidos en el enunciado y se utilizan correctamente al importarlos.\>
#### Bonus: 10 décimas máximo
##### ✅ Risa Dog <Cumple con los requisitos pedidos.\>
##### ❌ Estrella <explicacion\>
##### ❌ Disparos extra <explicacion\>
##### ❌ Bomba <explicacion\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```clases_objetos.py``` en ```T2/backend```
2. ```logica_juego.py``` en ```T2/backend```
3. ```logica_principal.py``` en ```T2/backend```
4. ```ventana_inicio.py``` en ```T2/frontend```
5. ```ventana_juego.py``` en ```T2/frontend```
6. ```ventana_postnivel.py``` en ```T2/frontend```
7. ```ventana_principal.py``` en ```T2/frontend```
8. ```ventana_ranking.py``` en ```T2/frontend```
9. ```ventana_juego.ui``` en ```T2/frontend```
10.```ventana_postnivel.ui``` en ```T2/frontend``` 
```parametros.py``` en ```T2```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```sys.path.append```
2. ```PyQt5```: ```QtWidgets, QtGui, QtCore``` (debe instalarse)
3. ```random```: ```randint, choice```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```clases_objetos```: Contiene a ```Mira```, ```Alien``` hecha para definir las clases de Mira y Alien y trabajar con sus atributos y métodos.
2. ```logica_juego```: Contiene a ```Juego```, la clase principal que contiene las mecánicas del juego>
3. ```logica_principal```: Contiene a ```LogicaPrincipal```, la cual maneja la lógica de la ventana principal.
4. ```ventana_inicio```: Contiene a ```VentanaInicio```, se utiliza para la parte visual de la ventana de inicio.
5. ```ventana_juego```: Contiene a ```VentanaJuego```, se utiliza para la parte visual de la ventana de inicio.
6. ```ventana_postnivel```: Contiene a ```VentanaPostnivel```, se utiliza para la parte visual de la ventana de inicio.
7. ```ventana_ranking```: Contiene a ```VentanaRanking```, se utiliza para la parte visual de la ventana de inicio.
8. ```ventana_principal```: Contiene a ```VentanaPrincipal```, se utiliza para la parte visual de la ventana de inicio.
9. ```parametros```: Contiene todos los parámetros que se utilizan a lo largo de la tarea.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Se dispara con la letra 'h' ya que la barra espaciadora me trajo problemas y no supe bien como implementarla./a> 


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.geeksforgeeks.org/python-import-from-parent-directory/>: utilicé este código para poder importar correctamente el archivo parámetros.py.
2. \<https://www.delftstack.com/es/tutorial/pyqt5/pyqt5-radiobutton//>: utilicé este código para poder utilizar correctamente los RadioButtons, y verificar qué opción estaba seleccionada. Lo utilicé en ventana_principal.py en el método 'onClicked'.
