from models.componente import Componente
import pygame
from models.Gema import Gema
class ScoreJugador(Componente):

    def __init__(self, x, y,  jugador, window):
        Componente.__init__(self, x, y, 400, 400)
        self.idJugador = jugador.id
        self.jugador = jugador
        self.window = window

    def dibujarScoreJugador(self):

        font = pygame.font.SysFont('comicsans', 40)
        jugadorText = font.render("Jugador "+ str(self.idJugador + 1), 1, (255,255,255))
        self.window.blit(jugadorText, (self.x, self.y))

        for i in range(6):
            if i < 3:
                gema = Gema(self.x - 50 + 60*i, self.y + 30, i, self.window)
                gema.dibujarGema()
                font = pygame.font.SysFont('comicsans', 40)
                numeroGemas = font.render(str(self.jugador.contadorGemas[i]), 1, (255, 255, 255))
                self.window.blit(numeroGemas, (gema.x + gema.width*2, gema.y))
            else:
                gema = Gema(self.x - 50 + 60 * (i - 3), self.y + 70, i, self.window)
                gema.dibujarGema()
                font = pygame.font.SysFont('comicsans', 40)
                numeroGemas = font.render(str(self.jugador.contadorGemas[i]), 1, (255, 255, 255))
                self.window.blit(numeroGemas, (gema.x + gema.width * 2, gema.y))