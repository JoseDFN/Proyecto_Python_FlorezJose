import os
import json

MY_DATABASE = None  # Define the path to your database file

def NewFile(*param):
    with open(MY_DATABASE, "w") as wf:
        json.dump(param[0], wf, indent=4)

def ReadFile():
    with open(MY_DATABASE, "r") as rf:
        return json.load(rf)

def checkFile(*param):
    data = list(param)
    if os.path.isfile(MY_DATABASE):
        if len(param):
            data[0].update(ReadFile())
    else:
        if len(param):
            NewFile(data[0])
def save_game(game):
    NewFile(game)
def load_game():
    game = {
        'Jugadores':{},
        'Maquina':{
            'pJugados': 0,
            'pGanados': 0,
            'pPerdidos':0
        }
    }
    checkFile(game)  # Chequea si el archivo existe, y si no, lo crea con los datos iniciales
    return game
