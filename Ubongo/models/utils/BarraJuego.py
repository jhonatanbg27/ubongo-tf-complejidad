import pygame
from models.componente import Componente
from models.Temporizador import Temporizador
menu = pygame.image.load('assets/Fondos/Ubongo-Hero.jpg')
reloj = pygame.image.load('assets/Acciones/reloj.png')
reloj = pygame.transform.scale(reloj, (70, 70))
from models.ScoreJugador import ScoreJugador
widthMenu = menu.get_rect().width
heightMenu = menu.get_rect().height

class BarraJuego(Componente):
    def __init__(self, window, jugadores, width = widthMenu, height = heightMenu):
        Componente.__init__(self, window.get_rect().width / 2 - width / 2, window.get_rect().height / 2 - height / 2, width, height)
        self.window = window
        self.temporizador = Temporizador(1450, 50, 70, 70, self.window)
        self.barra = None
        self.jugadores = jugadores
        self.scores = []
        self.setearScore()


    def dibujarBarraJuego(self):
        self.barra = pygame.draw.rect(self.window, (0, 0, 0), (0, 0, self.window.get_rect().width, 180))
        self.temporizador.dibujarTemporizador()
        for i in range(len(self.jugadores)):
            self.scores[i].dibujarScoreJugador()

    def setearScore(self):
        for i in range(len(self.jugadores)):
            self.scores.append(ScoreJugador(self.x + 50 + i*300, self.y - 130, self.jugadores[i], self.window))