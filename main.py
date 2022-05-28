from Menu import Menu
from ManejadorFacultades import ManejadorFacultades
import os

if __name__ == "__main__":
    os.system("clear")
    unManejadorFacultades = ManejadorFacultades()
    unManejadorFacultades.cargarFacultades("Facultades.csv")
    unMenu = Menu()
    unMenu.ejecutarMenu(unManejadorFacultades)