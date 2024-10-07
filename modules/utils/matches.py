import modules.utils.clAndPause as clp
import modules.utils.messages as msg
import modules.utils.dataPlayers as data
import modules.utils.core as core

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

def resultadoMatch (oP1, oP2):
    if (data.partida['Player1ShieldActive'] or data.partida['Player2ShieldActive']):
        print('Movimiento bloqueado por escudo')
        data.partida['Player1ShieldActive'] = False
        data.partida['Player2ShieldActive'] = False
        data.partida['Player1ConsecutiveWins'] = 0
        data.partida['Player2ConsecutiveWins'] = 0
    else:
        if oP1 == oP2:
            data.partida['Tie'] += 1
            data.partida['Player1ConsecutiveWins'] = 0
            data.partida['Player2ConsecutiveWins'] = 0
        elif (oP1 == 1) and (oP2 == 2):
            data.partida['Player2Wins'] += 1
            data.partida['Player2ConsecutiveWins'] += 1
            data.partida['Player1Losses'] += 1
        elif (oP1 == 2) and (oP2 == 1):
            data.partida['Player1Wins'] += 1
            data.partida['Player1ConsecutiveWins'] += 1
            data.partida['Player2Losses'] += 1
        elif (oP1 == 1) and (oP2 == 3):
            data.partida['Player1Wins'] += 1
            data.partida['Player1ConsecutiveWins'] += 1
            data.partida['Player2Losses'] += 1
        elif (oP1 == 3) and (oP2 == 1):
            data.partida['Player2Wins'] += 1
            data.partida['Player2ConsecutiveWins'] += 1
            data.partida['Player1Losses'] += 1
        elif (oP1 == 2) and (oP2 == 3):
            data.partida['Player2Wins'] += 1
            data.partida['Player2ConsecutiveWins'] += 1
            data.partida['Player1Losses'] += 1
        elif (oP1 == 3) and (oP2 == 2):
            data.partida['Player1Wins'] += 1
            data.partida['Player1ConsecutiveWins'] += 1
            data.partida['Player2Losses'] += 1
    if data.partida['Player1ConsecutiveWins'] == 2:
        data.partida['Player1ShieldActive'] = True
    elif data.partida['Player2ConsecutiveWins'] == 2:
        data.partida['Player2ShieldActive'] = True

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
        game_data["Jugadores"][str(Player1)]["points"] = (data.partida['Player1Wins'])*2
        game_data["Jugadores"][str(Player2)]["points"] = (data.partida['Player2Wins'])*2
        if ((data.partida['Player1Wins']) > (data.partida['Player2Wins'])):
            game_data["Jugadores"][str(Player1)]["wins"] += 1
            game_data["Jugadores"][str(Player2)]["losses"] += 1
            ganador = "Jugador 1"
        else:
            game_data["Jugadores"][str(Player2)]["wins"] += 1
            game_data["Jugadores"][str(Player1)]["losses"] += 1
            ganador = "Jugador 2"
        print(f"\n¡El ganador es {ganador}!")
        print(f"Resultado final: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
        core.save_game(game_data)
        print(msg.graciasJugar)
        break