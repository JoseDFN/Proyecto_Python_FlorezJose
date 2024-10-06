import modules.utils.clAndPause as clp
import modules.utils.messages as msg
import modules.utils.core as cf
from math import e  # Importa la constante 'e' de la librería math

if (__name__ == '__main__'):
    Juego = {
        'Jugadores':{},
        'Maquina':{
            'pJugados': 0,
            'pGanados': 0,
            'pPerdidos':0,
            'puntosT': 0
        }
    }
    cf.MY_DATABASE = 'data/PPoT.json'  # Assign the MY_DATABASE variable
    cf.checkFile(Juego)
    clp.limpiar()
    print (msg.MenuPrin)
    userOp = int(input('Ingrese el menu a entrar: '))
    match userOp:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass