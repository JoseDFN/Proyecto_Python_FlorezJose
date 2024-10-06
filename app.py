import modules.utils.clAndPause as clp
import modules.utils.messages as msg
import modules.utils.core as cf
import modules.PvPMode as pvpMode
from math import e  # Importa la constante 'e' de la librería math


if (__name__ == '__main__'):
    userOp = int(0)
    isGame = True
    Juego = {
        'Jugadores':{},
        'Maquina':{
            'pJugados': 0,
            'pGanados': 0,
            'pPerdidos':0,
            'puntosT': 0
        }
    }
    while isGame:
        cf.MY_DATABASE = 'data/PPoT.json'  # Assign the MY_DATABASE variable
        cf.checkFile(Juego)
        clp.limpiar()
        print (msg.MenuPrin)
        try:
            userOp = int(input('Ingrese el menu a entrar: '))
        except ValueError:
            # En caso de que el usuario ingrese algo que no sea un número.
            print('Tipo de opción no válida. Por favor ingrese un número.')
            clp.pausar()
            continue
        else:
            try:
                match userOp:
                    case 1:
                        pvpMode.menuPvP(Juego)
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        isGame = False
                    case _:
                        print("La opcion que ingreso no esta disponible.")
                        clp.pausar()
            except Exception as e:
                msg.mensajeErro(e)
                clp.pausar()
                continue