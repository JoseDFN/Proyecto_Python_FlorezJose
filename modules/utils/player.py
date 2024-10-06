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