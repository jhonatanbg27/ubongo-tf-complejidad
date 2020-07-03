import pygame
from models.componente import Componente
menu = pygame.image.load('assets/Fondos/Ubongo-Hero.jpg')
tablero = pygame.image.load('assets/Tablero/tablero.png')
tablero = pygame.transform.scale(tablero, (890, 290))
import random as rnd
from models.factory.GemaFactory import GemaFactory

class Tablero(Componente):
    def __init__(self, window, x, y, width = 100, height = 100):
        Componente.__init__(self, window.get_rect().width / 2 - width / 2, window.get_rect().height / 2 - height / 2, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.matrizGemas = [[None for _ in range(12)] for _ in range(6)]
        self.generarGemas()

    def dibujarTablero(self):
        self.window.blit(tablero, (self.x, self.y))
        for fila in range(len(self.matrizGemas)):
            for columna in range(len(self.matrizGemas[fila])):
                    self.matrizGemas[fila][columna].dibujarGema()

    def generarGemas(self):
        x = self.x + 174
        y = self.y + 32
        for fila in range(6):
            for columna in range(12):
                idGema = rnd.randint(0, 5)
                self.matrizGemas[fila][columna] = GemaFactory.crearGema(x,
                     y, idGema, self.window)
                if columna == 7:
                    x += 18 + 24
                else:
                    x += 18 + 32
            x = self.x + 174
            y += 11 + 30


