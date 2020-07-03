from models.Pieza import Pieza
from models.LecturaPiezas import recuperarPiezaPorId
import pygame


window1 = pygame.display.set_mode((1920, 1080))

class PiezaFactory:

    @staticmethod
    def crearPieza(x, y, idPieza, window):
        piezaCreada = Pieza(x, y, idPieza, window)
        return piezaCreada


