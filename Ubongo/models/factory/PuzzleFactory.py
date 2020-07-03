from models.Puzzle import Puzzle
import pygame


window1 = pygame.display.set_mode((1920, 1080))

class PuzzleFactory:

    @staticmethod
    def crearPuzzle(x, y, idPuzzle, window, dificultad):
        puzzleCreado = None
        if dificultad == "Normal":
            puzzleCreado = Puzzle(window, x, y, idPuzzle, dificultad)
        return puzzleCreado



