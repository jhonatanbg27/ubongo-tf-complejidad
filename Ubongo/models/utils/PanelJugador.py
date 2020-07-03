from models.componente import Componente

class PanelJugador(Componente):
    def __init__(self, x, y, window, width, height, idJugador):
        self.idJugador = idJugador
        self.window = window
        Componente.__init__(self, x, y, width, height)
        
