import modules.utils.clAndPause as clp
import modules.utils.messages as msg
import modules.utils.player as ch
import modules.utils.matches as mat

def menuPvE (game):
    isPlayer = True
    userOpPvE = int(0)
    while isPlayer:
        clp.limpiar()
        print (msg.MenuJvE)
        try:
            userOpPvE = int(input('Ingrese la opcion: '))
        except ValueError:
            # En caso de que el usuario ingrese algo que no sea un número.
            print('Tipo de opción no válida. Por favor ingrese un número.')
            clp.pausar()
            continue
        else:
            try:
                match userOpPvE:
                    case 1:
                        ch.registerP()
                    case 2:
                        ch.loginP1()
                    case 3:
                        mat.modePvE()
                    case 4:
                        isPlayer = False
                    case _:
                        print("La opcion que ingreso no esta disponible.")
                        clp.pausar()
            except Exception as e:
                msg.mensajeErro(e)
                clp.pausar()
                continue