# import sys
# sys.path.append("D://7MO CICLO//COMPLEJIDAD_ALGORÍTMICA//Trabajo Final//ubongoTime//Ubongo//assets//Piezas//")


def recuperarPiezaPorId(idPieza):
    fh = open('assets\\Piezas\\Piezas.txt', 'r')
    c = 0
    x = []
    y = []
    for line in fh.readlines():
        if line.strip() == 'P' + str(idPieza):
            c = 1
            continue
        if c == 1:
            if line.strip() == 'Fin':
                c = 0
                break
            else:
                for n in line.strip().split(','):
                    x.append(int(n))
                y.append(x)
                x = []
    return y





def procesarPiezas():
    piezas = ['P1', 'P0', 'P7', 'P8']
    fh = open("../assets/Piezas/Piezas.txt")
    x = []
    y = []
    z = []
    visitados = 0
    c = 0
    contador = 0
    for line in fh.readlines():
        if contador == 0:
            if visitados < len(piezas):
                for pieza in piezas:
                    if line.strip() == pieza:
                        visitados += 1
                        c = 1
                        break
            else:
                break
        if c == 1 and contador == 0:
            contador += 1
            continue
        elif c != 1:
            continue
        if contador > 0:
            if line.strip() == "Fin":
                contador = 0
                c = 0
                z.append(y)
                y = []
                continue
            for n in line.strip().split(','):
                 x.append(int(n))
            y.append(x)
            x = []
            contador += 1

    return z

