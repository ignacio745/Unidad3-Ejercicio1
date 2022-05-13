from Menu import Menu
from ManejadorFacultades import ManejadorFacultades

if __name__ == "__main__":
    unManejadorFacultades = ManejadorFacultades()
    unManejadorFacultades.cargarFacultades("Facultades.csv")
    unMenu = Menu()
    unMenu.ejecutarMenu(unManejadorFacultades)
