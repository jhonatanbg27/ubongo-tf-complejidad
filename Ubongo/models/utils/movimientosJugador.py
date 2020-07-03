import pygame

def definirMovimientosJugador(idJugador):
    if idJugador == 0:
        return [pygame.K_w, pygame.K_s,
                       pygame.K_a, pygame.K_d,
                       pygame.K_q, pygame.K_e, pygame.K_r]
    elif idJugador == 1:
        return [pygame.K_UP, pygame.K_DOWN,
                       pygame.K_LEFT, pygame.K_RIGHT,
                       pygame.K_1, pygame.K_2, pygame.K_3]


