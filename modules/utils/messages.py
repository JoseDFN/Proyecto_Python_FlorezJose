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
1. Registre Nombre y Nickname del Jugador 1
2. Inicie sesion del Jugador 1
3. Registre Nombre y Nickname del Jugador 2
4. Inicie sesion del Jugador 2
5. Iniciar Partida
6. Saliral menu Principal
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

MensajeRetroP = "¡Bien hecho!"

MensajeRetroF = "Sigue intentándolo!"
#por si algo agregar ver historial de partidas

def mensajeErro (e):
    print(f"Ha ocurrido un error inesperado: {e}")