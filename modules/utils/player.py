import copy
import modules.utils.messages as msg
import modules.utils.clAndPause as clp
import modules.utils.dataPlayers as data
import modules.utils.core as core
from math import e  # Importa la constante 'e' de la librería mathv

def registerP(*game):
    clp.limpiar()
    print (msg.MensajeRegJugador)
    player = copy.deepcopy(data.Jugador)
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    id = (len(game_data['Jugadores']) + 1)
    try:
        player['name'] = input('Ingrese su nombre: ')
        nick = input('Ingrese su nickname: ')
    except Exception as e:
        msg.mensajeErro(e)
        clp.pausar()
        return registerP()
    for p in game_data['Jugadores'].values():
        if p['nickname'] == nick:
            print('Nickname ya registrado, intente con otro.')
            clp.pausar()
            return registerP()
    player['nickname'] = nick
    #se guarda el jugador con el identificador del id
    game_data['Jugadores'][id] = player

    # Guardar el juego actualizado en el archivo JSON
    core.save_game(game_data)

def showPlayers():
    game_data = core.ReadFile()
    for p in game_data['Jugadores']:
        print(f'ID: {p}, Nickname: {game_data["Jugadores"][p]["nickname"]}')
def loginP1():
    game_data = core.ReadFile()  # Supongo que este método lee y carga correctamente el JSON
    clp.limpiar()  # Asumo que limpia la pantalla o consola
    showPlayers()  # Esta función debe mostrar a los jugadores disponibles
    print(msg.LoginJugador)
    
    try:
        # Pedir entrada al usuario y convertirla en un entero
        opPlayer = int(input("Ingrese el codigo del jugador: "))
        
        # Verificar si el código ingresado existe en el diccionario 'Jugadores'
        if str(opPlayer) in game_data["Jugadores"]:  # Convertir a string ya que las claves son cadenas de texto
            # Asignar el jugador 1
            data.partida['Player1'] = opPlayer
            # Imprimir el nickname del jugador seleccionado
            print(f'{game_data["Jugadores"][str(opPlayer)]["nickname"]} seleccionado como jugador 1')
            clp.pausar ()
        else:
            print(f"El jugador con código {opPlayer} no existe.")
            clp.pausar ()
    
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido.")
        clp.pausar ()
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        clp.pausar ()

def loginP2():
    game_data = core.ReadFile()  # Supongo que este método lee y carga correctamente el JSON
    clp.limpiar()  # Asumo que limpia la pantalla o consola
    showPlayers()  # Esta función debe mostrar a los jugadores disponibles
    print(msg.LoginJugador)
    
    try:
        # Pedir entrada al usuario y convertirla en un entero
        opPlayer = int(input("Ingrese el codigo del jugador: "))
        
        # Verificar si el código ingresado existe en el diccionario 'Jugadores'
        if str(opPlayer) in game_data["Jugadores"]:  # Convertir a string ya que las claves son cadenas de texto
            # Asignar el jugador 1
            data.partida['Player2'] = opPlayer
            # Imprimir el nickname del jugador seleccionado
            print(f'{game_data["Jugadores"][str(opPlayer)]["nickname"]} seleccionado como jugador 2')
            clp.pausar ()
        else:
            print(f"El jugador con código {opPlayer} no existe.")
            clp.pausar ()
    
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido.")
        clp.pausar ()
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        clp.pausar ()