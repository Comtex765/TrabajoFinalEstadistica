from tabulate import tabulate
from funcionesEstadisticasNOagrupados import quicksort

# ======================================Funciones=======================================#


def crearMatriz(filas, columnas):
    # Crea una matriz de las dimensiones de los parámetros
    matriz = []
    for i in range(filas):
        matriz.append([0]*columnas)

    return matriz


def mostrarResultadosNA(matriz):
    return(tabulate(matriz, headers=[
        'Valor', 'fi', 'FI', 'hI', 'HI'], tablefmt="grid", numalign="center", stralign="center"))


def unificarNA(datos):
    quicksort(datos, 0, len(datos) - 1)

    datosSinRepetir = []

    datosSinRepetir.append(datos[0])
    contador = 1

    for i in range(1, len(datos)):
        if(datos[i] != datos[i - 1]):
            contador += 1
            datosSinRepetir.append(datos[i])

    contador += 1

    matriz = crearMatriz(contador, 5)

    fAcumulada = 0

    for i in range(contador):
        if(i == contador - 1):
            matriz[i][0] = "TOTAL"
            matriz[i][1] = len(datos)
            matriz[i][2] = ''
            matriz[i][4] = ''
        else:
            matriz[i][0] = datosSinRepetir[i]

            fI = 0
            for j in range(len(datos)):
                if(datos[j] == matriz[i][0]):
                    fI += 1
            matriz[i][1] = fI

            fAcumulada += matriz[i][1]

            matriz[i][2] = fAcumulada
            matriz[i][3] = round(matriz[i][1] / len(datos), 5)
            matriz[i][4] = round(matriz[i][2] / len(datos), 5)

            matriz[contador - 1][3] += matriz[i][3]
    return matriz
