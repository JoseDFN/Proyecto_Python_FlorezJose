import modules.utils.clAndPause as clp
import modules.utils.messages as msg
import modules.utils.dataPlayers as data
import modules.utils.core as core
import random

# Variables globales para llevar la cuenta de victorias y derrotas de los jugadores
global winsP1
global lossesP1
global winsP2
global lossesP2

def initializedata0(data):
    # Inicializa los datos de la partida
    data['Tie'] = 0
    data['Player1Wins'] = 0
    data['Player2Wins'] = 0
    data['Player1Losses'] = 0
    data['Player2Losses'] = 0
    data['Player1ConsecutiveWins'] = 0
    data['Player2ConsecutiveWins'] = 0
    data['Player1ShieldActive'] = False
    data['Player2ShieldActive'] = False

def resultadoMatch(oP1, oP2):
    # Procesa el resultado del match entre dos jugadores
    wP1 = False
    wP2 = False
    # Empate
    if oP1 == oP2:
        data.partida['Tie'] += 1
        data.partida['Player1ConsecutiveWins'] = 0
        data.partida['Player2ConsecutiveWins'] = 0
    # Jugador 2 gana
    elif (oP1 == 1 and oP2 == 2) or (oP1 == 3 and oP2 == 1) or (oP1 == 2 and oP2 == 3):
        wP2 = True
        if (wP2 and data.partida['Player1ShieldActive']):
            print('Movimiento Bloqueado')  # Jugador 1 tiene escudo, movimiento bloqueado
            data.partida['Player1ShieldActive'] = False
            data.partida['Player1ConsecutiveWins'] = 0
        else:
            data.partida['Player2Wins'] += 1
            data.partida['Player2ConsecutiveWins'] += 1
            data.partida['Player1Losses'] += 1
            data.partida['Player1ConsecutiveWins'] = 0
    # Jugador 1 gana
    elif (oP1 == 2 and oP2 == 1) or (oP1 == 1 and oP2 == 3) or (oP1 == 3 and oP2 == 2):
        wP1 = True
        if (wP1 and data.partida['Player2ShieldActive']):
            print('Movimiento Bloqueado')  # Jugador 2 tiene escudo, movimiento bloqueado
            data.partida['Player2ShieldActive'] = False
            data.partida['Player2ConsecutiveWins'] = 0
        else:
            data.partida['Player1Wins'] += 1
            data.partida['Player1ConsecutiveWins'] += 1
            data.partida['Player2Losses'] += 1
            data.partida['Player2ConsecutiveWins'] = 0

    # Activar escudo si el jugador gana 2 partidas consecutivas
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

