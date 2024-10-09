import modules.utils.clAndPause as clp  # Funciones para limpiar la pantalla y pausar la ejecución
import modules.utils.messages as msg  # Mensajes predefinidos para la interfaz
import modules.utils.stats as st  # Funciones para manejar estadísticas del juego

def EstadisticasJuego(game):  # Función para gestionar las estadísticas del juego
    isPlayer = True  # Controla el bucle de estadísticas
    userOpPvE = int(0)  # Opción del usuario, inicializada en 0

    while isPlayer:  # Bucle para mostrar estadísticas
        clp.limpiar()  # Limpia la pantalla
        print(msg.EstadisticasJuego)  # Muestra el menú de estadísticas

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
                    case 1:  # Mostrar el top 3 de jugadores
                        st.tTres()
                    case 2:  # Mostrar el último jugador en el ranking
                        st.lastPGame()
                    case 3:  # Mostrar jugadores con más pérdidas contra la IA
                        st.mostLossesAi()
                    case 4:  # Mostrar promedio de jugadores ganadores contra la IA
                        st.avgWinsAi()
                    case 5:  # Salir del menú
                        isPlayer = False  # Termina el bucle
                    case _:  # Opción no válida
                        print("La opcion que ingreso no esta disponible.")
                        clp.pausar()  # Pausa para la lectura del mensaje

            except Exception as e:  # Captura errores no controlados
                msg.mensajeErro(e)  # Muestra mensaje de error
                clp.pausar()  # Pausa antes de continuar
                continue  # Reinicia el ciclo
