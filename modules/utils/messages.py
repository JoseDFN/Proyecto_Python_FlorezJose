# Mensajes de interacción con el usuario
agregarOJ = """¿Desea agregar otro jugador (S/N u otro)?"""  # Pregunta para agregar más jugadores

# Menú principal del juego
MenuPrin = """
  ___________________________
 °                           °
|        𝕄𝕖𝕟𝕦 ℙ𝕣𝕚𝕔𝕚𝕡𝕒𝕝        |
 °___________________________° 
1. Modo Jugador vs Jugador (JvJ)
2. Modo Jugador vs Máquina (JvE) 
3. Estadisticas de Juego         
4. Tabla de posiciones            
5. Salir                         
"""

# Menú para el modo Jugador vs Jugador
MenuJvJ = """
  ___________________________
 °                           ° 
|          𝕄𝕖𝕟𝕦 𝕁𝕧𝕁          |
 °___________________________° 
1. Registre Nombre y Nickname de los Jugadores  
2. Inicie sesion del Jugador 1                   
3. Inicie sesion del Jugador 2                 
4. Iniciar Partida                           
5. Salir al menú Principal                   
"""

# Menú para el modo Jugador vs Máquina
MenuJvE = """
  ___________________________
 °                           ° 
|          𝕄𝕖𝕟𝕦 𝕁𝕧𝔼          |
 °___________________________° 
1. Registre Nombre y Nickname del Jugador 
2. Inicie sesion del Jugador                
3. Iniciar Partida                           
4. Salir al menú Principal                   
"""

# Menú para ver estadísticas del juego
EstadisticasJuego = """
  ___________________________
 °                           ° 
|    𝔼𝕤𝕥𝕒𝕕𝕚́𝕤𝕥𝕚𝕔𝕒𝕤 𝕕𝕖𝕝 𝕁𝕦𝕖𝕘𝕠    |
 °___________________________° 
1. Top 3 Jugadores                         
2. Jugador último en el Ranking             
3. Jugadores que más han perdido contra la IA (Máquina)  
4. Promedio de jugadores que le han ganado a la IA (Máquina) 
5. Salir al menú Principal                  
"""

# Mensaje al registrar un nuevo jugador
MensajeRegJugador = """
  ___________________________
 °                           ° 
|     ℝ𝕖𝕘𝕚𝕤𝕥𝕣𝕒𝕟𝕕𝕠 𝕁𝕦𝕘𝕒𝕕𝕠𝕣     |
 °___________________________° 
"""

# Mensaje de bienvenida al juego
BienvenidoMatch = """
  ___________________________
 °                           ° 
|     𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒𝕝 𝕁𝕦𝕖𝕘𝕠     |
 °___________________________° 
"""

# Opciones de juego disponibles
OpcionesJuego = """
1. Piedra ✊
2. Papel ✋
3. Tijera ✂️
"""

# Mensaje de despedida al salir del juego
graciasJugar = "Gracias por jugar. ¡Hasta la próxima!"

# Mensaje para solicitar el código del jugador al iniciar sesión
LoginJugador = "Ingrese código del jugador a logearse: "

# Función para manejar errores inesperados
def mensajeErro(e):
    print(f"Ha ocurrido un error inesperado: {e}")  # Imprime un mensaje de error

# Función para mostrar la opción seleccionada por los jugadores
def pOpPlayers(op):
    match op:
        case 1:
            print("1. Piedra ✊")  # Opción seleccionada: Piedra
        case 2:
            print("2. Papel ✋")   # Opción seleccionada: Papel
        case 3:
            print("3. Tijera ✂️")  # Opción seleccionada: Tijera
        case _:
            print("Opción del jugador inválida")  # Mensaje para opción inválida
