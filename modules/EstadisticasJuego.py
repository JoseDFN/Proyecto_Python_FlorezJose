import modules.utils.clAndPause as clp
import modules.utils.messages as msg

def EstadisticasJuego (Juego):
    isPlayer = True
    userOpPvE = int(0)
    while isPlayer:
        clp.limpiar()
        print (msg.EstadisticasJuego)
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
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
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