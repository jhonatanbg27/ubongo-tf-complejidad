import pygame
from models.menu import Menu
from models.Juego import Juego

mesa = pygame.image.load('assets/Fondos/fondo mesa.png')
pygame.init()


window = pygame.display.set_mode((1920, 1080))
#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Prueba")
run = True
menu = Menu(window)
ubongo = Juego(window)


#kejestooo?
paraTirarDado = 0

while run:
    window.fill((0, 0, 0))
    window.blit(mesa, (0, 0))

    if ubongo.enMenu:
        ubongo.dibujarMenu()
    elif ubongo.enJuego:
        ubongo.dibujarJuego()

    pygame.display.update()

    #eventos
    for event in pygame.event.get():

        posicionMouse = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        #animaciones
        if event.type == pygame.MOUSEMOTION:
            if ubongo.enMenu:
                ubongo.hoverBotonesMenu(posicionMouse)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ubongo.enMenu:
                #aqui solo sirve para una ronda
                ubongo.transicionarMenu(posicionMouse)

        #teclas
        if event.type == pygame.KEYDOWN:
            if ubongo.enJuego:
                window.fill([0, 0, 0])
                ubongo.ejecutarAccion(event.key)
















