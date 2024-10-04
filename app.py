import modules.utils.clAndPause as clp
import modules.utils.mensajes as msg
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
    cf.MY_DATABASE='data/PPoT.json'
    cf.checkFile(Juego)
    clp.limpiar()
    print (msg.MenuPrin)
    userOp = int(input('Ingrese el menu a entrar: '))