#utils.py
#Realizado por Johel Fernandez y Isaac Esquivel 10:25AM 4/13/2026

"""
Modulo para utilidades

Contiene las funciones para animacionesen la terminal ,colores ANSI
y ayudas reutilizables
Para que se vea mas limpio y estetico el programa
"""

from os import system
import time

"""
Colores para la terminal en ANSI
"""
RESTABLECER = "\033[0m"
AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
BLANCO = "\033[97m"

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






