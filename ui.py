<<<<<<< HEAD
#ui
#Realizado por Johel Fernandez y Isaac Esquivel 10:25AM 4/13/2026

from os import system
import time

def limpiarPantalla():
    """
    El proposito de esta funcion es limpiar la consola para tener
    un menu ordenado y estetico.
    Parametros ninguno y no retorna nada.
    """
    system("cls")

def pausarPantalla():
    """
    El proposito de esta funcion es pausar la
    ejecucion hasta que el usuario precione una tecla
    permitiendo leer los resultados antes de volver al menu
    Parametros ninguno y no retorna nada.
    """
    system("pause")



=======
#ui.py
#Realizado por Johel Fernandez y Isaac Esquivel 4/13/2026 9:14PM
"""
Modulo de la interfaz para el usuario

Contiene todas las funciones que va a ver el usuario como menus y presentacion
de datos para que el usuario interactue con la applicacion a traves de la 
terminal
"""
import utils

def menuPrincipal():
    """
    El propolsito de esta funcion es mostrar las opciones principales
    del sistema DevSpaces.
    No recibe parametros ni retorna nada
    """

    utils.limpiarPantalla()
    print("---------MENU DEVSPACES---------")
    print("1. Consultar todos los Usuarios")
    print("2. Consultar todos los Spaces")
    print("3. Seguir un Space")
    print("4. Consultar mis Spaces seguidos")
    print("5. Gestionar seguidores de mis Spaces")
    print("6. Salir")
>>>>>>> de650a22c1e5c02441f1711d9ffc2f90941aa9e7



