import pygame
from models.componente import Componente
from models.LecturaPiezas import recuperarPiezaPorId
from models.utils.Cuadrado import Cuadrado

class Pieza(Componente):

    def __init__(self, x, y, idPieza, window):
        self.window = window
        self.idPieza = idPieza
        self.color = None
        #self.piezaImg = pygame.image.load('assets\\Piezas\\Pieza_' + str(idPieza) + '.png')
        #self.piezaImgEscalada = pygame.transform.scale(self.piezaImg, (self.width, self.height))
        self.forma = recuperarPiezaPorId(self.idPieza)
        Componente.__init__(self, x, y, len(self.forma[0]) * 35, len(self.forma) * 35)
        self.dibujoPieza = []
        self.definirColor()
        self.generarPieza()



    def definirColor(self):
        switcher = {
            0: (42, 115, 170),
            1: (208, 104, 27),
            2: (153, 94, 15),
            3: (16, 128, 174),
            4: (234, 156, 11),
            5: (35, 146, 39),
            6: (122, 25, 122),
            7: (181, 31, 138),
            8: (187, 19, 20),
            9: (152, 188, 28),
            10: (5, 153, 139),
            11: (228, 206, 7)
        }
        self.color = switcher.get(self.idPieza)

    def generarPieza(self):
        # self.window.blit(self.image, (self.x, self.y))
        self.dibujoPieza = []
        i = 0
        j = 0
        for fila in self.forma:
            for columna in fila:
                if columna == -1:
                    self.dibujoPieza.append(None)
                else:
                    self.dibujoPieza.append(Cuadrado(
                        self.window, columna,
                        self.x + j * 35, self.y + i * 35
                    ))
                j += 1
            j = 0
            i += 1

    def dibujarPieza(self):
        for cuadrado in self.dibujoPieza:
            if cuadrado != None:
                cuadrado.dibujarCuadrado('Pieza', self.color)

    def setForma(self, forma):
        self.forma = forma


    def piezaSube(self):
        self.y -= 35
        self.generarPieza()

    def piezaBaja(self):
        self.y += 35
        self.generarPieza()

    def piezaALaIzquierda(self):
        self.x -= 35
        self.generarPieza()

    def piezaALaDerecha(self):
        self.x += 35
        self.generarPieza()


    def rotarPieza(self):
        ##############################################
        # invertir columnas y filas

        matrizResultante = []

        cantidadFilas = len(self.forma)
        cantidadColumnas = len(self.forma[0])

        # crear cantidadFilenecientas columnas
        for _ in range(cantidadColumnas):
            matrizResultante.append([])

        # hasta aqui ya tengo la matriz con C filas

        # asigno valores
        for c in range(cantidadColumnas):
            # Mientras que f sea > -1, se le restará 1, comenzando desde cantidadFilas-1
            for f in range(cantidadFilas):
                matrizResultante[c].append(self.forma[cantidadFilas - f - 1][c])

        self.forma = matrizResultante
        self.height = len(self.forma) * 35
        self.width = len(self.forma[0]) * 35
        self.generarPieza()
        print(self.forma)


    def flipearPieza(self):

        cantidadFilas = len(self.forma)

        if cantidadFilas == 1:
            return self.forma

        cantidadColumnas = len(self.forma[0])

        matrizResultante = self.forma[:]

        for fila in range(cantidadFilas):
            for columna in range(cantidadColumnas//2):
                matrizResultante[fila][columna], matrizResultante[fila][cantidadColumnas - columna - 1] \
                    = matrizResultante[fila][cantidadColumnas - columna - 1],  matrizResultante[fila][columna]
        self.forma = matrizResultante
        self.generarPieza()
        print(self.forma)




















