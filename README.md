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

Las variables "Globales" incluidas en el modulo son:
-userOp:Almacena la opción seleccionada por el usuario en el menú principal.
-isGame:Controla si el ciclo principal del juego sigue en ejecución.
-Game:iccionario que se usa como base para la estructura del archivo JSON. Contiene información de los jugadores y de la máquina (juegos jugados, ganados y perdidos).

Luego de importar y haber definido las variales globales, se inciializa en bucle while teniendo como controlador a la variable isGame (mientras esta sea True el ciclo seguira "corriendo").
Si el usuario introduce un valor no numérico, se muestra un mensaje de error y se vuelve a mostrar el menú.

Dentro de este ciclo se Imprimiran las opciones del menu, las cuales llevan a el usuario a los menus determinados para cada opcion y/o modulo, los cuales son:
Opción 1: Entra en el menu y modo PvP usando pvpMode.menuPvP().
Opción 2: Entra en el menu y modo PvE usando pveMode.menuPvE().
Opción 3: Entra al menu de para mostrasr las estadísticas del juego con statsG.EstadisticasJuego().
Opción 4: Genera una "tabla" con estadísticas utilizando st.tabla().
Opción 5: Limpia la pantalla y termina el ciclo del juego (isGame = False).
Opción inválida: Muestra un mensaje de que la opción no está disponible.

Para este modulo se hace un manejo de errores por medio de Trys y except tanto para la entrada de datos de la opcion del jugador como para alguna excepción durante la ejecución de las opciones, el mensaje de error se captura y se muestra utilizando la función msg.mensajeErro(e). Asegurando asi que el programa no se cierre inesperadamente y se le da al usuario la oportunidad de intentar de nuevo.

En resumen:
1.El archivo JSON se prepara o verifica antes de cada ciclo.
2.Se muestra el menú principal.
3.El usuario selecciona una opción y el programa ejecuta la acción correspondiente.
4.El ciclo se repite hasta que el usuario decide salir (opción 5).
------------------------------------------------------------------------------
Modulo 2, PvPMode:

Este módulo es parte del sistema de juego que permite a los jugadores competir en el modo Jugador vs Jugador (PvP). Proporciona un menú para que los usuarios registren jugadores, inicien sesión y jueguen entre sí.

Las importaciones que se hicieron en este módulo son:
clAndPause: Para limpiar la pantalla y pausar la ejecución en momentos clave.
messages: Para mostrar mensajes y menús del modo Jugador vs Jugador.
player: Para registrar jugadores y gestionar el inicio de sesión.
matches: Para ejecutar la lógica de las partidas en el modo PvP.
Las variables "globales" incluidas en este módulo son:
userOpPvP: Almacena la opción seleccionada por el usuario en el menú PvP.
isPlayer: Controla si el ciclo del menú PvP sigue en ejecución.
Estructura del Ciclo Principal:
Después de limpiar la pantalla e imprimir el menú con las opciones disponibles, el usuario ingresa una opción. Si el valor ingresado no es un número válido, se captura el error y se muestra un mensaje indicándolo, permitiendo al usuario intentar nuevamente. Dentro del ciclo, las opciones del menú son las siguientes:

Opción 1: Registra a un nuevo jugador llamando a ch.registerP().
Opción 2: Inicia sesión para el primer jugador usando ch.loginP1().
Opción 3: Inicia sesión para el segundo jugador con ch.loginP2().
Opción 4: Inicia una partida en modo PvP con la función mat.modePvP().
Opción 5: Finaliza el ciclo del menú y regresa al menú principal del juego.
Manejo de Errores:
Se usa un bloque try-except para manejar los errores. Si el usuario ingresa una opción inválida, se muestra un mensaje que le indica que debe ingresar un número. Además, se captura cualquier excepción durante la ejecución de las opciones del menú, mostrando el error mediante msg.mensajeErro(e), asegurando que el programa no se cierre inesperadamente.

Resumen:
Se muestra el menú del modo Jugador vs Jugador.
El usuario selecciona una opción y el programa ejecuta la acción correspondiente.
El ciclo se repite hasta que el usuario decide salir (Opción 5).
El manejo de errores asegura que el programa continúe funcionando incluso si ocurre algún fallo durante la ejecución.