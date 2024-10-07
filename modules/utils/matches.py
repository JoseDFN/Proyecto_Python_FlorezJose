import modules.utils.clAndPause as clp
import modules.utils.messages as msg
import modules.utils.dataPlayers as data
import modules.utils.core as core
import random

global winsP1
global lossesP1
global winsP2
global lossesP2


def initializedata0 (data):
    data['Tie']=0
    data['Player1Wins'] = 0
    data['Player2Wins'] = 0
    data['Player1Losses'] = 0
    data['Player2Losses'] = 0
    data['Player1ConsecutiveWins'] = 0
    data['Player2ConsecutiveWins'] = 0
    data['Player1ShieldActive'] = False
    data['Player2ShieldActive'] = False

def resultadoMatch(oP1, oP2):
    # Procesar el resultado de la partida
    if oP1 == oP2:
        data.partida['Tie'] += 1
        data.partida['Player1ConsecutiveWins'] = 0
        data.partida['Player2ConsecutiveWins'] = 0
    elif (oP1 == 1 and oP2 == 2) or (oP1 == 3 and oP2 == 1):
        # Jugador 2 gana
        data.partida['Player2Wins'] += 1
        data.partida['Player2ConsecutiveWins'] += 1
        data.partida['Player1Losses'] += 1
        data.partida['Player1ConsecutiveWins'] = 0
    elif (oP1 == 2 and oP2 == 1) or (oP1 == 1 and oP2 == 3) or (oP1 == 3 and oP2 == 2):
        # Jugador 1 gana
        data.partida['Player1Wins'] += 1
        data.partida['Player1ConsecutiveWins'] += 1
        data.partida['Player2Losses'] += 1
        data.partida['Player2ConsecutiveWins'] = 0

    # Activar escudo si el jugador gana 2 partidas seguidas
    if data.partida['Player1ConsecutiveWins'] == 2:
        data.partida['Player1ShieldActive'] = True
    elif data.partida['Player2ConsecutiveWins'] == 2:
        data.partida['Player2ShieldActive'] = True

    # Verificar si el escudo está activo y si es la tercera victoria consecutiva
    if data.partida['Player1ShieldActive'] and data.partida['Player1ConsecutiveWins'] == 3:
        print('Jugador 1 ha ganado su tercera partida consecutiva con escudo activo.')
        data.partida['Player1ShieldActive'] = False
    elif data.partida['Player2ShieldActive'] and data.partida['Player2ConsecutiveWins'] == 3:
        print('Jugador 2 ha ganado su tercera partida consecutiva con escudo activo.')
        data.partida['Player2ShieldActive'] = False

def modePvP ():
    while True:
        initializedata0(data.partida)
        game_data = core.ReadFile()
        Player1 = data.partida['Player1']
        Player2 = data.partida['Player2']
        game_data["Jugadores"][str(Player1)]["gPlayed"] += 1
        game_data["Jugadores"][str(Player2)]["gPlayed"] += 1
        clp.limpiar()
        print (msg.BienvenidoMatch)
        while (((data.partida['Player1Wins']) or (data.partida['Player2Wins'])) < 3):
            clp.limpiar()
            print (msg.OpcionesJuego)
            opPlayer1 = int(input('Ingrese la opcion a elegir para Jugador 1: '))
            clp.limpiar()
            print (msg.OpcionesJuego)
            opPlayer2 = int(input('Ingrese la opcion a elegir para Jugador 2: '))
            resultadoMatch(opPlayer1, opPlayer2)
            print(f"Resultado actual: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
            clp.pausar()
        if ((data.partida['Player1Wins']) > (data.partida['Player2Wins'])):
            game_data["Jugadores"][str(Player1)]["wins"] += 1
            game_data["Jugadores"][str(Player1)]["points"] += 2
            game_data["Jugadores"][str(Player2)]["losses"] += 1
            ganador = "Jugador 1"
        else:
            game_data["Jugadores"][str(Player2)]["wins"] += 1
            game_data["Jugadores"][str(Player2)]["points"] += 2
            game_data["Jugadores"][str(Player1)]["losses"] += 1
            ganador = "Jugador 2"
        print(f"\n¡El ganador es {ganador}!")
        print(f"Resultado final: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
        core.save_game(game_data)
        print(msg.graciasJugar)
        break
def modePvE ():
    while True:
        oprandom = [1,2,3]
        initializedata0(data.partida)
        game_data = core.ReadFile()
        Player1 = data.partida['Player1']
        game_data["Jugadores"][str(Player1)]["gPlayed"] += 1
        game_data["Maquina"]["pJugados"] += 1
        clp.limpiar()
        print (msg.BienvenidoMatch)
        while (((data.partida['Player1Wins']) or (data.partida['Player2Wins'])) < 3):
            clp.limpiar()
            print (msg.OpcionesJuego)
            opPlayer1 = int(input('Ingrese la opcion a elegir para Jugador 1: '))
            clp.limpiar()
            opPlayer2 = random.choice(oprandom)
            resultadoMatch(opPlayer1, opPlayer2)
            print(f"Resultado actual: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
            clp.pausar()
        if ((data.partida['Player1Wins']) > (data.partida['Player2Wins'])):
            game_data["Jugadores"][str(Player1)]["gamesWonMachine"] += 1
            game_data["Maquina"]["pPerdidos"] += 1
            ganador = "Jugador 1"
        else:
            game_data["Maquina"]["pGanados"] += 1
            game_data["Jugadores"][str(Player1)]["gamesLostMatchine"] += 1
            ganador = "Jugador 2"
        print(f"\n¡El ganador es {ganador}!")
        print(f"Resultado final: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
        core.save_game(game_data)
        print(msg.graciasJugar)
        break