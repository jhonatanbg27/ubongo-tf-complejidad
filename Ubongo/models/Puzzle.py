import pygame
from models.componente import Componente
from models.LecturaPuzzles import recuperarPiezasDePuzzle
from models.LecturaPuzzles import recuperarPuzzlePorId
#from models.LecturaPuzzles import recuperarImagenPorIdYDificultad
from models.utils.Cuadrado import Cuadrado


class Puzzle(Componente):
    def __init__(self, window, x, y, idPuzzle, dificultad):

        self.window = window
        self.idPuzzle = idPuzzle
        self.dificultad = dificultad
        self.cantEspaciosVacios = 0
        self.piezas = recuperarPiezasDePuzzle(self.idPuzzle, self.dificultad)
        self.forma = recuperarPuzzlePorId(self.idPuzzle, self.dificultad)
        Componente.__init__(self, x, y, len(self.forma[0]) * 35, len(self.forma) * 35)
        self.dibujoPuzzle = []
        self.generarPuzzle()



    def generarPuzzle(self):
        #self.window.blit(self.image, (self.x, self.y))
        i = 0
        j = 0
        for fila in self.forma:
            for columna in fila:
                if columna == -2:
                    self.dibujoPuzzle.append(None)
                elif columna == -1:
                    self.cantEspaciosVacios += 1
                    self.dibujoPuzzle.append(Cuadrado(
                        self.window, columna,
                        self.x + j*35, self.y + i*35
                       ))
                j += 1
            j = 0
            i += 1


    def dibujarPuzzle(self):
        for cuadrado in self.dibujoPuzzle:
            if cuadrado != None:
                cuadrado.dibujarCuadrado('Puzzle')


    def colisionConPieza(self, pieza):

        if pieza.x + pieza.width > self.x and pieza.x < self.x + self.width:
            if pieza.y + pieza.height > self.y and pieza.y < self.y + self.height:
                return True
        return False


