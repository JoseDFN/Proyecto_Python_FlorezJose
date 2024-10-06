import modules.utils.clAndPause as clp
import modules.utils.messages as msg
import modules.utils.player as ch

def menuPvP (*game):
    isPlayer = True
    userOpPvP = int(0)
    while isPlayer:
        clp.limpiar()
        print (msg.MenuJvJ)
        try:
            userOpPvP = int(input('Ingrese la opcion: '))
        except ValueError:
            # En caso de que el usuario ingrese algo que no sea un número.
            print('Tipo de opción no válida. Por favor ingrese un número.')
            clp.pausar()
            continue
        else:
            try:
                match userOpPvP:
                    case 1:
                        ch.registerP(game)
                    case 2:
                        ch.loginP1()
                    case 3:
                        ch.loginP2()
                    case 4:
                        pass
                    case 5:
                        isPlayer = False
                    case _:
                        print("La opcion que ingreso no esta disponible.")
                        clp.pausar()
            except Exception as e:
                msg.mensajeErro(e)
                clp.pausar()
                continue