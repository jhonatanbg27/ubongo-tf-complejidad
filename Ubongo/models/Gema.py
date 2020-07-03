from models.componente import Componente
import pygame

class Gema(Componente):

    def __init__(self, x, y, idGema, window, width=18, height=30):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.idGema = idGema
        self.gemaImg = pygame.image.load('assets\\Gemas\\Gema ' + str(idGema) + '.png')
        self.gemaImgEscalada = pygame.transform.scale(self.gemaImg, (self.width, self.height))
        self.recogida = False

    def dibujarGema(self):
        self.window.blit(self.gemaImgEscalada, (self.x, self.y))


