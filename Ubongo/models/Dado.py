from models.componente import Componente
import pygame
import random

class Dado(Componente):
    def __init__(self, x, y, width, height, window):
        Componente.__init__(self, x, y, width, height)
        self.window = window
        self.posicion = 0
        self.image = pygame.image.load('../assets/Dado/Dado ' + str(self.posicion + 1) + '.png')
        self.image = pygame.transform.scale(self.image, (100, 100))

    def tirarDado(self):
        numero = random.randint(0, 5)
        self.posicion = numero
        self.image = pygame.image.load('../assets/Dado/Dado ' + str(self.posicion + 1) + '.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        print(self.posicion)

    def dibujar(self):
        self.window.blit(self.image, (self.x, self.y))