def modePvP():
    # Modo de juego PvP (Jugador vs Jugador)
    while True:
        oprandom = [1, 2, 3]  # Opciones de juego
        initializedata0(data.partida)  # Inicializa los datos de la partida
        game_data = core.ReadFile()  # Lee los datos del juego
        Player1 = data.partida['Player1']  # ID del jugador 1
        Player2 = data.partida['Player2']  # ID del jugador 2
        # Incrementar total de partidas jugadas por ambos jugadores
        game_data["Jugadores"][str(Player1)]["gPlayed"] += 1
        game_data["Jugadores"][str(Player2)]["gPlayed"] += 1
        
        clp.limpiar()  # Limpiar la pantalla
        print(msg.BienvenidoMatch)  # Mensaje de bienvenida

        # Jugar hasta que uno de los jugadores gane 3 partidas
        while ((data.partida['Player1Wins'] or data.partida['Player2Wins']) < 3):
            opPlayer1 = int(0)
            opPlayer2 = int(0)
            clp.limpiar()
            print(msg.OpcionesJuego)  # Mostrar opciones de juego

            # Obtener opción del jugador 1
            try:
                opPlayer1 = int(input('Ingrese la opcion a elegir para Jugador 1: '))
                while opPlayer1 not in oprandom:
                    print("Opcion invalida")
                    opPlayer1 = int(input('Ingrese la opcion a elegir para Jugador 1: '))
            except ValueError:
                # Manejo de error si la entrada no es un número
                print('Tipo de opción no válida. Por favor ingrese un número.')
                clp.pausar()
                continue
            
            clp.limpiar()
            print(msg.OpcionesJuego)  # Mostrar opciones de juego nuevamente

            # Obtener opción del jugador 2
            try:
                opPlayer2 = int(input('Ingrese la opcion a elegir para Jugador 2: '))
                while opPlayer2 not in oprandom:
                    print("Opcion invalida")
                    opPlayer2 = int(input('Ingrese la opcion a elegir para Jugador 2: '))
            except ValueError:
                # Manejo de error si la entrada no es un número
                print('Tipo de opción no válida. Por favor ingrese un número.')
                clp.pausar()
                continue

            clp.limpiar()  # Limpiar la pantalla
            resultadoMatch(opPlayer1, opPlayer2)  # Procesar el resultado de la partida
            
            # Mostrar elecciones y resultados
            print("La opcion que selecciono el jugador 1 es: ")
            msg.pOpPlayers(opPlayer1)
            print("La opcion que selecciono el jugador 2 es: ")
            msg.pOpPlayers(opPlayer2)
            print(f"Resultado actual: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
            clp.pausar()  # Pausar para mostrar el resultado
            
        # Actualizar datos finales después de 3 victorias
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
            
        # Mostrar el ganador y los resultados finales
        print(f"\n¡El ganador es {ganador}!")
        print(f"Resultado final: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
        core.save_game(game_data)  # Guardar los datos del juego
        print(msg.graciasJugar)  # Mensaje de despedida
        break

def modePvE():
    # Modo de juego PvE (Jugador vs Máquina)
    while True:
        oprandom = [1, 2, 3]  # Opciones de juego
        initializedata0(data.partida)  # Inicializa los datos de la partida
        game_data = core.ReadFile()  # Lee los datos del juego
        Player1 = data.partida['Player1']  # ID del jugador 1
        # Incrementar total de partidas jugadas
        game_data["Jugadores"][str(Player1)]["gPlayed"] += 1
        game_data["Maquina"]["pJugados"] += 1
        
        clp.limpiar()  # Limpiar la pantalla
        print(msg.BienvenidoMatch)  # Mensaje de bienvenida

        # Jugar hasta que uno de los jugadores gane 3 partidas
        while (((data.partida['Player1Wins'] or data.partida['Player2Wins'])) < 3):
            opPlayer1 = int(0)
            opPlayer2 = int(0)
            clp.limpiar()
            print(msg.OpcionesJuego)  # Mostrar opciones de juego

            # Obtener opción del jugador 1
            try:
                opPlayer1 = int(input('Ingrese la opcion a elegir para Jugador 1: '))
                while opPlayer1 not in oprandom:
                    print("Opcion invalida")
                    opPlayer1 = int(input('Ingrese la opcion a elegir para Jugador 1: '))
            except ValueError:
                # Manejo de error si la entrada no es un número
                print('Tipo de opción no válida. Por favor ingrese un número.')
                clp.pausar()
                continue
            
            clp.limpiar()
            opPlayer2 = random.choice(oprandom)  # Opción aleatoria para la máquina
            resultadoMatch(opPlayer1, opPlayer2)  # Procesar el resultado de la partida
            
            # Mostrar elecciones y resultados
            print("La opcion que selecciono el jugador 1 es: ")
            msg.pOpPlayers(opPlayer1)
            print("La opcion que selecciono el jugador 2 es: ")
            msg.pOpPlayers(opPlayer2)
            print(f"Resultado actual: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
            clp.pausar()  # Pausar para mostrar el resultado
            
        # Actualizar datos finales después de 3 victorias
        if ((data.partida['Player1Wins']) > (data.partida['Player2Wins'])):
            game_data["Jugadores"][str(Player1)]["gamesWonMachine"] += 1
            game_data["Maquina"]["pPerdidos"] += 1
            ganador = "Jugador 1"
        else:
            game_data["Maquina"]["pGanados"] += 1
            game_data["Jugadores"][str(Player1)]["gamesLostMatchine"] += 1
            ganador = "Jugador 2"
        
        # Mostrar el ganador y los resultados finales
        print(f"\n¡El ganador es {ganador}!")
        print(f"Resultado final: Jugador 1: {data.partida['Player1Wins']} - Jugador 2: {data.partida['Player2Wins']}")
        core.save_game(game_data)  # Guardar los datos del juego
        print(msg.graciasJugar)  # Mensaje de despedida
        clp.pausar()
        break