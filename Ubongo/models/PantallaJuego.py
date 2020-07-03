from models.componente import Componente
from models.Tablero import Tablero
from models.utils.BarraJuego import BarraJuego
from models.Dado import Dado

class PantallaJuego(Componente):
    def __init__(self, window, jugadores, width = 100, height = 100):
        Componente.__init__(self, window.get_rect().width / 2 - width / 2, window.get_rect().height / 2 - height / 2, width, height)
        self.window = window
        self.tablero = Tablero(window, 450, 250, 250, 250)
        self.jugadores = jugadores
        self.barraJuego = BarraJuego(window, jugadores)
        self.dado = Dado(1350, 300, 200, 200, window)
        self.width = width
        self.height = height


    def dibujarTablero(self):
        self.barraJuego.dibujarBarraJuego()
        self.tablero.dibujarTablero()
        self.dado.dibujar()

