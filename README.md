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
------------------------------------------------------------------------------
Modulo 3, PvEMode:

Este módulo es parte del sistema de juego que permite a los jugadores enfrentarse contra la máquina en el modo Jugador vs Máquina (PvE). A través de un menú, los jugadores pueden registrarse, iniciar sesión y jugar contra la inteligencia artificial.

Las importaciones que se hicieron en este módulo son:
clAndPause: Para limpiar la pantalla y pausar la ejecución.
messages: Para mostrar los mensajes y el menú del modo Jugador vs Máquina.
player: Para registrar a los jugadores y gestionar el inicio de sesión.
matches: Contiene la lógica para las partidas en el modo PvE.

Las variables "globales" incluidas en este módulo son:
userOpPvE: Almacena la opción seleccionada por el usuario en el menú PvE.
isPlayer: Controla si el ciclo del menú PvE sigue en ejecución.

Estructura del Ciclo Principal:
Una vez que se limpia la pantalla e imprime el menú, el jugador elige una opción. Si el valor ingresado no es un número, se captura la excepción y se muestra un mensaje de error, permitiendo que el jugador vuelva a intentarlo.Las opciones del menú en este módulo son:

Opción 1: Llama a ch.registerP() para registrar a un nuevo jugador.
Opción 2: Permite iniciar sesión para el jugador mediante ch.loginP1().
Opción 3: Inicia una partida en modo PvE con la función mat.modePvE().
Opción 4: Finaliza el ciclo del menú y regresa al menú principal del juego.

Manejo de Errores:
Se utiliza un bloque try-except para gestionar los errores de entrada del usuario. Si el usuario ingresa un valor no numérico, se muestra un mensaje indicando que debe ingresar un número. Además, si ocurre algún error durante la ejecución de una opción, se captura la excepción y se muestra el error utilizando msg.mensajeErro(e), lo que permite que el programa continúe su ejecución sin cerrarse inesperadamente.

Resumen:

El menú del modo Jugador vs Máquina se muestra al jugador.
El jugador selecciona una opción y el programa ejecuta la acción correspondiente.
El ciclo se repite hasta que el jugador decide salir (Opción 4).
El manejo de errores asegura que el programa siga funcionando incluso si hay problemas durante la ejecución.
------------------------------------------------------------------------------Modulo 4, EstadisticasJuego:

Este módulo permite a los jugadores acceder y visualizar diferentes estadísticas del juego. A través de un menú interactivo, los usuarios pueden consultar información sobre rendimientos y otros datos estadísticos relevantes.

Las importaciones que se hicieron en este módulo son:
clAndPause: Para limpiar la pantalla y pausar la ejecución cuando sea necesario.
messages: Para mostrar los mensajes y el menú de estadísticas del juego.
stats: Maneja las funciones que calculan y muestran las estadísticas relacionadas con los jugadores y las partidas.

Las variables "globales" incluidas en este módulo son:
userOpPvE: Almacena la opción seleccionada por el usuario en el menú de estadísticas.
isPlayer: Controla si el ciclo del menú de estadísticas sigue en ejecución.

Estructura del Ciclo Principal:
Después de limpiar la pantalla e imprimir el menú de estadísticas, el usuario elige una opción. Si el valor ingresado no es un número válido, se captura la excepción y se muestra un mensaje de error, permitiendo al usuario volver a intentarlo. Las opciones del menú son las siguientes:

Opción 1: Llama a st.tTres() para mostrar el top 3 de jugadores de la tabla.
Opción 2: Llama a st.lastPGame() para mostrar el último jugador de la tabla.
Opción 3: Llama a st.mostLossesAi() para mostrar los jugadores que más han perdido contra la IA.
Opción 4: Llama a st.avgWinsAi() para mostrar el promedio de jugadores que le han ganado a la IA.
Opción 5: Finaliza el ciclo del menú de estadísticas y regresa al menú principal.

Manejo de Errores:
El bloque try-except captura los errores en la entrada del usuario. Si se ingresa un valor no numérico, se muestra un mensaje de error solicitando que se ingrese un número. Además, cualquier excepción generada durante la ejecución de las opciones del menú es gestionada con msg.mensajeErro(e), permitiendo que el programa continúe sin interrupciones.

Resumen:

