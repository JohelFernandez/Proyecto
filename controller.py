#controller.py
#Realizado por Johel Fernandez y Isaac Esquivel 4/13/2026 10:07PM

import devspace
import utils
import ui


def menuPrinci():
    """
    Muestra el menu principal y gestiona la opcion que inserto el usuario
    y tambien se mantiene mostrando el menu por un ciclo mientras el usuario usa
    la aplicaciones

    Va a seguir el ciclo hasta que el usuario seleccione 6.
    igual despues de cada operacion regresa automaticamente a este menu
    """
    while True:
        ui.mostrarMenuPrincipal()

