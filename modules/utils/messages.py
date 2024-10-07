agregarOJ = """¿Desea agregar otro jugador (S/N u otro)?"""
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

MenuJvJ = """
  ___________________________
 °                           °
|          𝕄𝕖𝕟𝕦 𝕁𝕧𝕁          |
 °___________________________°
1. Registre Nombre y Nickname de los Jugadores
2. Inicie sesion del Jugador 1
3. Inicie sesion del Jugador 2
4. Iniciar Partida
5. Saliral menu Principal
"""

MenuJvE = """
  ___________________________
 °                           °
|          𝕄𝕖𝕟𝕦 𝕁𝕧𝔼          |
 °___________________________°
1. Registre Nombre y Nickname del Jugador
2. Inicie sesion del Jugador
3. Iniciar Partida
4. Saliral menu Principal
"""

EstadisticasJuego = """
  ___________________________
 °                           °
|    𝔼𝕤𝕥𝕒𝕕𝕚́𝕤𝕥𝕚𝕔𝕒𝕤 𝕕𝕖𝕝 𝕁𝕦𝕖𝕘𝕠    |
 °___________________________°
1. Top 3 Jugadores
2. Jugador ultimo en el Ranking
3. Jugadores que mas han perdido contra la IA (Maquina)
4. Promedio de jugadores que le han ganado a la IA (Maquina)
5. Saliral menu Principal
"""

MensajeRegJugador = """
  ___________________________
 °                           °
|     ℝ𝕖𝕘𝕚𝕤𝕥𝕣𝕒𝕟𝕕𝕠 𝕁𝕦𝕘𝕒𝕕𝕠𝕣     |
 °___________________________°
"""

BienvenidoMatch = """
  ___________________________
 °                           °
|     𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒𝕝 𝕁𝕦𝕖𝕘𝕠     |
 °___________________________°
"""

OpcionesJuego = """
1.Piedra ✊
2.Papel ✋
3.Tijera ✂️
"""

graciasJugar = "Gracias por jugar. ¡Hasta la próxima!"

LoginJugador = "Ingrese codigo del jugador a logearse: "

def mensajeErro (e):
    print(f"Ha ocurrido un error inesperado: {e}")