Se muestra el menú de estadísticas del juego.
El usuario selecciona una opción para consultar las estadísticas correspondientes.
El ciclo se repite hasta que el usuario decide salir (Opción 5).
El manejo de errores asegura que el programa continúe funcionando de manera estable en caso de fallos durante la ejecución.
------------------------------------------------------------------------------Funcion tabla:

Esta función se encarga de mostrar un ranking de los jugadores basado en sus puntos. Ordena a los jugadores de mayor a menor puntuación y muestra una tabla con los detalles de los mejores jugadores.

Descripción:
La función tabla realiza las siguientes acciones:

Limpieza de la pantalla: Utiliza la función clp.limpiar() para asegurar que la pantalla esté limpia antes de mostrar la información.
Lectura de datos del juego: La función accede a los datos del archivo JSON utilizando core.ReadFile(), el cual devuelve la información almacenada de los jugadores.
Conversión de jugadores: Convierte los datos de los jugadores a una lista de diccionarios para facilitar la manipulación.
Ordenación de jugadores: Ordena la lista de jugadores según su puntuación (points) de mayor a menor usando la función sorted() con una función lambda como clave de ordenación.
Despliegue del ranking: Muestra en pantalla los jugadores ordenados, incluyendo su nombre, apodo (nickname) y puntos. Cada jugador aparece en formato de ranking, precedido por su posición en el "Top".
Pausa del programa: Al finalizar, la función clp.pausar() se utiliza para pausar la ejecución y permitir que el usuario pueda visualizar los resultados antes de continuar.

Variables y Funcionalidad:
game_data: Contiene la información del archivo JSON leído que incluye los datos de los jugadores.
jugadores: Almacena los datos específicos de los jugadores, extraídos del JSON.
jugadores_list: Convierte los datos del diccionario de jugadores en una lista de diccionarios para facilitar la manipulación.
sPlayers: Lista de jugadores ordenada de mayor a menor según la cantidad de puntos.

Flujo de Ejecución:
Limpia la pantalla.
Lee los datos del archivo JSON.
Convierte los jugadores a una lista y los ordena por puntos.
Imprime el ranking de jugadores.
Pausa la ejecución para permitir la visualización del resultado.

Resumen:

La función tabla es útil para mostrar una clasificación de los jugadores según sus puntos acumulados. Esto permite a los usuarios visualizar quiénes son los jugadores con mejor desempeño en el juego.
------------------------------------------------------------------------------Modulo 5, clAndPause:

Este módulo contiene dos funciones principales: limpiar y pausar, las cuales están diseñadas para proporcionar una experiencia más fluida al usuario al limpiar la pantalla y permitir pausas durante la ejecución del programa, adaptándose al sistema operativo en el que se esté ejecutando.

Función limpiar:
Esta función se encarga de limpiar la pantalla de la terminal o consola, dependiendo del sistema operativo en el que se esté ejecutando el programa.

Detalles de ejecución:
Detección del sistema operativo: La función usa sys.platform para detectar si el sistema es Linux, macOS (denominado como "darwin"), o Windows.
Comando de limpieza:
Para Linux y macOS, utiliza el comando clear para limpiar la pantalla.
Para Windows, utiliza el comando cls para realizar la misma tarea.

Flujo de ejecución:
Verifica la plataforma en la que se ejecuta el programa.
Ejecuta el comando adecuado (clear o cls) según el sistema operativo.

Función pausar:
Esta función pausa la ejecución del programa, permitiendo que el usuario pueda leer o interactuar antes de continuar con la ejecución.

Detalles de ejecución:
Detección del sistema operativo: Al igual que la función limpiar, utiliza sys.platform para determinar el sistema operativo.
Pausa en la ejecución:
En Linux y macOS, utiliza un input() que espera que el usuario presione una tecla para continuar.
En Windows, usa el comando pause, que tiene el mismo propósito de esperar una interacción del usuario.

Flujo de ejecución:
Detecta el sistema operativo.
Si el sistema es Linux o macOS, espera que el usuario presione una tecla para continuar.
Si el sistema es Windows, usa el comando pause para pausar la ejecución.

Resumen:

limpiar: Limpia la pantalla según el sistema operativo.
pausar: Pausa la ejecución del programa y espera interacción del usuario.
Ambas funciones se adaptan automáticamente al sistema operativo, lo que las hace compatibles con múltiples plataformas.
------------------------------------------------------------------------------Modulo 6, core:

