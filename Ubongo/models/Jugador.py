import pygame
import copy

class Jugador():
    def __init__(self, id, listaMovimientos, movimientoFichas):
        self.id = id
        self.piezas = []
        self.piezaSeleccionada = None
        self.puzzles = []
        self.puzzleSeleccionado = None
        self._puzzleSeleccionadoForma = None
        self.ficha = None
        self.gemas = None
        self.listaMovimientos = listaMovimientos
        self.movimientoFichas = movimientoFichas
        self.contadorGemas = [0 for _ in range(6)]
        self.movimientoFicha = False
        self.contadorMovimientos = 0
        self.gemasRecolectadas = False



    def moverPieza(self, movimiento):

        if movimiento == self.listaMovimientos[0]:
            self.piezaSeleccionada.piezaSube()

        elif movimiento == self.listaMovimientos[1]:
            self.piezaSeleccionada.piezaBaja()

        elif movimiento == self.listaMovimientos[2]:
            self.piezaSeleccionada.piezaALaIzquierda()

        elif movimiento == self.listaMovimientos[3]:
            self.piezaSeleccionada.piezaALaDerecha()

        elif movimiento == self.listaMovimientos[4]:
            self.cambiarPiezaSeleccionada()

        elif movimiento == self.listaMovimientos[5]:
            self.piezaSeleccionada.rotarPieza()

        elif movimiento == self.listaMovimientos[6]:
            self.piezaSeleccionada.flipearPieza()

        else:
            return False
        print("Puzzle #" + str(self.puzzleSeleccionado.idPuzzle))
        print(f'Coordenadas: ({str(self.puzzleSeleccionado.x)} , {str(self.puzzleSeleccionado.y)})')
        print("Pieza #" + str(self.piezaSeleccionada.idPieza))
        print(f'Coordenadas: ({str(self.piezaSeleccionada.x)} , {str(self.piezaSeleccionada.y)})')

        return True

    def cambiarPiezaSeleccionada(self):
        idPiezaSeleccionada = self.piezas.index(self.piezaSeleccionada)
        if idPiezaSeleccionada == len(self.piezas) - 1:
            self.piezaSeleccionada = self.piezas[0]
        else:
            self.piezaSeleccionada = self.piezas[idPiezaSeleccionada + 1]

    def validarSolucionPuzzle(self):

        self.puzzleSeleccionado.forma = copy.deepcopy(self._puzzleSeleccionadoForma)
        contador = 0
        
        for pieza in self.piezas:

            if self.puzzleSeleccionado.colisionConPieza(pieza):

                matrizPieza = pieza.forma
                matrizPuzzle = self.puzzleSeleccionado.forma
                xPuz = self.puzzleSeleccionado.x
                xPie = pieza.x
                yPuz = self.puzzleSeleccionado.y
                yPie = pieza.y
                columnaIniPuz = columnaIniPie = 0
                filaIniPuz = filaIniPie = 0
                diferenciaX = (xPie - xPuz)//35
                diferenciaY = (yPuz - yPie)//35

                if diferenciaX < 0:
                    columnaIniPie = abs(diferenciaX)
                else:
                    columnaIniPuz = abs(diferenciaX)
                if diferenciaY <= 0:
                    filaIniPuz = abs(diferenciaY)
                else:
                    filaIniPie = abs(diferenciaY)


                c = copy.copy(columnaIniPuz)
                f = copy.copy(filaIniPuz)
                auxfPieza = copy.copy(filaIniPie)

                while c < self.puzzleSeleccionado.width//35 and \
                    columnaIniPie < pieza.width//35:

                    f = copy.copy(filaIniPuz)
                    filaIniPie = copy.copy(auxfPieza)

                    while f < self.puzzleSeleccionado.height // 35 and \
                        filaIniPie < pieza.height // 35:

                        if matrizPieza[filaIniPie][columnaIniPie] > -1:
                            if matrizPuzzle[f][c] != -2 and not matrizPuzzle[f][c] > -1:
                                matrizPuzzle[f][c] = matrizPieza[filaIniPie][columnaIniPie]
                                contador += 1
                        filaIniPie += 1
                        f += 1

                    columnaIniPie += 1
                    c += 1

                #validar puzzle completo
                if contador == self.puzzleSeleccionado.cantEspaciosVacios:
                    self.movimientoFicha = True
                    self.puzzles.pop()
                    print("Puzzle resuleto")
                    return True
        return False
                
                #print("Pieza colisionando con el puzzle " + str(pieza.idPieza)  )
        
        
        #print(self.puzzleSeleccionado.forma)

    def moverFicha(self, movimiento, limiteFilas, tablero):

        if movimiento == self.movimientoFichas[0]:
            if self.ficha.filaVariable - 1 < 0 or self.contadorMovimientos + 1 > limiteFilas:
                return
            if self.ficha.filaVariable > self.ficha.filaInicial:
                self.contadorMovimientos -= 1
            elif self.ficha.filaVariable <= self.ficha.filaInicial:
                self.contadorMovimientos += 1
            else:
                self.ficha.y -= 35
                self.ficha.filaVariable -= 1


        elif movimiento == self.movimientoFichas[1]:
            if self.ficha.filaVariable + 1 > 5 or self.contadorMovimientos + 1 > limiteFilas:
                return
            if self.ficha.filaVariable < self.ficha.filaInicial:
                self.contadorMovimientos -= 1
            elif self.ficha.filaVariable >= self.ficha.filaInicial:
                self.contadorMovimientos += 1

            self.ficha.y += 35
            self.ficha.filaVariable += 1

        elif movimiento == self.movimientoFichas[2] and not self.gemasRecolectadas:
            self.cogerGemas(tablero)
            self.gemasRecolectadas = True

    def cogerGemas(self, tablero):
        gemas = tablero.matrizGemas[self.ficha.filaVariable][:2]
        tablero.matrizGemas[self.ficha.filaVariable] = tablero.matrizGemas[self.ficha.filaVariable][2:]
        self.contadorGemas[gemas[0].idGema] += 1
        self.contadorGemas[gemas[1].idGema] += 1







