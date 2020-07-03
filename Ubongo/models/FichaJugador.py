from models.componente import Componente
import pygame

class FichaJugador(Componente):
    def __init__(self, x, y, width, height, window, color):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.color = color

    def dibujarFicha(self):
        pygame.draw(self.window,
                    self.color,
                    (self.x, self.y),
                    20)