Este módulo se encarga de la gestión de la base de datos del juego, que se almacena en un archivo JSON. Contiene funciones para crear, leer, actualizar y verificar la existencia del archivo, permitiendo así la persistencia de datos entre sesiones de juego.

Variables globales:
MY_DATABASE: Almacena la ruta del archivo de la base de datos. Inicialmente, está configurada como None y debe establecerse antes de usar las funciones del módulo.

Función NewFile(*param):
Esta función crea un nuevo archivo JSON o sobrescribe el archivo existente con los datos proporcionados.

Detalles de ejecución:
Abre el archivo especificado por MY_DATABASE en modo escritura ("w").
Utiliza json.dump() para escribir los datos en formato JSON en el archivo, con una indentación de 4 espacios para mejorar la legibilidad.
Parámetros:
*param: Recibe un número variable de argumentos, donde param 0 es el diccionario de datos que se desea guardar en el archivo.

Función ReadFile():
Esta función lee los datos del archivo JSON especificado por MY_DATABASE y devuelve el contenido como un diccionario.

Detalles de ejecución:
Abre el archivo en modo lectura ("r").
Utiliza json.load() para cargar los datos del archivo y devolverlos como un diccionario de Python.

Función checkFile(*param):
Esta función verifica si el archivo de la base de datos existe y, si es así, actualiza sus datos.

Detalles de ejecución:
Verifica si el archivo especificado por MY_DATABASE existe usando os.path.isfile().
Si el archivo existe y se proporcionan datos (len(param) es verdadero), actualiza el contenido del archivo con los datos leídos del archivo existente.
Si el archivo no existe y se proporcionan datos, llama a NewFile() para crear un nuevo archivo con esos datos.
Parámetros:
*param: Recibe un número variable de argumentos. Si se proporciona, se actualizará el archivo existente o se creará uno nuevo.

Función save_game(game):
Esta función guarda el estado actual del juego en el archivo JSON especificado.

Detalles de ejecución:
Llama a NewFile() con el estado actual del juego como argumento para guardar los datos en el archivo.
Parámetros:
game: El diccionario que representa el estado actual del juego, que se desea guardar en la base de datos.

Resumen:

MY_DATABASE: Variable global que define la ruta del archivo de la base de datos.
NewFile(param): Crea o sobrescribe el archivo JSON con los datos proporcionados.
ReadFile(): Lee y devuelve los datos del archivo JSON como un diccionario.
checkFile(param): Verifica la existencia del archivo y actualiza su contenido si es necesario.
save_game(game): Guarda el estado actual del juego en el archivo JSON.
------------------------------------------------------------------------------Modulo 7, dataPlayers:

Este módulo define dos diccionarios principales: Jugador y partida, que almacenan la información necesaria para gestionar los datos de los jugadores y el estado de una partida en el juego.

Diccionario Jugador:
El diccionario Jugador representa la información de un jugador en el juego. Cada jugador tiene varios atributos que permiten rastrear su rendimiento y estado.

Atributos:
name: (string) El nombre del jugador.
nickname: (string) El apodo del jugador, que puede ser utilizado para referirse a él en el juego.
wins: (int) El número total de partidas ganadas por el jugador.
losses: (int) El número total de partidas perdidas por el jugador.
points: (int) Los puntos acumulados por el jugador, que pueden influir en su clasificación o rendimiento general.
gPlayed: (int) El número total de juegos jugados por el jugador.
gamesLostMatchine: (int) La cantidad de partidas perdidas contra la máquina (IA).
gamesWonMachine: (int) La cantidad de partidas ganadas contra la máquina (IA).

Diccionario partida:
El diccionario partida contiene información sobre una partida específica, incluyendo datos sobre ambos jugadores y el estado de la partida.

Atributos:
Player1: (int) Identificador del jugador 1, que puede referirse a su posición o ID en el juego.
nicknameP1: (string) Apodo del jugador 1, utilizado para mostrar en la interfaz de usuario.
nicknameP2: (string) Apodo del jugador 2, utilizado para mostrar en la interfaz de usuario.
Player2: (int) Identificador del jugador 2.
Tie: (int) Número de empates en la partida.
Player1Wins: (int) Contador de victorias del jugador 1 en la partida actual.
Player2Wins: (int) Contador de victorias del jugador 2 en la partida actual.
Player1Losses: (int) Contador de derrotas del jugador 1 en la partida actual.
Player2Losses: (int) Contador de derrotas del jugador 2 en la partida actual.
Player1ConsecutiveWins: (int) Contador de victorias consecutivas del jugador 1.
Player2ConsecutiveWins: (int) Contador de victorias consecutivas del jugador 2.
Player1ShieldActive: (bool) Indica si el escudo del jugador 1 está activo.
Player2ShieldActive: (bool) Indica si el escudo del jugador 2 está activo.

