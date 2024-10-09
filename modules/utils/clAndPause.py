import sys  # Importa el módulo sys para acceder a funciones y variables relacionadas con el intérprete de Python
import os  # Importa el módulo os para interactuar con el sistema operativo

def limpiar():  # Define la función para limpiar la consola
    # Verifica el sistema operativo en uso
    if sys.platform == "linux" or sys.platform == "darwin":  # Para sistemas Linux o macOS
        os.system("clear")  # Ejecuta el comando 'clear' para limpiar la consola
    else:  # Para sistemas Windows
        os.system("cls")  # Ejecuta el comando 'cls' para limpiar la consola

def pausar():  # Define la función para pausar la ejecución y esperar la interacción del usuario
    if sys.platform == "linux" or sys.platform == "darwin":  # Para sistemas Linux o macOS
        x = input("Presione una tecla para continuar...")  # Solicita al usuario que presione una tecla
    else:  # Para sistemas Windows
        os.system("pause")  # Ejecuta el comando 'pause' que espera a que el usuario presione una tecla
