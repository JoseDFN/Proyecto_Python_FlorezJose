# The-Cachipun

The Chachipun con modo JvJ y JvE, implementando mecánicas de escudos y puntajes.
El juego "The Cachipun" es una "copia" de piedra papel y/o tijera pero con el poder de escudo. En este caso, si algun usuario y/o la maquina (Modo PvE) gana 2 veces seguidas (al quedar en empate se resetea las victorias seguidas), èste obtendra un escudo que le dura hasta que pierda.El jugador que gane 3 rondas es el que se "corona" como ganador de la partida.
Dentro del juego se puede, registrar jugadores, seleccionarlos para jugar las distintas partidas, jugar como tal el juego y ver las estadisticas (mejores 3, ultimo de la tabla, jugadores con mas perdidas contra la maquina y el promedio de los jugadores que le han ganado a la maquina.)
------------------------------------------------------------------------
Modulo 1, app:
En el modulo principal, app.py, inicialmente se importan los modulos para limpiar y pausar dependiendo del OS (modulo clAndPause) como clp, el modulo para los mensajes que se muestran por pantalla (messages)como msg, el modulo core para el Json (core) como cf, el modulo para el menu de la seccion PvP (PvPMode) como pvpMode, el modulo para el menu de la seccion PvE (PvEMode) como pveMode, el modulo para el menu de las estadisitcas (EstadisticasJuego) como statsG y el modulo stats para la tabla de puntos o posiciones (stats) como st.

posterior a esto se definio el cuerpo del modulo principal, que es el modulo del que se debe ejecutar el juego. dentro de este cuerpo principal se definio e hizo lo siguiente:
1.Se define o inicia la variable userOp en 0 para su posterior uso en la seleccion del menu.
2.Se inicia la variable isGame como True para su posterior uso como controlador del ciclo o bucle.
3.Se define el diccionario usado como referencia para evaluar y/o crear el archivo Json en donde se harà la persistencia de datos.
4.Se inicializa el bucle teniendo como variable de control a isGame(en este caso, el bucle seguira activo mientras la variable tenga como valor True).
5.Se le asigna como valor o ruta 'data/PPoT.json' a la variable MY_DATABASE, contenida en el core file.