Resumen:
Jugador: Diccionario que almacena información individual de un jugador, incluyendo su nombre, apodo, estadísticas de juego y rendimiento contra la máquina.
partida: Diccionario que mantiene el estado de una partida, incluyendo detalles de ambos jugadores, sus resultados y estadísticas durante la partida.
------------------------------------------------------------------------------
Modulo 8, matches:

Este módulo contiene funciones que gestionan la lógica de las partidas en el juego, incluyendo la inicialización de datos, el procesamiento de resultados de partidas y la ejecución de los modos PvP y PvE.

Variables Globales:
winsP1: (int) Número de victorias del jugador 1 (global).
lossesP1: (int) Número de derrotas del jugador 1 (global).
winsP2: (int) Número de victorias del jugador 2 (global).
lossesP2: (int) Número de derrotas del jugador 2 (global).

Funciones:

initializedata0(data):

Inicializa los datos de la partida para el diccionario data, estableciendo los contadores y estados iniciales de los jugadores.

Parámetros:
data: (dict) Diccionario que representa el estado de la partida.
Descripción:
Esta función configura los siguientes atributos en el diccionario data:

Tie: Número de empates.
Player1Wins: Contador de victorias del jugador 1.
Player2Wins: Contador de victorias del jugador 2.
Player1Losses: Contador de derrotas del jugador 1.
Player2Losses: Contador de derrotas del jugador 2.
Player1ConsecutiveWins: Contador de victorias consecutivas del jugador 1.
Player2ConsecutiveWins: Contador de victorias consecutivas del jugador 2.
Player1ShieldActive: Estado del escudo del jugador 1 (inicialmente False).
Player2ShieldActive: Estado del escudo del jugador 2 (inicialmente False).

resultadoMatch(oP1, oP2):

Procesa el resultado de una partida entre dos jugadores.

Parámetros:
oP1: (int) Opción seleccionada por el jugador 1.
oP2: (int) Opción seleccionada por el jugador 2.
Descripción:
Esta función evalúa las opciones seleccionadas por ambos jugadores y actualiza los contadores de victorias, derrotas y empates en el diccionario data.partida:

Determina el ganador de la ronda y actualiza los contadores de victorias y pérdidas.
Maneja el estado del escudo para cada jugador, activando un escudo si un jugador gana dos partidas consecutivas.
Imprime un mensaje si un jugador gana tres partidas consecutivas con escudo activo.

modePvP():

Inicia una partida en modo jugador contra jugador (PvP).

Descripción:
Inicializa los datos de la partida y lee la información de los jugadores desde el archivo.
Realiza un bucle donde ambos jugadores seleccionan sus opciones hasta que uno de ellos logre 3 victorias.
Procesa los resultados de cada ronda usando la función resultadoMatch().
Actualiza las estadísticas de los jugadores en el archivo después de la partida.

modePvE():

Inicia una partida en modo jugador contra máquina (PvE).

Descripción:
Inicializa los datos de la partida y lee la información de los jugadores desde el archivo.
Realiza un bucle donde el jugador 1 selecciona su opción y la máquina elige aleatoriamente una opción hasta que uno de ellos logre 3 victorias.
Procesa los resultados de cada ronda usando la función resultadoMatch().
Actualiza las estadísticas de los jugadores y la máquina en el archivo después de la partida.

Resumen:

Este módulo proporciona las funcionalidades necesarias para gestionar las partidas en el juego, tanto en modo PvP como PvE, incluyendo la inicialización de datos, la lógica de resultados y la actualización de estadísticas de los jugadores. Las funciones permiten un flujo de juego dinámico, interactuando con el usuario para elegir opciones y mostrando resultados en tiempo real.
------------------------------------------------------------------------------Modulo 9, messages:

Este módulo define varios mensajes y menús utilizados en la interfaz del juego, así como funciones para manejar errores y mostrar opciones de los jugadores.

Mensajes y Menús:

