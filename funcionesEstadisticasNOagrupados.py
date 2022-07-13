from math import floor, trunc
from statistics import mode


def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)


def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda]
    while True:
        # Mientras cada elemento desde la izquierda esté en orden (sea menor que el
        # pivote) continúa avanzando el índice
        while arreglo[izquierda] < pivote:
            izquierda += 1

        # Mientras cada elemento desde la derecha esté en orden (sea mayor que el
        # pivote) continúa disminuyendo el índice
        while arreglo[derecha] > pivote:
            derecha -= 1

        """
            Si la izquierda es mayor o igual que la derecha significa que no
            necesitamos hacer ningún intercambio
            de variables, pues los elementos ya están en orden (al menos en esta
            iteración)
        """
        if izquierda >= derecha:
            # Indicar "en dónde nos quedamos" para poder dividir el arreglo de nuevo
            # y ordenar los demás elementos
            return derecha
        else:
            # Nota: yo sé que el else no hace falta por el return round(de arriba, pero así el algoritmo es más claro
            """
                Si las variables quedaron "lejos" (es decir, la izquierda no superó ni
                alcanzó a la derecha)
                significa que se detuvieron porque encontraron un valor que no estaba
                en orden, así que lo intercambiamos
            """
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            """
                Ya intercambiamos, pero seguimos avanzando los índices
            """
            izquierda += 1
            derecha -= 1

#######################################################################################
#------------------------------Medidas Tendencia Central------------------------------#
#######################################################################################


def mediaNA(datos):
    """
    Calcula la media de un conjunto de datos agrupados
    """
    media = 0

    for i in range(len(datos)):
        media += datos[i]

    media = media / len(datos)

    return round(media, 5)


def medianaNA(datos):
    """
    Calcula la mediana de un grupo de datos agrupados
    """
    quicksort(datos, 0, len(datos) - 1)

    mitadClase = trunc(len(datos) / 2)

    if(len(datos) % 2 == 0):
        mediana = (datos[mitadClase] + datos[mitadClase - 1]) / 2
    else:
        mediana = datos[mitadClase]

    return round(mediana, 5)


def modaNA(datos):
    """
    Calcula la moda de un grupo de datos agrupados
    """

    quicksort(datos, 0, len(datos) - 1)

    moda = mode(datos)

    return round(moda, 5)


#######################################################################################
#------------------------------Medidas Varabilidad------------------------------------#
#######################################################################################
def rangoNA(datos):
    quicksort(datos, 0, len(datos) - 1)

    rango = datos[len(datos) - 1] - datos[0]

    return round(rango, 5)


def desviacionMediaNA(datos):
    sumatoria = 0

    mediaDat = mediaNA(datos)

    for i in range(len(datos)):
        sumatoria += abs(datos[i] - mediaDat)


    desviacionMedia = sumatoria / len(datos)

    return round(desviacionMedia, 5)


def varianzaNA(datos):
    sumatoria = 0

    mediaDat = mediaNA(datos)

    for i in range(len(datos)):
        sumatoria += ((datos[i] - mediaDat)**2)

    varianza = sumatoria / len(datos)

    return round(varianza, 5)


def desviacionEstandarNA(datos):
    desviacionEstandar = varianzaNA(datos) ** 0.5

    return round(desviacionEstandar, 5)


#######################################################################################
#------------------------------Medidas de Forma---------------------------------------#
#######################################################################################
def sesgoNA(datos):
    k = len(datos) / ((len(datos) - 1) * (len(datos) - 2))

    sumatoria = 0
    mediaDat = mediaNA(datos)
    desvEst = desviacionEstandarNA(datos)

    for i in range(len(datos)):
        sumatoria += ((datos[i] - mediaDat) / desvEst)**3

    sesgo = k * sumatoria

    return round(sesgo, 5)


def curtosisNA(datos):
    sumatoria = 0

    for i in range(len(datos)):
        sumatoria += ((datos[i] - mediaNA(datos))**4)

    sumatoria /= len(datos)

    curtosis = ((sumatoria / (len(datos))) /
                (len(datos) * varianzaNA(datos)**4)) - 3

    return round(curtosis, 5)

#######################################################################################
#------------------------------Medidas de Posicion------------------------------------#
#######################################################################################


def medidaPosicionNA(datos, valor, medidaPos):
    """
    Calcula cuartiles, deciles y percentiles de datos agrupados
    parámetro valor --> indica qué medida de posición calcular
    """

    quicksort(datos, 0, len(datos) - 1)

    if (valor == 1):
        lim = 4
    elif(valor == 2):
        lim = 10
    else:
        lim = 100

    posicion = medidaPos * (len(datos) + 1) / lim

    if(floor(posicion) == posicion):
        return round(datos[floor(posicion - 1)], 5)
    else:
        return round(datos[floor(posicion) - 1] + ((datos[floor(posicion)] - datos[floor(posicion) - 1]) * (posicion - floor(posicion))), 5)