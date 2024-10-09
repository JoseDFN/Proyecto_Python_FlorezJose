import modules.utils.clAndPause as clp  # Funciones para limpiar la pantalla y pausar la ejecución
import modules.utils.messages as msg  # Mensajes predefinidos para la interfaz
import modules.utils.core as cf  # Funciones centrales para la lógica del juego
import modules.PvPMode as pvpMode  # Módulo para el modo Jugador vs Jugador
import modules.PvEMode as pveMode  # Módulo para el modo Jugador vs Máquina
import modules.EstadisticasJuego as statsG  # Módulo para estadísticas del juego
from math import e  # Importa la constante 'e' de math
import modules.utils.stats as st  # Funciones para manejar estadísticas
import os

if (__name__ == '__main__'):  # Verifica si se ejecuta como programa principal
    userOp = int(0)  # Opción del usuario inicializada en 0
    isGame = True  # Controla el bucle principal del juego
    # Diccionario que almacena jugadores y estadísticas de la máquina
    Game = {
        'Jugadores': {},
        'Maquina': {
            'pJugados': 0,
            'pGanados': 0,
            'pPerdidos': 0
        }
    }
    
    while isGame:  # Bucle principal del juego
        cf.MY_DATABASE = 'data/PPoT.json'  # Asigna la ruta del archivo JSON
        cf.checkFile(Game)  # Verifica existencia y estructura del archivo JSON
        clp.limpiar()  # Limpia la pantalla
        print(msg.MenuPrin)  # Muestra el menú principal

        try:
            userOp = int(input('Ingrese el menu a entrar: '))  # Solicita opción al usuario
        except ValueError:  # Captura entrada no numérica
            print('Tipo de opción no válida. Por favor ingrese un número.')
            clp.pausar()  # Pausa para la lectura del mensaje
            continue  # Reinicia el ciclo

        else:
            try:
                # Evalúa la opción ingresada
                match userOp:
                    case 1:  # Modo Jugador vs Jugador
                        pvpMode.menuPvP(cf.MY_DATABASE)
                    case 2:  # Modo Jugador vs Máquina
                        pveMode.menuPvE(cf.MY_DATABASE)
                    case 3:  # Mostrar estadísticas del juego
                        statsG.EstadisticasJuego(cf.MY_DATABASE)
                    case 4:  # Mostrar tabla de posiciones
                        st.tabla()
                    case 5:  # Salir del juego
                        clp.limpiar()  # Limpia la pantalla antes de salir
                        isGame = False  # Termina el bucle
                    case _:  # Opción no válida
                        print("La opcion que ingreso no esta disponible.")
                        clp.pausar()  # Pausa para la lectura del mensaje

            except Exception as e:  # Captura errores no controlados
                msg.mensajeErro(e)  # Muestra mensaje de error
                clp.pausar()  # Pausa antes de continuar
                continue  # Reinicia el ciclo