agregarOJ: (str) Mensaje que pregunta si se desea agregar otro jugador.

MenuPrin: (str) Menú principal del juego, donde los usuarios pueden 

seleccionar diferentes modos y opciones:

1. Modo Jugador vs Jugador (JvJ)
2. Modo Jugador vs Máquina (JvE)
3. Estadísticas de Juego
4. Tabla de posiciones
5. Salir

MenuJvJ: (str) Menú para el modo Jugador vs Jugador (JvJ):

1. Registre Nombre y Nickname de los Jugadores
2. Inicie sesión del Jugador 1
3. Inicie sesión del Jugador 2
4. Iniciar Partida
5. Salir al menú Principal

MenuJvE: (str) Menú para el modo Jugador vs Máquina (JvE):

1. Registre Nombre y Nickname del Jugador
2. Inicie sesión del Jugador
3. Iniciar Partida
4. Salir al menú Principal

EstadisticasJuego: (str) Menú que muestra las estadísticas del juego:

1. Top 3 Jugadores
2. Jugador último en el Ranking
3. Jugadores que más han perdido contra la IA (Máquina)
4. Promedio de jugadores que le han ganado a la IA (Máquina)
5. Salir al menú Principal

MensajeRegJugador: (str) Mensaje que indica que se está registrando un jugador.

BienvenidoMatch: (str) Mensaje de bienvenida al juego.

OpcionesJuego: (str) Opciones de juego disponibles para los jugadores:

1. Piedra ✊
2. Papel ✋
3. Tijera ✂️

graciasJugar: (str) Mensaje de despedida agradeciendo al jugador por participar.

LoginJugador: (str) Mensaje que solicita al usuario que ingrese el código del jugador para iniciar sesión.

Funciones:

mensajeErro(e)
Imprime un mensaje de error en caso de que ocurra un problema inesperado.

Parámetros:

e: (Exception) Excepción que se produjo, para incluir detalles en el mensaje de error.
Descripción:

La función formatea y muestra el mensaje de error en la consola, facilitando la identificación de problemas.

pOpPlayers(op)
Muestra la opción seleccionada por el jugador en un formato legible.

Parámetros:

op: (int) Opción seleccionada por el jugador (1 para Piedra, 2 para Papel, 3 para Tijera).

Descripción:

Utiliza una declaración match para imprimir el ícono correspondiente a la opción seleccionada. Si la opción no es válida, imprime un mensaje de error indicando que la opción del jugador es inválida.

Resumen:

Este módulo proporciona una interfaz textual para la interacción del usuario en el juego. Incluye mensajes y menús para facilitar la navegación y la selección de opciones, así como funciones para manejar errores y mostrar las elecciones de los jugadores. La claridad de los mensajes y la estructura de los menús son esenciales para mejorar la experiencia del usuario.
------------------------------------------------------------------------------
Modulo 10, player:

Este módulo se encarga de registrar nuevos jugadores, iniciar sesión y mostrar la lista de jugadores registrados. Utiliza otros módulos para manejar la entrada/salida de datos y la gestión de la interfaz.

Importaciones:

import copy: Permite crear copias de objetos, utilizado para manejar el registro de jugadores.
import modules.utils.messages as msg: Importa mensajes predefinidos para mostrar en la interfaz.
import modules.utils.clAndPause as clp: Módulo para limpiar la pantalla y pausar la ejecución.
import modules.utils.dataPlayers as data: Maneja los datos de los jugadores registrados.
import modules.utils.core as core: Contiene funciones para leer y guardar el estado del juego.
from math import e: Importa la constante 'e' de la librería math (aunque no se utiliza en este módulo).

Funciones:

registerP(*game):

Registra un nuevo jugador en el sistema.

Parámetros:

*game: Argumentos opcionales, no utilizados directamente en la función.
Descripción:
Limpia la pantalla e imprime el mensaje de registro.
Crea una copia del objeto Jugador y carga los datos existentes desde un archivo JSON.
Asigna un ID único al nuevo jugador.
Solicita al usuario que ingrese su nombre y nickname.
Verifica si el nickname ya está registrado. Si es así, informa al usuario y vuelve a pedir el registro.
Guarda los datos del jugador en el archivo JSON.
Pregunta si desea agregar otro jugador y repite el proceso si la respuesta es afirmativa.

showPlayers():

Muestra la lista de jugadores registrados.

Descripción:

