import modules.utils.clAndPause as clp  # Funciones para limpiar la pantalla y pausar la ejecución
import modules.utils.messages as msg  # Mensajes predefinidos para la interfaz
import modules.utils.player as ch  # Funciones para el manejo de jugadores
import modules.utils.matches as mat  # Funciones para gestionar partidas en modo PvE

def menuPvE(game):  # Función para gestionar el menú de Jugador vs Máquina (PvE)
    isPlayer = True  # Controla el bucle del menú
    userOpPvE = int(0)  # Opción del usuario, inicializada en 0
    
    while isPlayer:  # Bucle para mostrar el menú
        clp.limpiar()  # Limpia la pantalla
        print(msg.MenuJvE)  # Muestra el menú de opciones

        try:
            userOpPvE = int(input('Ingrese la opcion: '))  # Solicita opción al usuario
        except ValueError:  # Captura entrada no numérica
            print('Tipo de opción no válida. Por favor ingrese un número.')
            clp.pausar()  # Pausa para la lectura del mensaje
            continue  # Reinicia el ciclo

        else:
            try:
                # Evalúa la opción ingresada
                match userOpPvE:
                    case 1:  # Registrar nuevo jugador
                        ch.registerP()
                    case 2:  # Iniciar sesión jugador 1
                        ch.loginP1()
                    case 3:  # Iniciar partida en modo PvE
                        mat.modePvE()
                    case 4:  # Salir del menú
                        isPlayer = False  # Termina el bucle
                    case _:  # Opción no válida
                        print("La opcion que ingreso no esta disponible.")
                        clp.pausar()  # Pausa para la lectura del mensaje

            except Exception as e:  # Captura errores no controlados
                msg.mensajeErro(e)  # Muestra mensaje de error
                clp.pausar()  # Pausa antes de continuar
                continue  # Reinicia el ciclo
