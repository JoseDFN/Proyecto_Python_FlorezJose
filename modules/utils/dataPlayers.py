# Diccionario que representa un jugador
Jugador = {
    'name': '',  # Nombre del jugador
    'nickname': '',  # Apodo del jugador
    'wins': 0,  # Partidas ganadas
    'losses': 0,  # Partidas perdidas
    'points': 0,  # Puntos acumulados
    'gPlayed': 0,  # Total de partidas jugadas
    'gamesLostMatchine': 0,  # Partidas perdidas contra la IA
    'gamesWonMachine': 0  # Partidas ganadas contra la IA
}

# Diccionario que representa el estado de una partida
partida = {
    'Player1': 0,  # ID del jugador 1
    'nicknameP1': "",  # Apodo del jugador 1
    'nicknameP2': "",  # Apodo del jugador 2
    'Player2': 0,  # ID del jugador 2
    'Tie': 0,  # Empates
    'Player1Wins': 0,  # Victorias del jugador 1
    'Player2Wins': 0,  # Victorias del jugador 2
    'Player1Losses': 0,  # Derrotas del jugador 1
    'Player2Losses': 0,  # Derrotas del jugador 2
    'Player1ConsecutiveWins': 0,  # Victorias consecutivas del jugador 1
    'Player2ConsecutiveWins': 0,  # Victorias consecutivas del jugador 2
    'Player1ShieldActive': False,  # Estado del escudo del jugador 1
    'Player2ShieldActive': False  # Estado del escudo del jugador 2
}
