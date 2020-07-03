import pygame

def definirMovimientosFichas(idJugador):
    if idJugador == 0:
        return [pygame.K_w, pygame.K_s, pygame.K_e]
    elif idJugador == 1:
        return [pygame.K_UP, pygame.K_DOWN, pygame.K_2]