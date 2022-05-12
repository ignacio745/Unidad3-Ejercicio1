from Menu import Menu
from ManejadorFacultades import ManejadorFacultades

if __name__ == "__main__":
    unManejadorFacultades = ManejadorFacultades()
    unManejadorFacultades.cargarFacultades("Facultades malo.csv")
    unMenu = Menu()
    unMenu.ejecutarMenu(unManejadorFacultades)