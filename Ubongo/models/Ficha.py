from models.componente import Componente
import pygame

class Ficha(Componente):

    def __init__(self, x, y, diameter, window, color, idJugador, fila):
        Componente.__init__(self, x, y, diameter, diameter)
        self.window = window
        self.color = color
        self.idJugador = idJugador
        self.colorTexto = (0, 0, 0)
        self.filaInicial = fila
        self.filaVariable = fila
    def dibujarFicha(self):

        pygame.draw.circle(self.window, self.color,
                           (self.x + self.width // 2,
                            self.y + self.height // 2),
                           self.width // 2)

        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(str(self.idJugador), 1, self.colorTexto)
        self.window.blit(text, (
        self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))























