from models.componente import Componente
import pygame

class Temporizador(Componente):

    def __init__(self, x, y, width, height, window):
        Componente.__init__(self, x, y, width, height)
        self.segundos = 60
        self.window = window
        self.imagen = reloj = pygame.image.load('assets/Acciones/reloj.png')
        self.imagenReescalada = pygame.transform.scale(reloj, (70, 70))

    def correrTiempo(self):
        self.segundos -= 1

    def reiniciarTiempo(self):
        self.segundos = 60

    def dibujarTemporizador(self):
        self.window.blit(self.imagenReescalada, (self.x, self.y))

        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(str(self.segundos), 1, (255, 255, 255))
        self.window.blit(text, (
            self.x + self.width + 20, self.y + 35))