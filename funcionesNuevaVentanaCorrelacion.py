from tabulate import tabulate

from funcionesEstadisticasNOagrupados import mediaNA

# ======================================Funciones=======================================#


def crearMatriz(filas, columnas):
    # Crea una matriz de las dimensiones de los parámetros
    matriz = []
    for i in range(filas):
        matriz.append([0]*columnas)

    return matriz


def mostrarResultadosCorrelacion(matriz):
    
    return(tabulate(
        matriz,
        headers=['N', 'X', 'Y', 'X - media(X)', 'Y - media(Y)', '(X - media(X))^2',
                 '(Y - media(Y))^2', '(X - media(X))(Y - media(Y))'],
        tablefmt="grid",
        numalign="center",
        stralign="center")
    )


def calcularCorrelacion(datosX, datosY):
    mediaX = mediaNA(datosX)
    mediaY = mediaNA(datosY)

    matriz = crearMatriz(len(datosX) + 1, 8)

    matriz[len(datosX)][0] = ""

    matriz[len(datosX)][1] = 0
    matriz[len(datosY)][2] = 0

    matriz[len(datosY)][3] = ""
    matriz[len(datosY)][4] = ""

    matriz[len(datosX)][5] = 0
    matriz[len(datosY)][6] = 0

    matriz[len(datosY)][7] = 0

    for i in range(len(datosX)):
        matriz[i][0] = i + 1

        matriz[i][1] = datosX[i]
        matriz[i][2] = datosY[i]

        matriz[i][3] = round(matriz[i][1] - mediaX, 5)
        matriz[i][4] = round(matriz[i][2] - mediaY, 5)

        matriz[i][5] = round(matriz[i][3] ** 2, 5)
        matriz[i][6] = round(matriz[i][4] ** 2, 5)

        matriz[i][7] = matriz[i][3] * matriz[i][4]

        matriz[len(datosX)][1] += matriz[i][1]
        matriz[len(datosY)][2] += matriz[i][2]

        matriz[len(datosX)][5] += matriz[i][5]
        matriz[len(datosY)][6] += matriz[i][6]
        matriz[len(datosY)][7] += matriz[i][7]

    return matriz


def correlacion(sumX, sumY, sumP, n):
    desvX = (sumX / (n - 1)) ** 0.5
    desvY = (sumY / (n - 1)) ** 0.5

    return round(((sumP) / ((n - 1) * (desvX) * (desvY))), 5)
