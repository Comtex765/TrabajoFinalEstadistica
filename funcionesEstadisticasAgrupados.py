def transformarStringAEntero(valor):
    return int(valor)

#######################################################################################
#------------------------------Medidas Tendencia Central------------------------------#
#######################################################################################


def mediaDA(num, fI, fAc, mC):
    """
    Calcula la media de un conjunto de datos agrupados
    """
    media = 0

    for i in range(num):
        valEntero = transformarStringAEntero(fI[i].get())
        media = media + (mC[i] * valEntero)

    media = media / fAc[num - 1]

    return round(media, 5)


def medianaDA(num, lI, lS,  fI, fAc):
    """
    Calcula la mediana de un grupo de datos agrupados
    """
    enteroLI = list()
    enteroLS = list()
    enteroFI = list()

    for i in range(num):
        enteroLI.append(transformarStringAEntero(lI[i].get()))
        enteroLS.append(transformarStringAEntero(lS[i].get()))
        enteroFI.append(transformarStringAEntero(fI[i].get()))

    mitadClase = fAc[num - 1] / 2
    limiteInferior = 0
    amplitud = (enteroLS[0] - enteroLI[0])

    for i in range(num):
        if(fAc[i - 1] < mitadClase and fAc[i] > mitadClase):
            limiteInferior = i

    mediana = enteroLI[limiteInferior] + \
        ((mitadClase - fAc[limiteInferior - 1]) /
         enteroFI[limiteInferior]) * amplitud

    return round(mediana, 5)


def modaDA(num, lI, lS, fI):
    """
    Calcula la moda de un grupo de datos agrupados
    """

    enteroLI = list()
    enteroLS = list()
    enteroFI = list()

    for i in range(num):
        enteroLI.append(transformarStringAEntero(lI[i].get()))
        enteroLS.append(transformarStringAEntero(lS[i].get()))
        enteroFI.append(transformarStringAEntero(fI[i].get()))

    global diferenciaInferior
    global diferenciaSuperior

    mayor = 0

    for i in range(num):
        if(enteroFI[i] > enteroFI[mayor]):
            mayor = i

    if (mayor == 0):
        diferenciaInferior = 0
        diferenciaSuperior = (enteroFI[mayor] - enteroFI[mayor + 1])
    elif (mayor == num - 1):
        diferenciaInferior = (enteroFI[mayor] - enteroFI[mayor - 1])
        diferenciaSuperior = 0
    else:
        diferenciaInferior = (enteroFI[mayor] - enteroFI[mayor - 1])
        diferenciaSuperior = (enteroFI[mayor] - enteroFI[mayor + 1])

    amplitud = (enteroLS[0] - enteroLI[0])

    moda = enteroLI[mayor] + (diferenciaInferior /
                              (diferenciaInferior + diferenciaSuperior)) * amplitud


    return round(moda, 5)


#######################################################################################
#------------------------------Medidas Varabilidad------------------------------------#
#######################################################################################
def rangoDA(num, lI, lS):
    inf = transformarStringAEntero(lI[0].get())
    sup = transformarStringAEntero(lS[num - 1].get())

    rango = sup - inf


    return rango


def desviacionMediaDA(num, lI, fI, fAc, mC):
    enteroLI = list()
    enteroFI = list()

    for i in range(num):
        enteroLI.append(transformarStringAEntero(lI[i].get()))
        enteroFI.append(transformarStringAEntero(fI[i].get()))

    sumatoria = 0

    media = mediaDA(num, fI, fAc, mC)

    for i in range(num):
        sumatoria += abs(mC[i] - media) * enteroFI[i]

    desviacionMedia = sumatoria / fAc[num - 1]

    return round(desviacionMedia, 5)


def varianzaDA(num, fI, fAc, mC):
    enteroFI = list()

    for i in range(num):
        enteroFI.append(transformarStringAEntero(fI[i].get()))

    sumatoria = 0

    media = mediaDA(num, fI, fAc, mC)

    for i in range(num):
        sumatoria += ((mC[i] - media)**2) * enteroFI[i]

    varianza = sumatoria / fAc[num - 1]

    return round(varianza, 5)


def desviacionEstandarDA(num, fI, fAc, mC):
    desviacionEstandar = varianzaDA(num, fI, fAc, mC) ** 0.5

    return round(desviacionEstandar, 5)


#######################################################################################
#------------------------------Medidas de Forma---------------------------------------#
#######################################################################################
def sesgoDA(num, lI, lS,  fI, fAc, mC):
    sesgo = 3 * (mediaDA(num, fI, fAc, mC) - medianaDA(num, lI,
                 lS, fI, fAc)) / varianzaDA(num, fI, fAc, mC)

    return round(sesgo, 5)


def curtosisDA(num, fI, fAc, mC):
    enteroFI = list()

    for i in range(num):
        enteroFI.append(transformarStringAEntero(fI[i].get()))

    sumatoria = 0

    for i in range(num):
        sumatoria += (((mC[i] - mediaDA(num, fI, fAc, mC)))**4) * enteroFI[i]

    curtosis = (sumatoria / ((fAc[num - 1]) *
                desviacionEstandarDA(num, fI, fAc, mC)**4)) - 3


    return round(curtosis, 5)

#######################################################################################
#------------------------------Medidas de Posicion------------------------------------#
#######################################################################################


def medidaPosicionDA(num, lI, lS, fAc, valor, medidaPos):
    """
    Calcula cuartiles, deciles y percentiles de datos agrupados
    parámetro valor --> indica qué medida de posición calcular
    """

    enteroLI = list()
    enteroLS = list()

    for i in range(num):
        enteroLI.append(transformarStringAEntero(lI[i].get()))
        enteroLS.append(transformarStringAEntero(lS[i].get()))

    FAnterior = 0
    FPosterior = 0
    lInferior = 0
    amplitud = 0

    if (valor == 1):
        lim = 4
    elif(valor == 2):
        lim = 10
    else:
        lim = 100

    posicion = medidaPos * fAc[num - 1] / lim

    for i in range(num):
        if (fAc[i] == posicion):
            return enteroLS[i]

    for i in range(num):
        if(fAc[i - 1] < posicion and posicion < fAc[i]):
            FAnterior = fAc[i - 1]
            FPosterior = fAc[i]
            lInferior = enteroLI[i]
            amplitud = enteroLS[0] - enteroLI[0]

            resultado = lInferior + amplitud * \
                ((posicion - FAnterior) / (FPosterior - FAnterior))
            return round(resultado, 5)

        elif(i == 0 and posicion < fAc[i]):
            FAnterior = 0
            FPosterior = fAc[i]
            lInferior = enteroLI[i]
            amplitud = enteroLS[0] - enteroLI[0]

            resultado = lInferior + amplitud * \
                ((posicion - FAnterior) / (FPosterior - FAnterior))
            return round(resultado, 5)