Carga los datos de jugadores desde el archivo JSON.
Imprime el ID y el nickname de cada jugador registrado en el sistema.
loginP1()
Permite al usuario iniciar sesión como el Jugador 1.

Descripción:

Limpia la pantalla y muestra la lista de jugadores disponibles.
Solicita al usuario que ingrese el código del jugador.
Verifica si el código ingresado existe en el diccionario Jugadores. Si existe, asigna el jugador a Player1 y muestra un mensaje de confirmación.
Si el código no existe o hay un error en la entrada, muestra un mensaje de error correspondiente.

loginP2():

Permite al usuario iniciar sesión como el Jugador 2.

Descripción:

Funciona de manera similar a loginP1, pero asigna el jugador a Player2.
Limpia la pantalla, muestra la lista de jugadores y verifica la entrada del usuario para iniciar sesión.

Resumen:

Este módulo proporciona funciones esenciales para el registro y gestión de jugadores en el juego. Permite a los jugadores registrarse, iniciar sesión y ver otros jugadores. La estructura clara de las funciones y el manejo de errores aseguran una experiencia de usuario fluida. La integración con otros módulos facilita la gestión de datos y la interfaz del juego.
------------------------------------------------------------------------------
Modulo 11, stats:

Este módulo se encarga de mostrar diversas estadísticas relacionadas con los jugadores, incluyendo los mejores jugadores, el último jugador registrado, la tabla de posiciones, las pérdidas contra la IA y el promedio de victorias de los jugadores sobre la IA.

Importaciones:

import copy: Permite crear copias de objetos, aunque no se utiliza en este módulo.
import modules.utils.messages as msg: Importa mensajes predefinidos para mostrar en la interfaz (no utilizado directamente en este módulo).
import modules.utils.clAndPause as clp: Módulo para limpiar la pantalla y pausar la ejecución.
import modules.utils.dataPlayers as data: Maneja los datos de los jugadores registrados (no utilizado directamente en este módulo).
import modules.utils.core as core: Contiene funciones para leer y guardar el estado del juego.

Funciones:

tTres():

Muestra el top 3 de los jugadores con más puntos.

Descripción:

Limpia la pantalla e imprime la lista de los tres mejores jugadores.
Carga los datos de jugadores desde el archivo JSON.
Ordena a los jugadores por sus puntos de mayor a menor.
Imprime el nombre y el nickname de los tres jugadores con más puntos.

lastPGame():

Muestra el último jugador registrado.

Descripción:

Limpia la pantalla e imprime el último jugador en la lista de jugadores.
Carga los datos de jugadores desde el archivo JSON.
Si no hay jugadores registrados, muestra un mensaje indicando que no se encontraron jugadores.
Ordena a los jugadores por sus puntos de mayor a menor y obtiene el último jugador.
Imprime el nombre, el nickname y los puntos del último jugador.

tabla():

Muestra la tabla completa de posiciones de todos los jugadores.

Descripción:

Limpia la pantalla e imprime la tabla de posiciones.
Carga los datos de jugadores desde el archivo JSON.
Ordena a los jugadores por sus puntos de mayor a menor.
Imprime el nombre, el nickname y los puntos de cada jugador en la tabla.

mostLossesAi():

Muestra los jugadores con más pérdidas contra la IA.

Descripción:

Limpia la pantalla e imprime los jugadores con más pérdidas contra la IA.
Carga los datos de jugadores desde el archivo JSON.
Si no hay jugadores registrados, muestra un mensaje indicando que no se encontraron jugadores.
Ordena a los jugadores por el número de partidas perdidas contra la IA de mayor a menor.
Imprime el nombre, el nickname y el número de partidas perdidas de cada jugador.

avgWinsAi():

Calcula y muestra el promedio de jugadores que le han ganado a la IA.

Descripción:

Limpia la pantalla e imprime el promedio de victorias de los jugadores contra la IA.
Carga los datos de la IA desde el archivo JSON.
Calcula el porcentaje de jugadores que le han ganado a la IA y lo imprime.

Resumen:

Este módulo proporciona funciones para mostrar estadísticas clave del juego, tales como los mejores jugadores, el último jugador registrado, la tabla de posiciones, las pérdidas contra la IA y el promedio de victorias. La estructura clara de las funciones y el manejo de la interfaz aseguran que los jugadores puedan ver y comprender fácilmente su desempeño en el juego.