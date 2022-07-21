from itertools import combinations
from tabulate import tabulate

from funcionesEstadisticasNOagrupados import mediaNA, quicksort

# ======================================Funciones=======================================#


def crearMatriz(filas, columnas):
    # Crea una matriz de las dimensiones de los parámetros
    matriz = []
    for i in range(filas):
        matriz.append([0]*columnas)

    return matriz


def mostrarResultadosMuestral(matriz):
    return(tabulate(matriz, headers=[
        'Combinations', 'Sample Mean', 'Num of Means', 'Probability'], tablefmt="grid", numalign="center", stralign="center"))


def calcularMuestraMedia(datos, t):

    combinaciones = list(combinations(datos, t))

    numComb = 0

    for i in combinaciones:
        numComb += 1

    matrizAux = crearMatriz(numComb, 2)

    medias = []

    for i in range(numComb):
        matrizAux[i][0] = combinaciones[i]
        matrizAux[i][1] = mediaNA(combinaciones[i])

        if (i == 0):
            medias.append(matrizAux[i][1])

        else:
            for j in range(len(medias)):
                if(medias[j] == matrizAux[i][1]):
                    break
                elif(j == len(medias) - 1):
                    medias.append(matrizAux[i][1])

    quicksort(medias, 0, len(medias) - 1)

    matriz = crearMatriz(len(medias) + 1, 4)

    for i in range(len(medias)):
        auxStr = ""
        contador = 0

        for j in range(numComb):
            if(medias[i] == matrizAux[j][1]):
                auxStr += str(matrizAux[j][0])
                auxStr += "\n"
                contador += 1

        matriz[i][0] = auxStr
        matriz[i][1] = medias[i]
        matriz[i][2] = contador
        matriz[i][3] = str(contador) + "/" +  str(numComb) + "  " + str(round(contador / numComb, 5))

    matriz[len(medias)][3]= " 1   ~   1"
    matriz[len(medias)][2] = numComb
    matriz[len(medias)][1] = ""
    matriz[len(medias)][0] = ""

    return matriz
