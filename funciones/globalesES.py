from os import system
import sys
from enum import Enum

def borar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system('cls')

def pausar_pantalla(): 
    if sys.platform == "linux" or sys.platform == "darwin":
        x=input("presione una tecla para continuar")
    else:
        system("pause")
centromedico = {
    "dataespecialista" : {}
}