import pygame
from models.Jugador import Jugador
import copy

contador = 0

class JugadorComputadora(Jugador):

    def __init__(self, id, listaMovimientos, movimientoFichas):
        Jugador.__init__(self, id, listaMovimientos, movimientoFichas)

    def reflejarHorizontalmente(self, matrizOriginal):
        matrizResultante = []

        cantidadFilas = len(matrizOriginal)
        cantidadColumnas = len(matrizOriginal[0])

        matrizResultante = matrizOriginal[:]

        if cantidadColumnas == 1:
            return matrizOriginal


        ultimoIndice = cantidadColumnas - 1

        for f in range(cantidadFilas):
            for c in range(cantidadColumnas//2):
                matrizResultante[f][ultimoIndice - c], matrizResultante[f][0 + c] =  matrizResultante[f][0 + c], matrizResultante[f][ultimoIndice - c]

        return matrizResultante

    def reflejarVerticalmente(self, matrizOriginal):
        matrizResultante = []

        cantidadFilas = len(matrizOriginal)
        cantidadColumnas = len(matrizOriginal[0])

        matrizResultante = matrizOriginal[:]

        if cantidadFilas == 1:
            return matrizOriginal

        ultimoIndice = cantidadFilas - 1

        for c in range(cantidadColumnas):
            for f in range(cantidadFilas//2):
                matrizResultante[ultimoIndice-f][c], matrizResultante[0+f][c] = matrizResultante[0+f][c], matrizResultante[ultimoIndice-f][c]

        return matrizResultante

    def rotarMatriz(self, matrizOriginal):
        #invertir columnas y filas

        matrizResultante = []

        cantidadFilas = len(matrizOriginal)
        cantidadColumnas = len(matrizOriginal[0])


        for f in range(cantidadColumnas):
            matrizResultante.append([])

        #hasta aqui ya tengo la matriz con C filas

        #asigno valores
        for c in range(cantidadColumnas):
            #Mientras que f sea > -1, se le restará 1, comenzando desde cantidadFilas-1
            for f in range(cantidadFilas-1, -1, -1):
                matrizResultante[c].append(matrizOriginal[f][c]) 

        return matrizResultante

    def verificarPuzzle(self,puzzle):
        for f in range(len(puzzle)):
            for c in range(len(puzzle[0])):
                if puzzle[f][c] == -1:
                    return False
        else:
            return True   

    def resolverPuzzle(self):
        
        piezas = []
        piezasCombinadas = []

        for i in range(len(self.piezas)):
            piezas.append(copy.deepcopy(self.piezas[i].forma))
    
        for i in range(len(piezas)):
        
            #pieza original
            piezasCombinadas.append( piezas[i] )
            #todos sus giros
            for j in range (3):
                piezas[i] = self.rotarMatriz(piezas[i])
                piezasCombinadas.append( piezas[i] )
            
            #voltear horizontal
            piezas[i] = self.reflejarHorizontalmente(piezas[i])
            piezasCombinadas.append(piezas[i])
            #todos sus giros
            for j in range (3):
                piezas[i] = self.rotarMatriz(piezas[i])
                piezasCombinadas.append( piezas[i] )
    
            #voltear vertical 
            piezas[i] = self.reflejarVerticalmente(piezas[i])
            piezasCombinadas.append( piezas[i] )
            #todos sus giros
            for j in range (3):
                piezas[i] = self.rotarMatriz(piezas[i])
                piezasCombinadas.append( piezas[i] )
    
            #voltear horizontal
            piezas[i] = self.reflejarHorizontalmente(piezas[i])
            piezasCombinadas.append(piezas[i])
            #todos sus giros
            for j in range (3):
                piezas[i] = self.rotarMatriz(piezas[i])
                piezasCombinadas.append( piezas[i] )
    
            ##########
            # Hasta aqui han sido generadas todas las combinaciones de self.piezas
            #aqui comienza el backtracking
    
        visitados = [0]*len(piezasCombinadas)
    
        self.backtracking(piezasCombinadas, self.puzzleSeleccionado.forma, visitados)
    
    def backtracking(self, piezasCombinadas,puzzle, visitados):
        
        global contador 
        
        for j in range(len(piezasCombinadas)):
            #Si al menos una pieza no esta visitada, continuar con el loop
            if visitados[j] == 0:
                break
        else:
            #si no hay ninguna pieza sin visitar o el puzzle está completo,
            #entonces se ha completado el puzzle
            if self.verificarPuzzle(puzzle) == True:
                print("it's over")
                return True
            else:
                contador+=1
                return False
        
    
        #probar
        #iterar espacio por espacio hasta buscar uno libre para colocar una pieza NO VISITADA
        #Buscaré que pieza entra en este punto inicial
        for f in range(len(puzzle)):
            for c in range(len(puzzle[0])):
            
                #Iterar todas las piezas y ver cual puedo poner 
                for j in range(len(piezasCombinadas)):
                
                    if visitados[j] != 0:
                        continue
                    
                    #puedo poner la pieza J en el punto F,C?
                    #Si el espacio inicial esta vacio, o esta ocupado pero coincide con uno vacio de la pieza,
                    #Entonces probar ahi
                    if puzzle[f][c] == -1 or ( puzzle[f][c] > -1 and piezasCombinadas[j][0][0] < 0 ) :
                    
                        visitados[j] += 1
                        
                        #copia del puzzle original
                        _puzzle = copy.deepcopy(puzzle)
    
                        ##Al posicionar la pieza, supero el tamaño del puzzle?
                        if f + len(piezasCombinadas[j]) > len(puzzle) or c + len(piezasCombinadas[j][0]) > len(puzzle[0]):
                            visitados[j] = 0
                            continue
                        
                        #Puedo meter mi pieza sin que colisione con algun espacio bloqueado 
                        #o con otra pieza?
                        #iterar todas las posiciones de la pieza
                        for f2 in range(len(piezasCombinadas[j])):
                            for c2 in range(len(piezasCombinadas[j][0])):
                                
                                if piezasCombinadas[j][f2][c2] > -1:
                                    #esta vacio el espacio donde 
                                    #se quiere colocar esa parte de la pieza?
                                    if puzzle[f+f2][c+c2] < 0:
                                        puzzle[f+f2][c+c2] = piezasCombinadas[j][f2][c2]
                                    #si esta ocupado, romper el ciclo
                                    elif puzzle[f+f2][c+c2] > -1:
                                        break
                                    
                            else:
                                continue
                            
                            #no se ha completado todo el for, por lo tanto, hay un espacio ocupado
                            #entonces no puedo meter mi pieza
                            #deshacer cambios
                            puzzle = copy.deepcopy(_puzzle)
                            break
                        else:
                            #se posiciono la pieza sin problemas
                            #romper ciclo de busqueda de un espacio para colocar pieza
                            if j < 16:
                                for p in range(0,16):
                                    visitados[p] = 1
                            elif j < 32:
                                for p in range(16,32):
                                    visitados[p] = 1
                            elif j < 48:
                                for p in range(32,48):
                                    visitados[p] = 1
                            elif j < 64:
                                for p in range(48,64):
                                    visitados[p] = 1    
                            #buscar mas con esta opcion
                            
                            if self.backtracking(piezasCombinadas, copy.deepcopy(puzzle), visitados) == True:
                                return True
    
                        #no se poisiciono la pieza
                        #deshacer el visitado
                        #volver el puzzle a su estado original
                        puzzle = copy.deepcopy(_puzzle)
                        if j < 16:
                            for p in range(0,16):
                                visitados[p] = 0
                        elif j < 32:
                            for p in range(16,32):
                                visitados[p] = 0
                        elif j < 48:
                            for p in range(32,48):
                                visitados[p] = 0
                        elif j < 64:
                            for p in range(48,64):
                                visitados[p] = 0
                                
        return False

    
    
    
    
    
    
    