import copy  # Importa el módulo para realizar copias profundas de objetos
import modules.utils.messages as msg  # Importa mensajes predefinidos para la interfaz
import modules.utils.clAndPause as clp  # Importa funciones para limpiar la pantalla y pausar la ejecución
import modules.utils.dataPlayers as data  # Importa datos de jugadores
import modules.utils.core as core  # Importa funciones principales del juego

# Función para mostrar el top 3 jugadores
def tTres():
    clp.limpiar()  # Limpia la pantalla
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    jugadores = game_data["Jugadores"]  # Accede a los jugadores en el JSON
    # Convierte los jugadores a una lista de diccionarios
    jugadores_list = [jugadores[key] for key in jugadores]

    # Ordena la lista de jugadores según los puntos de mayor a menor
    sPlayers = sorted(jugadores_list, key=lambda player: player['points'], reverse=True)

    # Muestra los tres jugadores con más puntos
    for idx, player in enumerate(sPlayers[:3], start=1):
        print(f"Top {idx}: {player['name']} ({player['nickname']}) con {player['points']} puntos")
    clp.pausar()  # Pausa la ejecución para que el usuario pueda ver el resultado

# Función para mostrar el último jugador registrado en el ranking
def lastPGame():
    clp.limpiar()  # Limpia la pantalla
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    jugadores = game_data["Jugadores"]  # Accede a los jugadores en el JSON
    
    if not jugadores:  # Verifica si hay jugadores registrados
        print("No se encontraron jugadores.")  # Mensaje si no hay jugadores
        return

    # Convierte los jugadores a una lista de diccionarios
    jugadores_list = [jugadores[key] for key in jugadores]

    # Ordena la lista de jugadores según los puntos de mayor a menor
    sPlayers = sorted(jugadores_list, key=lambda player: player['points'], reverse=True)

    # Obtiene el último jugador en la lista ordenada
    lPlayer = sPlayers[-1]
    
    # Imprime los detalles del último jugador
    print(f"Último jugador: {lPlayer['name']} ({lPlayer['nickname']}) con {lPlayer['points']} puntos")
    
    clp.pausar()  # Pausa la ejecución

# Función para mostrar la tabla de posiciones de todos los jugadores
def tabla():
    clp.limpiar()  # Limpia la pantalla
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    jugadores = game_data["Jugadores"]  # Accede a los jugadores en el JSON
    # Convierte los jugadores a una lista de diccionarios
    jugadores_list = [jugadores[key] for key in jugadores]

    # Ordena la lista de jugadores según los puntos de mayor a menor
    sPlayers = sorted(jugadores_list, key=lambda player: player['points'], reverse=True)

    # Muestra la tabla de posiciones
    for idx, player in enumerate(sPlayers, start=1):
        print(f"Top {idx}: {player['name']} ({player['nickname']}) con {player['points']} puntos")
    clp.pausar()  # Pausa la ejecución

# Función para mostrar los jugadores que más han perdido contra la IA
def mostLossesAi():
    clp.limpiar()  # Limpia la pantalla
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    jugadores = game_data["Jugadores"]  # Accede a los jugadores en el JSON
    
    if not jugadores:  # Verifica si hay jugadores registrados
        print("No se encontraron jugadores.")  # Mensaje si no hay jugadores
        return

    # Convierte los jugadores a una lista de diccionarios
    jugadores_list = [jugadores[key] for key in jugadores]

    # Ordena la lista de jugadores según el número de partidas perdidas contra la IA
    sPlayers = sorted(jugadores_list, key=lambda player: player['gamesLostMatchine'], reverse=True)

    # Muestra los jugadores que más han perdido contra la IA
    for idx, player in enumerate(sPlayers, start=1):
        print(f"Top {idx}: {player['name']} ({player['nickname']}) con {player['gamesLostMatchine']} partidas perdidas contra la IA")
    clp.pausar()  # Pausa la ejecución

# Función para calcular y mostrar el promedio de jugadores que han ganado a la IA
def avgWinsAi():
    clp.limpiar()  # Limpia la pantalla
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    # Calcula el promedio de jugadores que le han ganado a la IA
    prom = ((game_data["Maquina"]["pPerdidos"]) / (game_data["Maquina"]["pJugados"])) * 100
    print(f"El promedio de jugadores que le han ganado a la IA es: {round(prom, 2)}%")  # Muestra el promedio
    clp.pausar()  # Pausa la ejecución
