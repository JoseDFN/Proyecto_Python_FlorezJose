import os  # Importa el módulo os para interactuar con el sistema operativo
import json  # Importa el módulo json para trabajar con archivos JSON

MY_DATABASE = None  # Define la ruta del archivo de la base de datos

def NewFile(*param):  # Define la función para crear un nuevo archivo JSON
    with open(MY_DATABASE, "w") as wf:  # Abre el archivo en modo escritura
        json.dump(param[0], wf, indent=4)  # Guarda el contenido del primer parámetro como JSON en el archivo

def ReadFile():  # Define la función para leer un archivo JSON
    with open(MY_DATABASE, "r") as rf:  # Abre el archivo en modo lectura
        return json.load(rf)  # Carga y devuelve el contenido del archivo como un objeto de Python

def checkFile(*param):  # Define la función para verificar la existencia del archivo de base de datos
    data = list(param)  # Convierte los parámetros en una lista
    if os.path.isfile(MY_DATABASE):  # Verifica si el archivo existe
        if len(param):  # Si hay parámetros proporcionados
            data[0].update(ReadFile())  # Actualiza el primer parámetro con los datos leídos del archivo
    else:  # Si el archivo no existe
        if len(param):  # Si hay parámetros proporcionados
            NewFile(data[0])  # Crea un nuevo archivo JSON con el primer parámetro

def save_game(game):  # Define la función para guardar el estado del juego
    NewFile(game)  # Llama a la función NewFile para guardar el juego en el archivo
