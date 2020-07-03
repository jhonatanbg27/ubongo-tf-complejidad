import pygame

def recuperarPuzzlePorId(idPuzzle, dificultad):
    if dificultad == "Normal":
        fh = open('assets\\Puzzles\\PuzzlesDificultadNormal.txt', 'r')
    else:
        fh = open('assets\\Puzzles\\PuzzlesDificultadDificil.txt.txt', 'r')
    c = 0
    matrizPuzzle = []
    partePuzzle = []
    for line in fh.readlines():
        if line.strip() == '#Puzzle ' + str(idPuzzle):
            c = 1
            continue
        if c == 1:
            if line.strip() == '#Fin':
                c = 0
                break
            else:
                for n in line.strip().split(','):
                    partePuzzle.append(int(n))
                matrizPuzzle.append(partePuzzle)
                partePuzzle = []
    return matrizPuzzle

def recuperarImagenPorIdYDificultad(idPuzzle, dificultad):
    if dificultad == "Normal":
        return pygame.image.load('../assets/Puzzles/Normal/NPuzzle ' + str(idPuzzle) + '.png')
    else:
        return pygame.image.load('../assets/Puzzles/Dificil/DPuzzle ' + str(idPuzzle) + '.png')


def recuperarPiezasDePuzzle(idPuzzle, dificultad):
    if dificultad == "Normal":
        fh = open('assets\\Puzzles\\PiezasPuzzleNormal.txt', 'r')
    else:
        fh = open('assets\\Puzzles\\PiezasPuzzleDificil.txt', 'r')
    c = 0
    listaPiezas = []
    matrizPiezas = []
    for line in fh.readlines():
        if line.strip() == '#Piezas ' + str(idPuzzle):
            c = 1
            continue
        if c == 1:
            if line.strip() == "#Fin":
                c = 0
                break
            for n in line.strip().split(','):
                listaPiezas.append(int(n))
            matrizPiezas.append(listaPiezas)
            listaPiezas = []
    return matrizPiezas