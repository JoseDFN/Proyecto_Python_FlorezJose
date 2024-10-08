# The-Cachipun

The Chachipun con modo JvJ y JvE, implementando mecánicas de escudos y puntajes.
El juego "The Cachipun" es una "copia" de piedra papel y/o tijera pero con el poder de escudo. En este caso, si algun usuario y/o la maquina (Modo PvE) gana 2 veces seguidas (al quedar en empate se resetea las victorias seguidas), èste obtendra un escudo que le dura hasta que pierda.El jugador que gane 3 rondas es el que se "corona" como ganador de la partida.
Dentro del juego se puede, registrar jugadores, seleccionarlos para jugar las distintas partidas, jugar como tal el juego y ver las estadisticas (mejores 3, ultimo de la tabla, jugadores con mas perdidas contra la maquina y el promedio de los jugadores que le han ganado a la maquina.)
------------------------------------------------------------------------
Modulo 1, app:
Este módulo es parte de un juego que permite a los usuarios elegir entre diferentes modos de juego y ver estadísticas. Utiliza varias utilidades y funciones modularizadas para facilitar la interacción con el usuario y gestionar el estado del juego.

Las importaciones que se hicieron en este modulo principal son:
-clAndPause: Para limpiar la pantalla y pausar la ejecución.
-messages: Para mostrar mensajes y menús al usuario.
-core: Para manejar la base de datos del juego.
-PvPMode y PvEMode: Para gestionar los modos de juego jugador contra jugador y jugador contra máquina, respectivamente.
-EstadisticasJuego: Para mostrar las estadísticas del juego.
-stats: Para manejar estadísticas adicionales.
-math.e: Se importa la constante 'e' de la librería de matemáticas, aunque no se utiliza en el fragmento proporcionado.

En un primer momento el programa inicia variables de control como isGame en True, variables de control de opcion como userOp en 0 y se crea el diccionario "principal" en el que se encontrara el diccionario vacio de jugadores y el diccionario de maquina con sus estadisticas incializadas en 0 (número de partidas jugadas, ganadas y perdidas)

Luego se inicializa un bucle en el que se usa como controlador la variable isGame. Dentro del bucle se le asigna la ruta al archivo MY_DATABASE