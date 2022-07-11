from tabulate import tabulate
from funcionesEstadisticasAgrupados import transformarStringAEntero as transformar

# ======================================Funciones=======================================#


def crearMatriz(filas, columnas):
    # Crea una matriz de las dimensiones de los parámetros
    matriz = []
    for i in range(filas):
        matriz.append([0]*columnas)

    return matriz


def mostrarResultadosDA(num, matriz):
    """
    Muestra la tabla de intervalos con el correspondiente 
    mensaje según el valor que se haya tenido que calcular
    """

    imprimir = crearMatriz(num + 1, 4)

    for i in range(num):
        """print(f"num valeee {num} --- matriz valeeeeee {len(matriz)} ---- i vale {i} ----- ")"""

        imprimir[i][0] = str(matriz[i][0].get()) + \
            " - " + str(matriz[i][1].get())
        imprimir[i][1] = transformar(matriz[i][2].get())
        imprimir[i][2] = transformar(matriz[i][3])
        imprimir[i][3] = transformar(matriz[i][4])
    
    imprimir[num][0] = "TOTAL"
    imprimir[num][1] = matriz[num][2]
    imprimir[num][2] = ''
    imprimir[num][3] = ''

    print(f"La tabla de datos agrupados es:\n")
    return(tabulate(imprimir, headers=[
        'Intervalo', 'fi', 'Fi', 'Marca de clase'], tablefmt="grid", numalign="center", stralign="center"))


def unificarDA(lI, lS, fI, fAc, mC, num):
    matriz = crearMatriz(num + 1, 5)

    for i in range(num):
        """print(f"num valeee {num} --- matriz valeeeeee {len(matriz)} ---- i vale {i} ----- lI vale {lI[i].get()}")
        print(type(lI[i]))
        print(type(lS[i]))
        print(type(fI[i]))
        print(type(mC[i]))"""

        matriz[i][0] = lI[i]
        matriz[i][1] = lS[i]
        matriz[i][2] = fI[i]
        matriz[i][3] = fAc[i]
        matriz[i][4] = mC[i]

        matriz[num][2] += transformar(matriz[i][2].get())


    return matriz
