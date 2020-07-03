import pygame
from models.componente import Componente

class Boton(Componente):

    def __init__(self, colorBoton, colorTexto, x, y, width, height, text=''):
        Componente.__init__(self, x, y, width, height)
        self.colorBoton = colorBoton
        self.colorTexto = colorTexto
        self.text = text


    def draw(self, window):

        pygame.draw.rect(window, self.colorBoton, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, self.colorTexto)
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def hover(self, colorBoton, colorTexto):
        self.colorBoton = colorBoton
        self.colorTexto = colorTexto

    def setColores(self, colorBoton, colorTexto):
        self.colorTexto = colorTexto
        self.colorBoton = colorBoton