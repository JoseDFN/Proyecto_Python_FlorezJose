import copy  # Importa el módulo para realizar copias profundas de objetos
import modules.utils.messages as msg  # Importa mensajes predefinidos para la interfaz
import modules.utils.clAndPause as clp  # Importa funciones para limpiar la pantalla y pausar la ejecución
import modules.utils.dataPlayers as data  # Importa datos de jugadores
import modules.utils.core as core  # Importa funciones principales del juego
from math import e  # Importa la constante 'e' de la librería math

# Función para registrar un nuevo jugador
def registerP(*game):
    while True:  # Bucle infinito para continuar registrando jugadores hasta que el usuario decida salir
        clp.limpiar()  # Limpia la pantalla
        print(msg.MensajeRegJugador)  # Muestra el mensaje de registro de jugador
        player = copy.deepcopy(data.Jugador)  # Crea una copia del objeto 'Jugador'
        game_data = core.ReadFile()  # Carga los datos del archivo JSON
        id = (len(game_data['Jugadores']) + 1)  # Asigna un ID único al jugador

        try:
            # Solicita el nombre y el nickname del jugador
            player['name'] = input('Ingrese su nombre: ')
            nick = input('Ingrese su nickname: ')
        except Exception as e:  # Maneja excepciones durante la entrada de datos
            msg.mensajeErro(e)  # Muestra un mensaje de error
            clp.pausar()  # Pausa la ejecución
            return registerP()  # Reinicia el registro del jugador

        # Verifica si el nickname ya está registrado
        for p in game_data['Jugadores'].values():
            if p['nickname'] == nick:
                print('Nickname ya registrado, intente con otro.')  # Mensaje de error si el nickname existe
                clp.pausar()  # Pausa la ejecución
                return registerP()  # Reinicia el registro del jugador

        player['nickname'] = nick  # Asigna el nickname al jugador
        game_data['Jugadores'][id] = player  # Guarda el jugador con el identificador del id

        # Guarda el juego actualizado en el archivo JSON
        core.save_game(game_data)
        
        # Pregunta al usuario si desea agregar otro jugador
        confimacion = input('Desea agregar otro jugador (S/ N u otra tecla)? ').upper()
        if confimacion != 'S':  # Si la respuesta no es 'S', sale del bucle
            break
        else:
            continue  # Continúa el bucle para registrar otro jugador

# Función para mostrar la lista de jugadores registrados
def showPlayers():
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    # Imprime el ID y el nickname de cada jugador registrado
    for p in game_data['Jugadores']:
        print(f'ID: {p}, Nickname: {game_data["Jugadores"][p]["nickname"]}')

# Función para iniciar sesión del jugador 1
def loginP1():
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    clp.limpiar()  # Limpia la pantalla
    showPlayers()  # Muestra la lista de jugadores disponibles
    print(msg.LoginJugador)  # Muestra el mensaje para iniciar sesión
    
    try:
        # Solicita la entrada del usuario y la convierte en un entero
        opPlayer = int(input("Ingrese el código del jugador: "))
        
        # Verifica si el código ingresado existe en el diccionario 'Jugadores'
        if str(opPlayer) in game_data["Jugadores"]:  # Convierte a string ya que las claves son cadenas
            data.partida['Player1'] = opPlayer  # Asigna el jugador 1
            print(f'{game_data["Jugadores"][str(opPlayer)]["nickname"]} seleccionado como jugador 1')  # Imprime el nickname del jugador seleccionado
            clp.pausar()  # Pausa la ejecución
        else:
            print(f"El jugador con código {opPlayer} no existe.")  # Mensaje si el jugador no existe
            clp.pausar()  # Pausa la ejecución
    
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido.")  # Mensaje si la entrada no es un número
        clp.pausar()  # Pausa la ejecución
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")  # Maneja excepciones inesperadas
        clp.pausar()  # Pausa la ejecución

# Función para iniciar sesión del jugador 2
def loginP2():
    game_data = core.ReadFile()  # Carga los datos del archivo JSON
    clp.limpiar()  # Limpia la pantalla
    showPlayers()  # Muestra la lista de jugadores disponibles
    print(msg.LoginJugador)  # Muestra el mensaje para iniciar sesión
    
    try:
        # Solicita la entrada del usuario y la convierte en un entero
        opPlayer = int(input("Ingrese el código del jugador: "))
        
        # Verifica si el código ingresado existe en el diccionario 'Jugadores'
        if str(opPlayer) in game_data["Jugadores"]:  # Convierte a string ya que las claves son cadenas
            data.partida['Player2'] = opPlayer  # Asigna el jugador 2
            print(f'{game_data["Jugadores"][str(opPlayer)]["nickname"]} seleccionado como jugador 2')  # Imprime el nickname del jugador seleccionado
            clp.pausar()  # Pausa la ejecución
        else:
            print(f"El jugador con código {opPlayer} no existe.")  # Mensaje si el jugador no existe
            clp.pausar()  # Pausa la ejecución
    
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido.")  # Mensaje si la entrada no es un número
        clp.pausar()  # Pausa la ejecución
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")  # Maneja excepciones inesperadas
        clp.pausar()  # Pausa la ejecución
