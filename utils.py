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
RESETCOLOR = "\033[0m"
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

"""
El proposito de las siguientes funciones
es imprimr mensajes ya sean de error,que todo se verifico con exito
de informacion y de advertencia
Recibe de parametro el mensaje(str) que es el mensaje de error,exito,info o
advertencia a mostrar.
"""

def imprimirError(mensaje):
    print(ROJO + " X " + mensaje + RESETCOLOR)


def imprimirExito(mensaje):
    print(VERDE + " ✔ " + mensaje + RESETCOLOR)

def imprimirInfo(mensaje):
    print(AZUL + " -> " + mensaje + RESETCOLOR)

def imprimirWarning(mensaje):
    print(AMARILLO + " ⚠ " + mensaje + RESETCOLOR)

def imprimirAnimado(texto):
    """
    El proposito de esta funcion es imprimir un texto en la terminal linea
    por linea con una pausa de 0.3 ms simulando asi una animacion

    Recibe de parametro un texto(str) que lo divide en lineas
    """

    for linea in texto.split('\n'):
        print(linea)
        time.sleep(0.3)



