import copy
import modules.utils.messages as msg
import modules.utils.clAndPause as clp
import modules.utils.dataPlayers as data
import modules.utils.core as core

def tTres ():
    game_data = core.ReadFile()
    jugadores = game_data["Jugadores"]
    # Convertir los jugadores a una lista de diccionarios
    jugadores_list = [jugadores[key] for key in jugadores]

    # Ordenar la lista de jugadores según los puntos de mayor a menor
    sPlayers = sorted(jugadores_list, key=lambda player: player['points'], reverse=True)

    for idx, player in enumerate(sPlayers[:3], start=1):
        print(f"Top {idx}: {player['name']} ({player['nickname']}) with {player['points']} points")
    clp.pausar()
def lastPGame():
    game_data = core.ReadFile()
    jugadores = game_data["Jugadores"]
    
    if not jugadores:
        print("No se encontraron jugadores.")
        return

    # Convertir los jugadores a una lista de diccionarios
    jugadores_list = [jugadores[key] for key in jugadores]

    # Ordenar la lista de jugadores según los puntos de mayor a menor
    sPlayers = sorted(jugadores_list, key=lambda player: player['points'], reverse=True)

    # Obtener el último jugador en la lista ordenada
    lPlayer = sPlayers[-1]
    
    # Imprimir los detalles del último jugador
    print(f"Último jugador: {lPlayer['name']} ({lPlayer['nickname']}) con {lPlayer['points']} puntos")
    
    clp.pausar()

