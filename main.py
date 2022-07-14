from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
from pygal import Histogram
from pygal.style import Style

from funcionesEstadisticasAgrupados import *
from funcionesNuevaVentanaAgrupados import *

from funcionesEstadisticasNOagrupados import *
from funcionesNuevaVentanaNOagrupados import *

from funcionesNuevaVentanaDistribucionMuestralMedia import *

from funcionesNuevaVentanaCorrelacion import *


#==============================================GLOBAL VENTANA==================================#
global raizVentana
raizVentana = Tk()
raizVentana.title("ESTADISTICA")

# ================================VARIABLES GLOBALES DATOS AGRUPADOS====================================#
# Asigna el valor del limite inferior al primer elemento del arreglo lI_DatosAgrupados
global inicioLI_DatosAgrupados
# Asigna el valor del limite superior al primer elemento del arreglo lS_DatosAgrupados
global inicioLS_DatosAgrupados
# Guarda el número de las clases que van a crearse en una StringVar
global numClases_DatosAgrupados
global lI_DatosAgrupados  # Guarda en un arreglo los límites inferiores de las clases
global lS_DatosAgrupados  # Guarda en un arreglo los límites superiores de las clases
global fI_DatosAgrupados  # Guarda en un arreglo la frecuencia absoluta de las clases
global fAc_DatosAgrupados  # Guarda en un arreglo la frecuencia acumulada de las clases
global mC_DatosAgrupados  # Guarda en un arreglo la marca de las clases
global entradafI_DatosAgrupados  # Es el arrelgo de ENTRY's de las frecuencias
# Arreglo de LABEL's que muestran los intervalos de clase
global intervalosTexto_DatosAgrupados

global entradaCuartil_DatosAgrupados
global entradaDecil_DatosAgrupados
global entradaPercentil_DatosAgrupados

global frameSuperior_DatosAgrupados
global frameTabla_DatosAgrupados

global boolMedia_DatosAgrupados
global boolMediana_DatosAgrupados
global boolModa_DatosAgrupados
global boolRango_DatosAgrupados
global boolDesviacionMedia_DatosAgrupados
global boolVarianza_DatosAgrupados
global boolDesviacionEstandar_DatosAgrupados
global boolSesgo_DatosAgrupados
global boolCurtosis_DatosAgrupados
global boolCuartil_DatosAgrupados
global boolDecil_DatosAgrupados
global boolPercentil_DatosAgrupados
global boolHistograma_DatosAgrupados

inicioLI_DatosAgrupados = StringVar()
iniciolS_DatosAgrupados = StringVar()

numClases_DatosAgrupados = StringVar()
numClases_DatosAgrupados.set("")

entradaCuartil_DatosAgrupados = StringVar()
entradaDecil_DatosAgrupados = StringVar()
entradaPercentil_DatosAgrupados = StringVar()

boolMedia_DatosAgrupados = IntVar()
boolMediana_DatosAgrupados = IntVar()
boolModa_DatosAgrupados = IntVar()
boolRango_DatosAgrupados = IntVar()
boolDesviacionMedia_DatosAgrupados = IntVar()
boolVarianza_DatosAgrupados = IntVar()
boolDesviacionEstandar_DatosAgrupados = IntVar()
boolSesgo_DatosAgrupados = IntVar()
boolCurtosis_DatosAgrupados = IntVar()
boolCuartil_DatosAgrupados = IntVar()
boolDecil_DatosAgrupados = IntVar()
boolPercentil_DatosAgrupados = IntVar()
boolHistograma_DatosAgrupados = IntVar()

lI_DatosAgrupados = []
lS_DatosAgrupados = []
fI_DatosAgrupados = []
fAc_DatosAgrupados = []
mC_DatosAgrupados = []


entradafI_DatosAgrupados = []

intervalosTexto_DatosAgrupados = []

# ================================VARIABLES GLOBALES DATOS NO AGRUPADOS EN LISTA====================================#
# Datos ingresados en el text, son string
global datosStringEnlistados_DatosNoAgrupados
# Se procesan los datos de datosString para que sean enteros
global datosIntEnlistados_DatosNoAgrupados
global fIEnlistados_DatosNoAgrupados

global entradaDatosEnlistados_DatosNoAgrupados
global entradaCuartilEnlistados_DatosNoAgrupados
global entradaDecilEnlistados_DatosNoAgrupados
global entradaPercentilEnlistados_DatosNoAgrupados

global frameSuperiorEnlistadosEnlistados_DatosNoAgrupados
global frameTablaA1Enlistados_DatosNoAgrupados

global boolMediaEnlistados_DatosNoAgrupados
global boolMedianaEnlistados_DatosNoAgrupados
global boolModaEnlistados_DatosNoAgrupados
global boolRangoEnlistados_DatosNoAgrupados
global boolDesviacionMediaEnlistados_DatosNoAgrupados
global boolVarianzaEnlistados_DatosNoAgrupados
global boolDesviacionEstandarEnlistados_DatosNoAgrupados
global boolSesgoEnlistados_DatosNoAgrupados
global boolCurtosisEnlistados_DatosNoAgrupados
global boolCuartilEnlistados_DatosNoAgrupados
global boolDecilEnlistados_DatosNoAgrupados
global boolPercentilEnlistados_DatosNoAgrupados

entradaCuartilEnlistados_DatosNoAgrupados = StringVar()
entradaDecilEnlistados_DatosNoAgrupados = StringVar()
entradaPercentilEnlistados_DatosNoAgrupados = StringVar()

boolMediaEnlistados_DatosNoAgrupados = IntVar()
boolMedianaEnlistados_DatosNoAgrupados = IntVar()
boolModaEnlistados_DatosNoAgrupados = IntVar()
boolRangoEnlistados_DatosNoAgrupados = IntVar()
boolDesviacionMediaEnlistados_DatosNoAgrupados = IntVar()
boolVarianzaEnlistados_DatosNoAgrupados = IntVar()
boolDesviacionEstandarEnlistados_DatosNoAgrupados = IntVar()
boolSesgoEnlistados_DatosNoAgrupados = IntVar()
boolCurtosisEnlistados_DatosNoAgrupados = IntVar()
boolCuartilEnlistados_DatosNoAgrupados = IntVar()
boolDecilEnlistados_DatosNoAgrupados = IntVar()
boolPercentilEnlistados_DatosNoAgrupados = IntVar()

fIEnlistados_DatosNoAgrupados = []
datosIntEnlistados_DatosNoAgrupados = []

# ================================VARIABLES GLOBALES DATOS NO AGRUPADOS EN TABLA====================================#
global entradaValoresTabla_DatosNoAgrupados
global entradafITabla_DatosNoAgrupados

global valoresTabla_DatosNoAgrupados
global fITabla_DatosNoAgrupados

# Se procesan los datos de datosString para que sean enteros
global datosIntTabla_DatosNoAgrupados

global numValoresTabla_DatosNoAgrupados

global entradaDatosTabla_DatosNoAgrupados
global entradaCuartilTabla_DatosNoAgrupados
global entradaDecilTabla_DatosNoAgrupados
global entradaPercentilTabla_DatosNoAgrupados

global frameSuperiorTabla_DatosNoAgrupados
global frameTablaA2_DatosNoAgrupados

global boolMediaTabla_DatosNoAgrupados
global boolMedianaTabla_DatosNoAgrupados
global boolModaTabla_DatosNoAgrupados
global boolRangoTabla_DatosNoAgrupados
global boolDesviacionMediaTabla_DatosNoAgrupados
global boolVarianzaTabla_DatosNoAgrupados
global boolDesviacionEstandarTabla_DatosNoAgrupados
global boolSesgoTabla_DatosNoAgrupados
global boolCurtosisTabla_DatosNoAgrupados
global boolCuartilTabla_DatosNoAgrupados
global boolDecilTabla_DatosNoAgrupados
global boolPercentilTabla_DatosNoAgrupados

entradaCuartilTabla_DatosNoAgrupados = StringVar()
entradaDecilTabla_DatosNoAgrupados = StringVar()
entradaPercentilTabla_DatosNoAgrupados = StringVar()

numValoresTabla_DatosNoAgrupados = StringVar()

boolMediaTabla_DatosNoAgrupados = IntVar()
boolMedianaTabla_DatosNoAgrupados = IntVar()
boolModaTabla_DatosNoAgrupados = IntVar()
boolRangoTabla_DatosNoAgrupados = IntVar()
boolDesviacionMediaTabla_DatosNoAgrupados = IntVar()
boolVarianzaTabla_DatosNoAgrupados = IntVar()
boolDesviacionEstandarTabla_DatosNoAgrupados = IntVar()
boolSesgoTabla_DatosNoAgrupados = IntVar()
boolCurtosisTabla_DatosNoAgrupados = IntVar()
boolCuartilTabla_DatosNoAgrupados = IntVar()
boolDecilTabla_DatosNoAgrupados = IntVar()
boolPercentilTabla_DatosNoAgrupados = IntVar()


entradaValoresTabla_DatosNoAgrupados = []
entradafITabla_DatosNoAgrupados = []

valoresTabla_DatosNoAgrupados = []
fITabla_DatosNoAgrupados = []


datosIntTabla_DatosNoAgrupados = []
fITabla_DatosNoAgrupados = []

# ================================VARIABLES GLOBALES DISTRIBUCION MUESTRAL====================================#
global datosString_MediaMuestral
global datosInt_MediaMuestral

global tamanioString_MediaMuestral
global tamanioInt_MediaMuestral

global frameSuperior_MediaMuestral

datosInt_MediaMuestral = []

tamanioString_MediaMuestral = StringVar()
tamanioInt_MediaMuestral = 1

# ================================VARIABLES GLOBALES CORRELACION====================================#
global datosString_X_Correlacion
global datosInt_X_Correlacion

global datosString_Y_Correlacion
global datosInt_Y_Correlacion

global frameSuperior_Correlacion

datosInt_X_Correlacion = []
datosInt_Y_Correlacion = []

# ======================================FUNCIONES DATOS AGRUPADOS=======================================#


def transformarStringAEntero(valor):
    try:
        int(valor)
    except ValueError:
        try:
            float(valor)
            messagebox.showinfo("FUNCIONALIDAD NO IMPLEMENTADA",
                                "Aún no se han implementado las clases con flotantes :(")
        except ValueError:
            messagebox.showerror("ERROR", "Debes ingresar números")
        else:
            return
    else:
        return int(valor)


def comprobarDatosInicio_DatosAgrupados(inf, sup):
    if(inf == "" or sup == "" or numClases_DatosAgrupados.get() == ""):
        messagebox.showerror(
            "ERROR", "Debes ingresar los 3 datos para continuar")
    else:
        try:
            inf = transformarStringAEntero(inicioLI_DatosAgrupados.get())

            sup = transformarStringAEntero(iniciolS_DatosAgrupados.get())

            clases = transformarStringAEntero(numClases_DatosAgrupados.get())

            if(clases > 15):
                messagebox.showerror(
                    "ERROR", "El número máximo de clases es 15")
            elif(inf > sup):
                messagebox.showerror(
                    "ERROR", "El límite inferior no puede ser mayor que el superior")
            elif(inf == sup):
                messagebox.showerror(
                    "ERROR", "Los límites no pueden ser iguales")
            elif(inf < 0):
                messagebox.showerror(
                    "ERROR", "Los límites no pueden ser negativos")
            elif(clases <= 0):
                messagebox.showerror(
                    "ERROR", "El número de clases no puede ser 0 o menor")
            else:
                crearCuadrosTexto_DatosAgrupados()
        except TypeError:
            pass


def crearCuadrosTexto_DatosAgrupados():
    num = transformarStringAEntero(numClases_DatosAgrupados.get())

    Label(
        frameTabla_DatosAgrupados,
        text="Intervalo",
        width=20,
        pady=10,
        font=("Kristen ITC", 11)
    ).grid(
        row=0,
        column=0,
        pady=10,
        padx=5
    )

    Label(
        frameTabla_DatosAgrupados,
        text="Frecuencia Absoluta",
        width=21,
        pady=10,
        font=("Kristen ITC", 11)
    ).grid(
        row=0,
        column=1,
        pady=10,
        padx=5
    )

    if(len(lI_DatosAgrupados) > 0):
        # Este condicional borra los cuadros generados por el número de clases ingresados
        # Para mostrar el nuevo número según se ingrese
        for i in range(0, len(lI_DatosAgrupados)):
            entradafI_DatosAgrupados[i].grid_forget()

            intervalosTexto_DatosAgrupados[i].grid_forget()

        while (len(lI_DatosAgrupados) > 0):
            entradafI_DatosAgrupados.pop()

            lI_DatosAgrupados.pop()
            lS_DatosAgrupados.pop()
            fI_DatosAgrupados.pop()
            fAc_DatosAgrupados.pop()

            if(len(mC_DatosAgrupados) > 0):
                mC_DatosAgrupados.pop()

            intervalosTexto_DatosAgrupados.pop()

    for i in range(0, num):
        lI_DatosAgrupados.append(StringVar())
        lS_DatosAgrupados.append(StringVar())
        fI_DatosAgrupados.append(StringVar())
        fAc_DatosAgrupados.append(StringVar())

        entradafI_DatosAgrupados.append(0)

        intervalosTexto_DatosAgrupados.append(0)

        if (i == 0):
            lI_DatosAgrupados[0] = inicioLI_DatosAgrupados
            lS_DatosAgrupados[0] = iniciolS_DatosAgrupados
        else:
            lI_DatosAgrupados[i] = lS_DatosAgrupados[i - 1]
            lS_DatosAgrupados[i] = calcularLimiteSuperior(
                lI_DatosAgrupados[i].get())

        entradafI_DatosAgrupados[i] = Entry(
            frameTabla_DatosAgrupados,
            width=7,
            textvariable=fI_DatosAgrupados[i],
            justify="center",
            bg="#e9e4eb",
            bd=2,
            relief="groove",
        )
        entradafI_DatosAgrupados[i].grid(
            row=i + 1,
            column=1,
        )

        intervalosTexto_DatosAgrupados[i] = Label(
            frameTabla_DatosAgrupados,
            text=f"[{lI_DatosAgrupados[i].get()}, {lS_DatosAgrupados[i].get()})",
            width=20,
            font=("Comic Sans MS", 13),
            pady=2)
        intervalosTexto_DatosAgrupados[i].grid(
            row=i + 1,
            column=0,
            padx=5
        )

    botonLlenarTabla_DatosAgrupados.grid(
        row=num + 4,
        column=0,
        columnspan=2,
        pady=15
    )

    botonConfirmarCalculos_DatosAgrupados.grid_forget()


def crearHistograma_DatosAgrupados():
    frecuenciasInt = []
    liInt = []
    lsInt = []

    for i in range(len(fI_DatosAgrupados)):
        frecuenciasInt.append(transformarStringAEntero(fI_DatosAgrupados[i].get()))
        liInt.append(transformarStringAEntero(lI_DatosAgrupados[i].get()))
        lsInt.append(transformarStringAEntero(lS_DatosAgrupados[i].get()))

    print(frecuenciasInt)

    datos = []

    # generamos la lista de tuplas con la información de cada intervalo
    for i, valor in enumerate(frecuenciasInt):
        datos.append((valor, liInt[i], lsInt[i]))

    estilo = Style(colors=['#F2AB6D', '#F2AA6D']) # creamos un estilo para darle color a las barras

    # creamos el histograma y añadimos los datos
    histograma = Histogram(title='Histograma\nDesarrollado por Fernando Novillo & Edison Azogue',
                        x_title='intervalos', 
                        y_title='frecuencias', 
                        style=estilo)

    histograma.add('Intervalos', datos)

    histograma.render_in_browser();


def calcularLimiteSuperior(inferior):
    rango = transformarStringAEntero(
        iniciolS_DatosAgrupados.get()) - transformarStringAEntero(inicioLI_DatosAgrupados.get())
    suma = transformarStringAEntero(inferior) + rango
    suma = str(suma)

    a = StringVar(value=suma)

    return a


def comprobarDatosFrecuencia(valor):

    for i in range(transformarStringAEntero(numClases_DatosAgrupados.get())):
        if(fI_DatosAgrupados[i].get() == ""):
            messagebox.showerror("ERROR", "No debes dejar espacios vacíos")
            return

    try:
        for i in range(transformarStringAEntero(numClases_DatosAgrupados.get())):
            a = int(fI_DatosAgrupados[i].get())
        if (a <= 0):
            messagebox.showerror(
                "ERROR", "La frecuencia no puede ser 0 o menor")
            return
    except ValueError:
        messagebox.showerror("ERROR", "Debes ingresar números")
    else:
        if (valor == 1):
            mostrarDatos_DatosAgrupados()
        elif (valor == 2):
            revisarBotonesMedidas_DatosAgrupados()


def mostrarDatos_DatosAgrupados():
    mostrarBotonesDeOpciones_DatosAgrupados()
    calcularFrecuenciaAcumulada()
    calcularMarcaClase()


def mostrarBotonesDeOpciones_DatosAgrupados():
    Label(
        frameTabla_DatosAgrupados,
        text="Calcular",
        width=20,
        pady=10,
        font=("Kristen ITC", 11)
    ).grid(
        row=0,
        column=2,
        pady=10,
        padx=5,
        columnspan=3
    )

    botonSeleccionarMedia_DatosAgrupados.grid(
        row=1,
        column=2,
        sticky="w"
    )

    botonSeleccionarMediana_DatosAgrupados.grid(
        row=1,
        column=3,
        sticky="w"
    )

    botonSeleccionarModa_DatosAgrupados.grid(
        row=1,
        column=4,
        sticky="w"
    )

    botonSeleccionarRango_DatosAgrupados.grid(
        row=2,
        column=2,
        sticky="w"
    )

    botonSeleccionarDesviacionMedia_DatosAgrupados.grid(
        row=2,
        column=3,
        sticky="w"
    )

    botonSeleccionarVarianza_DatosAgrupados.grid(
        row=2,
        column=4,
        sticky="w"
    )

    botonSeleccionarDesviacionEstandar_DatosAgrupados.grid(
        row=3,
        column=2,
        sticky="w"
    )

    botonSeleccionarSesgo_DatosAgrupados.grid(
        row=3,
        column=3,
        sticky="w"
    )

    botonSeleccionarCurtosis_DatosAgrupados.grid(
        row=3,
        column=4,
        sticky="w"
    )

    botonSeleccionarCuartil_DatosAgrupados.grid(
        row=4,
        column=2,
        sticky="w"
    )

    botonSeleccionarDecil_DatosAgrupados.grid(
        row=4,
        column=3,
        sticky="w"
    )

    botonSeleccionarPercentil_DatosAgrupados.grid(
        row=4,
        column=4,
        sticky="w"
    )
    
    botonSeleccionarHistograma_DatosAgrupados.grid(
        row=6,
        column=2,
        sticky="w"
    )

    botonConfirmarCalculos_DatosAgrupados.grid(
        row=transformarStringAEntero(numClases_DatosAgrupados.get()) + 4,
        column=2,
        pady=15,
        columnspan=3
    )


def calcularFrecuenciaAcumulada():
    fAc_DatosAgrupados[0] = transformarStringAEntero(
        fI_DatosAgrupados[0].get())

    for i in range(1, transformarStringAEntero(numClases_DatosAgrupados.get())):

        anterior = fAc_DatosAgrupados[i - 1]

        actual = fI_DatosAgrupados[i].get()
        actual = int(actual)

        suma = anterior + actual

        fAc_DatosAgrupados[i] = suma


def calcularMarcaClase():
    for i in range(transformarStringAEntero(numClases_DatosAgrupados.get())):
        limI = transformarStringAEntero(lI_DatosAgrupados[i].get())
        limS = transformarStringAEntero(lS_DatosAgrupados[i].get())
        mC_DatosAgrupados.append((limI + limS) / 2)


def revisarBotonesMedidas_DatosAgrupados():
    texto_extra = ""

    num = transformarStringAEntero(numClases_DatosAgrupados.get())
    check = False

    if(boolMedia_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> La media es: {mediaDA(num, fI_DatosAgrupados, fAc_DatosAgrupados, mC_DatosAgrupados)}"
        check = True

    if(boolMediana_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> La mediana es: {medianaDA(num, lI_DatosAgrupados, lS_DatosAgrupados, fI_DatosAgrupados, fAc_DatosAgrupados)}"
        check = True

    if(boolModa_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> La moda es: {modaDA(num, lI_DatosAgrupados, lS_DatosAgrupados, fI_DatosAgrupados)}"
        check = True

    if(boolRango_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> El rango es: {rangoDA(num, lI_DatosAgrupados, lS_DatosAgrupados)}"
        check = True

    if(boolDesviacionMedia_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> La desviación media es: {desviacionMediaDA(num, lI_DatosAgrupados, fI_DatosAgrupados, fAc_DatosAgrupados, mC_DatosAgrupados)}"
        check = True

    if(boolVarianza_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> La varianza es: {varianzaDA(num, fI_DatosAgrupados, fAc_DatosAgrupados, mC_DatosAgrupados)}"
        check = True

    if(boolDesviacionEstandar_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> La desviación estándar es: {desviacionEstandarDA(num, fI_DatosAgrupados, fAc_DatosAgrupados, mC_DatosAgrupados)}"
        check = True

    if(boolSesgo_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> El sesgo es: {sesgoDA(num, lI_DatosAgrupados, lS_DatosAgrupados, fI_DatosAgrupados, fAc_DatosAgrupados, mC_DatosAgrupados)}"
        check = True

    if(boolCurtosis_DatosAgrupados.get() == 1):
        texto_extra += f"\n-> La curtosis es: {curtosisDA(num, fI_DatosAgrupados, fAc_DatosAgrupados, mC_DatosAgrupados)}"
        check = True

    if(boolCuartil_DatosAgrupados.get() == 1):
        posC = transformarStringAEntero(entradaCuartil_DatosAgrupados.get())

        if(posC < 1 or posC > 3):
            messagebox.showerror("ERROR", "El cuartil va de 1 a 3!")
            check = False
        else:
            texto_extra += f"\n-> El {posC} cuartil es {medidaPosicionDA(num, lI_DatosAgrupados, lS_DatosAgrupados, fAc_DatosAgrupados, 1, posC)}"
            check = True

    if(boolDecil_DatosAgrupados.get() == 1):
        posD = transformarStringAEntero(entradaDecil_DatosAgrupados.get())

        if(posD < 1 or posD > 9):
            messagebox.showerror("ERROR", "El decil va de 1 a 9!")
            check = False
        else:
            texto_extra += f"\n-> El {posD} decil es {medidaPosicionDA(num, lI_DatosAgrupados, lS_DatosAgrupados, fAc_DatosAgrupados, 2, posD)}"
            check = True

    if(boolPercentil_DatosAgrupados.get() == 1):
        posP = transformarStringAEntero(entradaPercentil_DatosAgrupados.get())

        if(posP < 1 or posP > 99):
            messagebox.showerror("ERROR", "El Percentil va de 1 a 99!")
            check = False
        else:
            texto_extra += f"\n-> El {posP} percentil es {medidaPosicionDA(num, lI_DatosAgrupados, lS_DatosAgrupados, fAc_DatosAgrupados, 3, posP)}"
            check = True
    
    if(boolHistograma_DatosAgrupados.get() == 1):
        texto_extra += "\n-> El Histograma se encuentra en su navegador web"
        crearHistograma_DatosAgrupados()
        check = True

    if(check == True):
        crearVentana_DatosAgrupados(texto_extra)
    else:
        if(boolCuartil_DatosAgrupados.get() == 0 and boolPercentil_DatosAgrupados.get() == 0 and boolPercentil_DatosAgrupados.get() == 0):
            messagebox.showerror("ERROR", "Selecciona al menos una medida")


def mostrarCuadroTextoCuartil_DatosAgrupados():
    textoEntradaCuartil = Entry(
        frameTabla_DatosAgrupados,
        textvariable=entradaCuartil_DatosAgrupados,
        width=5
    )

    if(boolCuartil_DatosAgrupados.get() == 1):
        textoEntradaCuartil.grid(
            row=5,
            column=2,
            sticky="n"
        )


def mostrarCuadroTextoDecil_DatosAgrupados():
    textoEntradaDecil = Entry(
        frameTabla_DatosAgrupados,
        textvariable=entradaDecil_DatosAgrupados,
        width=5
    )

    if(boolDecil_DatosAgrupados.get() == 1):
        textoEntradaDecil.grid(
            row=5,
            column=3,
            sticky="n"
        )


def mostrarCuadroTextoPercentil_DatosAgrupados():
    textoEntradaPercentil = Entry(
        frameTabla_DatosAgrupados,
        textvariable=entradaPercentil_DatosAgrupados,
        width=5
    )

    if(boolPercentil_DatosAgrupados.get() == 1):
        textoEntradaPercentil.grid(
            row=5,
            column=4,
            sticky="n"
        )


def crearVentana_DatosAgrupados(texto):
    #==================================CREACION VENTANA=====================================#
    num = transformarStringAEntero(numClases_DatosAgrupados.get())
    ventanaNueva = Toplevel()

    ventanaNueva.title("Tabla de Frecuencias")

    frameNuevaVentana = Frame(ventanaNueva)
    frameNuevaVentana.pack()

    matriz = unificarDA(lI_DatosAgrupados, lS_DatosAgrupados,
                        fI_DatosAgrupados, fAc_DatosAgrupados, mC_DatosAgrupados, num)

    tablaResultado = Text(
        frameNuevaVentana,
        width=70,
        height=40
    )

    tablaResultado.tag_configure('tag-center', justify='center')
    tablaResultado.insert(
        'end', mostrarResultadosDA(num, matriz), 'tag-center')

    tablaResultado.insert(END, "\n\n\n")
    tablaResultado.insert(END, texto)

    tablaResultado.grid(
        row=0,
        column=0
    )

    #=======================================BARRA DE SCROLL=================================#

    scrollVert = Scrollbar(
        frameNuevaVentana,
        command=tablaResultado.yview
    )

    scrollVert.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    tablaResultado.insert(
        END, "\n\n(: Desarrollado con amor por Fernando Novillo & Edison Azogue :) \n\t\t\t\t<3")

    tablaResultado.config(yscrollcommand=scrollVert.set, state="disabled")


# ======================================FUNCIONES DATOS NO AGRUPADOS EN LISTADO=======================================#
def comprobarDatosInicioEnlistados_DatosNoAgrupados():
    datosStringEnlistados_DatosNoAgrupados = entradaDatosEnlistados_DatosNoAgrupados.get(
        1.0, 'end')

    for i in range(len(datosStringEnlistados_DatosNoAgrupados)):
        if(datosStringEnlistados_DatosNoAgrupados[i] == ',' and datosStringEnlistados_DatosNoAgrupados[i + 1] == ','):
            messagebox.showerror("ERROR", "INGRESASTE [,] SEGUIDAS")
            return

    j = 0

    numero = ""

    while(len(datosIntEnlistados_DatosNoAgrupados) > 0):
        datosIntEnlistados_DatosNoAgrupados.pop()

    while(j < len(datosStringEnlistados_DatosNoAgrupados) - 1):
        if(datosStringEnlistados_DatosNoAgrupados[j] != ','):
            while(datosStringEnlistados_DatosNoAgrupados[j] != ',' and j < len(datosStringEnlistados_DatosNoAgrupados) - 1):
                numero += datosStringEnlistados_DatosNoAgrupados[j]
                j += 1
            try:
                entero = int(numero)
                datosIntEnlistados_DatosNoAgrupados.append(entero)
            except ValueError:
                messagebox.showerror("ERROR", "DEBES INGRESAR NUMEROS")
                j = len(datosStringEnlistados_DatosNoAgrupados)
                return

            numero = ""
        else:
            j += 1

    mostrarBotonesDeOpcionesEnlistados_DatosNoAgrupados()


def mostrarBotonesDeOpcionesEnlistados_DatosNoAgrupados():
    Label(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Calcular",
        width=20,
        pady=10,
        font=("Kristen ITC", 11)
    ).grid(
        row=0,
        column=2,
        pady=10,
        padx=5,
        columnspan=3
    )

    botonSeleccionarMediaEnlistados_DatosNoAgrupados.grid(
        row=1,
        column=2,
        sticky="w"
    )

    botonSeleccionarMedianaEnlistados_DatosNoAgrupados.grid(
        row=1,
        column=3,
        sticky="w"
    )

    botonSeleccionarModaEnlistados_DatosNoAgrupados.grid(
        row=1,
        column=4,
        sticky="w"
    )

    botonSeleccionarRangoEnlistados_DatosNoAgrupados.grid(
        row=2,
        column=2,
        sticky="w"
    )

    botonSeleccionarDesviacionMediaEnlistados_DatosNoAgrupados.grid(
        row=2,
        column=3,
        sticky="w"
    )

    botonSeleccionarVarianzaEnlistados_DatosNoAgrupados.grid(
        row=2,
        column=4,
        sticky="w"
    )

    botonSeleccionarDesviacionEstandarEnlistados_DatosNoAgrupados.grid(
        row=3,
        column=2,
        sticky="w"
    )

    botonSeleccionarSesgoEnlistados_DatosNoAgrupados.grid(
        row=3,
        column=3,
        sticky="w"
    )

    botonSeleccionarCurtosisEnlistados_DatosNoAgrupados.grid(
        row=3,
        column=4,
        sticky="w"
    )

    botonSeleccionarCuartilEnlistados_DatosNoAgrupados.grid(
        row=4,
        column=2,
        sticky="w"
    )

    botonSeleccionarDecilEnlistados_DatosNoAgrupados.grid(
        row=4,
        column=3,
        sticky="w"
    )

    botonSeleccionarPercentilEnlistados_DatosNoAgrupados.grid(
        row=4,
        column=4,
        sticky="w"
    )

    botonConfirmarCalculosEnlistados_DatosNoAgrupados.grid(
        row=8,
        column=2,
        pady=15,
        columnspan=3
    )


def revisarBotonesMedidasEnlistados_DatosNoAgrupados():
    texto_extra = ""

    check = False

    if(boolMediaEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La media es: {mediaNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolMedianaEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La mediana es {medianaNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolModaEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La moda es: {modaNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolRangoEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> El rango es: {rangoNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolDesviacionMediaEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La desviación media es: {desviacionMediaNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolVarianzaEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La varianza es: {varianzaNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolDesviacionEstandarEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La desviación estándar es: {desviacionEstandarNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolSesgoEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> El sesgo es: {sesgoNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolCurtosisEnlistados_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La curtosis es: {curtosisNA(datosIntEnlistados_DatosNoAgrupados)}"
        check = True

    if(boolCuartilEnlistados_DatosNoAgrupados.get() == 1):
        posC = transformarStringAEntero(
            entradaCuartilEnlistados_DatosNoAgrupados.get())

        if(posC < 1 or posC > 3):
            messagebox.showerror("ERROR", "El cuartil va de 1 a 3!")
            check = False
        else:
            texto_extra += f"\n-> El {posC} cuartil es {medidaPosicionNA(datosIntEnlistados_DatosNoAgrupados, 1, posC)}"
            check = True

    if(boolDecilEnlistados_DatosNoAgrupados.get() == 1):
        posD = transformarStringAEntero(
            entradaDecilEnlistados_DatosNoAgrupados.get())

        if(posD < 1 or posD > 9):
            messagebox.showerror("ERROR", "El decil va de 1 a 9!")
            check = False
        else:
            texto_extra += f"\n-> El {posD} decil es {medidaPosicionNA(datosIntEnlistados_DatosNoAgrupados,2, posD)}"
            check = True

    if(boolPercentilEnlistados_DatosNoAgrupados.get() == 1):
        posP = transformarStringAEntero(
            entradaPercentilEnlistados_DatosNoAgrupados.get())

        if(posP < 1 or posP > 99):
            messagebox.showerror("ERROR", "El Percentil va de 1 a 99!")
            check = False
        else:
            texto_extra += f"\n-> El {posP} percentil es {medidaPosicionNA(datosIntEnlistados_DatosNoAgrupados, 3, posP)}"
            check = True

    if(check == True):
        crearVentanaEnlistados_DatosNoAgrupados(texto_extra)
    else:
        if(boolCuartilEnlistados_DatosNoAgrupados.get() == 0 and boolPercentilEnlistados_DatosNoAgrupados.get() == 0 and boolPercentilEnlistados_DatosNoAgrupados.get() == 0):
            messagebox.showerror("ERROR", "Selecciona al menos una medida")


def mostrarCuadroTextoCuartilEnlistados_DatosNoAgrupados():
    textoEntradaCuartilEnlistados_DatosNoAgrupados = Entry(
        frameTablaA1Enlistados_DatosNoAgrupados,
        textvariable=entradaCuartilEnlistados_DatosNoAgrupados,
        width=5
    )

    if(boolCuartilEnlistados_DatosNoAgrupados.get() == 1):
        textoEntradaCuartilEnlistados_DatosNoAgrupados.grid(
            row=5,
            column=2,
            sticky="n"
        )


def mostrarCuadroTextoDecilEnlistados_DatosNoAgrupados():
    textoEntradaDecilEnlistados_DatosNoAgrupados = Entry(
        frameTablaA1Enlistados_DatosNoAgrupados,
        textvariable=entradaDecilEnlistados_DatosNoAgrupados,
        width=5
    )

    if(boolDecilEnlistados_DatosNoAgrupados.get() == 1):
        textoEntradaDecilEnlistados_DatosNoAgrupados.grid(
            row=5,
            column=3,
            sticky="n"
        )


def mostrarCuadroTextoPercentilEnlistados_DatosNoAgrupados():
    textoEntradaPercentilEnlistados_DatosNoAgrupados = Entry(
        frameTablaA1Enlistados_DatosNoAgrupados,
        textvariable=entradaPercentilEnlistados_DatosNoAgrupados,
        width=5
    )

    if(boolPercentilEnlistados_DatosNoAgrupados.get() == 1):
        textoEntradaPercentilEnlistados_DatosNoAgrupados.grid(
            row=5,
            column=4,
            sticky="n"
        )


def crearVentanaEnlistados_DatosNoAgrupados(texto):
    #==================================CREACION VENTANA=====================================#
    ventanaNueva = Toplevel()

    frameNuevaVentana = Frame(ventanaNueva)
    frameNuevaVentana.grab_set()
    frameNuevaVentana.focus_set()
    frameNuevaVentana.pack()

    matriz = unificarNA(datosIntEnlistados_DatosNoAgrupados)

    tablaResultado = Text(
        frameNuevaVentana,
        width=70,
        height=40
    )

    tablaResultado.tag_configure(
        'tag-center', justify='center')
    tablaResultado.insert('end', mostrarResultadosNA(matriz), 'tag-center')

    tablaResultado.insert(END, "\n\n\n")
    tablaResultado.insert(END, texto)

    tablaResultado.grid(
        row=0,
        column=0
    )

    #=======================================BARRA DE SCROLL=================================#

    scrollVert = Scrollbar(
        frameNuevaVentana,
        command=tablaResultado.yview
    )

    scrollVert.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    tablaResultado.insert(
        END, "\n\n(: Desarrollado con amor por Fernando Novillo & Edison Azogue :) \n\t\t\t\t<3")

    tablaResultado.config(
        yscrollcommand=scrollVert.set, state="disabled")


#======================================FUNCIONES DATOS NO AGRUPADOS EN TABLA=======================================#

def tablaLista(valores, frecuencias):
    if(len(datosIntTabla_DatosNoAgrupados) > 0):
        for i in range(len(datosIntTabla_DatosNoAgrupados)):
            datosIntTabla_DatosNoAgrupados.pop()

    for i in range(len(valores)):
        f = transformarStringAEntero(frecuencias[i].get())
        for j in range(f):
            numero = transformarStringAEntero(valores[i].get())
            datosIntTabla_DatosNoAgrupados.append(numero)


def crearCuadrosTextoTabla_DatosAgrupados():
    num = transformarStringAEntero(numValoresTabla_DatosNoAgrupados.get())

    Label(
        frameTablaA2_DatosNoAgrupados,
        text="Valor",
        width=10,
        pady=10,
        font=("Kristen ITC", 11)
    ).grid(
        row=0,
        column=0,
        pady=10,
        padx=5,
        sticky='e'
    )

    Label(
        frameTablaA2_DatosNoAgrupados,
        text="Frecuencia\nAbsoluta",
        width=10,
        pady=10,
        font=("Kristen ITC", 11)
    ).grid(
        row=0,
        column=1,
        pady=10,
        padx=5,
        sticky='w'
    )

    if(len(valoresTabla_DatosNoAgrupados) > 0):
        # Este condicional borra los cuadros generados por el número de clases ingresados
        # Para mostrar el nuevo número según se ingrese
        for i in range(0, len(valoresTabla_DatosNoAgrupados)):
            entradaValoresTabla_DatosNoAgrupados[i].grid_forget()
            entradafITabla_DatosNoAgrupados[i].grid_forget()

        while (len(valoresTabla_DatosNoAgrupados) > 0):
            entradaValoresTabla_DatosNoAgrupados.pop()
            entradafITabla_DatosNoAgrupados.pop()

            valoresTabla_DatosNoAgrupados.pop()
            fITabla_DatosNoAgrupados.pop()

    for i in range(0, num):

        valoresTabla_DatosNoAgrupados.append(StringVar())
        fITabla_DatosNoAgrupados.append(StringVar())

        entradaValoresTabla_DatosNoAgrupados.append(0)
        entradafITabla_DatosNoAgrupados.append(0)

        entradaValoresTabla_DatosNoAgrupados[i] = Entry(
            frameTablaA2_DatosNoAgrupados,
            width=7,
            textvariable=valoresTabla_DatosNoAgrupados[i],
            justify="center",
            bg="#e9e4eb",
            bd=2,
            relief="groove"
        )
        entradaValoresTabla_DatosNoAgrupados[i].grid(
            row=i + 1,
            column=0,
            sticky='w',
            pady=2,
            padx=30
        )

        entradafITabla_DatosNoAgrupados[i] = Entry(
            frameTablaA2_DatosNoAgrupados,
            width=7,
            textvariable=fITabla_DatosNoAgrupados[i],
            justify="center",
            bg="#e9e4eb",
            bd=2,
            relief="groove"
        )
        entradafITabla_DatosNoAgrupados[i].grid(
            row=i + 1,
            column=1,
            sticky='e',
            pady=2,
            padx=30
        )

    botonLlenarTabla_DatosNoAgrupados.grid(
        row=num + 4,
        column=0,
        columnspan=2,
        pady=15
    )

    botonConfirmarCalculosTabla_DatosNoAgrupados.grid_forget()


def comprobarDatosInicioTabla_DatosNoAgrupados():
    try:

        valores = transformarStringAEntero(
            numValoresTabla_DatosNoAgrupados.get())
        valores = int(valores)

        if(valores > 15):
            messagebox.showerror(
                "ERROR", "El número máximo de valores es 15")
        elif(valores <= 0):
            messagebox.showerror(
                "ERROR", "El número de valores no puede ser 0 o menor")
        else:
            crearCuadrosTextoTabla_DatosAgrupados()
    except TypeError:
        pass


def comprobarDatosTabla_DatosNoAgrupados():
    for i in range(transformarStringAEntero(numValoresTabla_DatosNoAgrupados.get())):
        if(fITabla_DatosNoAgrupados[i].get() == ""):
            messagebox.showerror("ERROR", "No debes dejar frecuencias vacías")
            return
        elif(valoresTabla_DatosNoAgrupados[i].get() == ""):
            messagebox.showerror("ERROR", "No debes dejar valores vacíos")
            return
    tablaLista(valoresTabla_DatosNoAgrupados, fITabla_DatosNoAgrupados)
    mostrarBotonesDeOpcionesTabla_DatosNoAgrupados()


def mostrarBotonesDeOpcionesTabla_DatosNoAgrupados():
    Label(
        frameTablaA2_DatosNoAgrupados,
        text="Calcular",
        width=20,
        pady=10,
        font=("Kristen ITC", 11)
    ).grid(
        row=0,
        column=2,
        pady=10,
        padx=5,
        columnspan=3
    )

    botonSeleccionarMediaTabla_DatosNoAgrupados.grid(
        row=1,
        column=2,
        sticky="w"
    )

    botonSeleccionarMedianaTabla_DatosNoAgrupados.grid(
        row=1,
        column=3,
        sticky="w"
    )

    botonSeleccionarModaTabla_DatosNoAgrupados.grid(
        row=1,
        column=4,
        sticky="w"
    )

    botonSeleccionarRangoTabla_DatosNoAgrupados.grid(
        row=2,
        column=2,
        sticky="w"
    )

    botonSeleccionarDesviacionMediaTabla_DatosNoAgrupados.grid(
        row=2,
        column=3,
        sticky="w"
    )

    botonSeleccionarVarianzaTabla_DatosNoAgrupados.grid(
        row=2,
        column=4,
        sticky="w"
    )

    botonSeleccionarDesviacionEstandarTabla_DatosNoAgrupados.grid(
        row=3,
        column=2,
        sticky="w"
    )

    botonSeleccionarSesgoTabla_DatosNoAgrupados.grid(
        row=3,
        column=3,
        sticky="w"
    )

    botonSeleccionarCurtosisTabla_DatosNoAgrupados.grid(
        row=3,
        column=4,
        sticky="w"
    )

    botonSeleccionarCuartilTabla_DatosNoAgrupados.grid(
        row=4,
        column=2,
        sticky="w"
    )

    botonSeleccionarDecilTabla_DatosNoAgrupados.grid(
        row=4,
        column=3,
        sticky="w"
    )

    botonSeleccionarPercentilTabla_DatosNoAgrupados.grid(
        row=4,
        column=4,
        sticky="w"
    )

    botonConfirmarCalculosTabla_DatosNoAgrupados.grid(
        row=8,
        column=2,
        pady=15,
        columnspan=3
    )


def revisarBotonesMedidasTabla_DatosNoAgrupados():
    texto_extra = ""

    check = False

    if(boolMediaTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La media es: {mediaNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolMedianaTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La mediana es {medianaNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolModaTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La moda es: {modaNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolRangoTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> El rango es: {rangoNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolDesviacionMediaTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La desviación media es: {desviacionMediaNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolVarianzaTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La varianza es: {varianzaNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolDesviacionEstandarTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La desviación estándar es: {desviacionEstandarNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolSesgoTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> El sesgo es: {sesgoNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolCurtosisTabla_DatosNoAgrupados.get() == 1):
        texto_extra += f"\n-> La curtosis es: {curtosisNA(datosIntTabla_DatosNoAgrupados)}"
        check = True

    if(boolCuartilTabla_DatosNoAgrupados.get() == 1):
        posC = transformarStringAEntero(
            entradaCuartilTabla_DatosNoAgrupados.get())

        if(posC < 1 or posC > 3):
            messagebox.showerror("ERROR", "El cuartil va de 1 a 3!")
            check = False
        else:
            texto_extra += f"\n-> El {posC} cuartil es {medidaPosicionNA(datosIntTabla_DatosNoAgrupados, 1, posC)}"
            check = True

    if(boolDecilTabla_DatosNoAgrupados.get() == 1):
        posD = transformarStringAEntero(
            entradaDecilTabla_DatosNoAgrupados.get())

        if(posD < 1 or posD > 9):
            messagebox.showerror("ERROR", "El decil va de 1 a 9!")
            check = False
        else:
            texto_extra += f"\n-> El {posD} decil es {medidaPosicionNA(datosIntTabla_DatosNoAgrupados,2, posD)}"
            check = True

    if(boolPercentilTabla_DatosNoAgrupados.get() == 1):
        posP = transformarStringAEntero(
            entradaPercentilTabla_DatosNoAgrupados.get())

        if(posP < 1 or posP > 99):
            messagebox.showerror("ERROR", "El Percentil va de 1 a 99!")
            check = False
        else:
            texto_extra += f"\n-> El {posP} percentil es {medidaPosicionNA(datosIntTabla_DatosNoAgrupados, 3, posP)}"
            check = True

    if(check == True):
        crearVentanaTabla_DatosNoAgrupados(texto_extra)
    else:
        if(boolCuartilTabla_DatosNoAgrupados.get() == 0 and boolPercentilTabla_DatosNoAgrupados.get() == 0 and boolPercentilTabla_DatosNoAgrupados.get() == 0):
            messagebox.showerror("ERROR", "Selecciona al menos una medida")


def mostrarCuadroTextoCuartilTabla_DatosNoAgrupados():
    textoEntradaCuartilTabla_DatosNoAgrupados = Entry(
        frameTablaA2_DatosNoAgrupados,
        textvariable=entradaCuartilTabla_DatosNoAgrupados,
        width=5
    )

    if(boolCuartilTabla_DatosNoAgrupados.get() == 1):
        textoEntradaCuartilTabla_DatosNoAgrupados.grid(
            row=5,
            column=2,
            sticky="n"
        )


def mostrarCuadroTextoDecilTabla_DatosNoAgrupados():
    textoEntradaDecilTabla_DatosNoAgrupados = Entry(
        frameTablaA2_DatosNoAgrupados,
        textvariable=entradaDecilTabla_DatosNoAgrupados,
        width=5
    )

    if(boolDecilTabla_DatosNoAgrupados.get() == 1):
        textoEntradaDecilTabla_DatosNoAgrupados.grid(
            row=5,
            column=3,
            sticky="n"
        )


def mostrarCuadroTextoPercentilTabla_DatosNoAgrupados():
    textoEntradaPercentilTabla_DatosNoAgrupados = Entry(
        frameTablaA2_DatosNoAgrupados,
        textvariable=entradaPercentilTabla_DatosNoAgrupados,
        width=5
    )

    if(boolPercentilTabla_DatosNoAgrupados.get() == 1):
        textoEntradaPercentilTabla_DatosNoAgrupados.grid(
            row=5,
            column=4,
            sticky="n"
        )


def crearVentanaTabla_DatosNoAgrupados(texto):
    #==================================CREACION VENTANA=====================================#
    ventanaNueva = Toplevel()

    frameNuevaVentana = Frame(ventanaNueva)
    frameNuevaVentana.grab_set()
    frameNuevaVentana.focus_set()
    frameNuevaVentana.pack()

    matriz = unificarNA(datosIntTabla_DatosNoAgrupados)

    tablaResultado = Text(
        frameNuevaVentana,
        width=70,
        height=40
    )

    tablaResultado.tag_configure('tag-center', justify='center')
    tablaResultado.insert('end', mostrarResultadosNA(matriz), 'tag-center')

    tablaResultado.insert(END, "\n\n\n")
    tablaResultado.insert(END, texto)

    tablaResultado.grid(
        row=0,
        column=0
    )

    #=======================================BARRA DE SCROLL=================================#

    scrollVert = Scrollbar(
        frameNuevaVentana,
        command=tablaResultado.yview
    )

    scrollVert.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    tablaResultado.insert(
        END, "\n\n(: Desarrollado con amor por Fernando Novillo & Edison Azogue :) \n\t\t\t\t<3")

    tablaResultado.config(yscrollcommand=scrollVert.set, state="disabled")


# ======================================FUNCIONES DISTRIBUCION MEDIA MUESTRAL=======================================#


def comprobarDatosInicio_MediaMuestral():
    datosString_MediaMuestral = entradaDatos_MediaMuestral.get(1.0, 'end')

    for i in range(len(datosString_MediaMuestral)):
        if(datosString_MediaMuestral[i] == ',' and datosString_MediaMuestral[i + 1] == ','):
            messagebox.showerror("ERROR", "INGRESASTE [,] SEGUIDAS")
            return

    global tamanioInt_MediaMuestral
    tamanioInt_MediaMuestral = transformarStringAEntero(
        tamanioString_MediaMuestral.get())

    j = 0

    numero = ""

    while(len(datosInt_MediaMuestral) > 0):
        datosInt_MediaMuestral.pop()

    while(j < len(datosString_MediaMuestral) - 1):
        if(datosString_MediaMuestral[j] != ','):
            while(datosString_MediaMuestral[j] != ',' and j < len(datosString_MediaMuestral) - 1):
                numero += datosString_MediaMuestral[j]
                j += 1
            try:
                entero = int(numero)
                datosInt_MediaMuestral.append(entero)
            except ValueError:
                messagebox.showerror("ERROR", "DEBES INGRESAR NUMEROS")
                j = len(datosString_MediaMuestral)
                return

            numero = ""
        else:
            j += 1

    if(tamanioInt_MediaMuestral > len(datosInt_MediaMuestral)):
        messagebox.showerror(
            "ERROR", "El tamaño de la muestra no puede ser mayor a la muestra")
        return

    if(tamanioInt_MediaMuestral <= 0):
        messagebox.showerror(
            "ERROR", "No se puede tener una muestra 0 o menor")
        return

    crearVentana_MediaMuestral()


def crearVentana_MediaMuestral():
    #==================================CREACION VENTANA=====================================#
    ventanaNueva = Toplevel()

    frameNuevaVentana = Frame(ventanaNueva)
    frameNuevaVentana.grab_set()
    frameNuevaVentana.focus_set()
    frameNuevaVentana.grab_set()
    frameNuevaVentana.focus_set()
    frameNuevaVentana.pack()

    matriz = calcularMuestraMedia(
        datosInt_MediaMuestral, tamanioInt_MediaMuestral)

    tablaResultado = Text(
        frameNuevaVentana,
        width=100,
        height=40
    )

    tablaResultado.tag_configure('tag-center', justify='center')
    tablaResultado.insert(
        'end', mostrarResultadosMuestral(matriz), 'tag-center')

    tablaResultado.insert(END, "\n\n\n")

    tablaResultado.grid(
        row=0,
        column=0
    )

    #=======================================BARRA DE SCROLL=================================#

    scrollVert = Scrollbar(
        frameNuevaVentana,
        command=tablaResultado.yview
    )

    scrollVert.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    tablaResultado.insert(
        END, "\n\n(: Desarrollado con amor por Fernando Novillo & Edison Azogue :) \n\t\t\t\t<3")

    tablaResultado.config(yscrollcommand=scrollVert.set, state="disabled")

# ======================================FUNCIONES CORRELACION=======================================#


def transformarStringAEntero(valor):
    try:
        int(valor)
    except ValueError:
        try:
            float(valor)
            messagebox.showinfo("FUNCIONALIDAD NO IMPLEMENTADA",
                                "Solo se trabaja con números enteros :(")
        except ValueError:
            messagebox.showerror("ERROR", "Debes ingresar números")
        else:
            return
    else:
        return int(valor)


def comprobarDatosInicio_Correlacion():
    datosString_X_Correlacion = entradaDatos_X_Correlacion.get(1.0, 'end')
    datosString_Y_Correlacion = entradaDatos_Y_Correlacion.get(1.0, 'end')

    numDatosX = 0
    numDatosY = 0

    for i in range(len(datosString_X_Correlacion)):
        if(datosString_X_Correlacion[i] == ','):
            numDatosX += 1

    for i in range(len(datosString_Y_Correlacion)):
        if(datosString_Y_Correlacion[i] == ','):
            numDatosY += 1

    if(numDatosX != numDatosY):
        messagebox.showerror(
            "ERROR", "(X) y (Y) deben tener la misma cantidad de datos")
        return

    for i in range(len(datosString_X_Correlacion)):
        if(datosString_X_Correlacion[i] == ',' and datosString_X_Correlacion[i + 1] == ','):
            messagebox.showerror("ERROR", "INGRESASTE [,] SEGUIDAS en (X)")
            return

    for i in range(len(datosString_Y_Correlacion)):
        if(datosString_Y_Correlacion[i] == ',' and datosString_Y_Correlacion[i + 1] == ','):
            messagebox.showerror("ERROR", "INGRESASTE [,] SEGUIDAS en (Y)")
            return

    j = 0
    k = 0

    numeroX = ""
    numeroY = ""

    while(len(datosInt_X_Correlacion) > 0):
        datosInt_X_Correlacion.pop()
        datosInt_Y_Correlacion.pop()

    while(j < len(datosString_X_Correlacion) - 1):
        if(datosString_X_Correlacion[j] != ','):
            while(datosString_X_Correlacion[j] != ',' and j < len(datosString_X_Correlacion) - 1):
                numeroX += datosString_X_Correlacion[j]
                j += 1
            try:
                entero = int(numeroX)
                datosInt_X_Correlacion.append(entero)
            except ValueError:
                messagebox.showerror("ERROR", "DEBES INGRESAR NUMEROS")
                j = len(datosString_X_Correlacion)
                return

            numeroX = ""
        else:
            j += 1

    while(k < len(datosString_Y_Correlacion) - 1):
        if(datosString_Y_Correlacion[k] != ','):
            while(datosString_Y_Correlacion[k] != ',' and k < len(datosString_Y_Correlacion) - 1):
                numeroY += datosString_Y_Correlacion[k]
                k += 1
            try:
                entero = int(numeroY)
                datosInt_Y_Correlacion.append(entero)
            except ValueError:
                messagebox.showerror("ERROR", "DEBES INGRESAR NUMEROS")
                k = len(datosString_Y_Correlacion)
                return

            numeroY = ""
        else:
            k += 1

    crearVentana_Correlacion()


def crearVentana_Correlacion():
    #==================================CREACION VENTANA=====================================#
    ventanaNueva = Toplevel()

    frameNuevaVentana = Frame(ventanaNueva)
    frameNuevaVentana.pack()

    matriz = calcularCorrelacion(
        datosInt_X_Correlacion, datosInt_Y_Correlacion)

    tablaResultado = Text(
        frameNuevaVentana,
        width=150,
        height=40
    )

    tablaResultado.tag_configure('tag-center', justify='center')
    tablaResultado.insert(
        'end', mostrarResultadosCorrelacion(matriz), 'tag-center')

    tablaResultado.insert(END, "\n\n\n")

    tablaResultado.grid(
        row=0,
        column=0
    )

    #=======================================BARRA DE SCROLL=================================#

    scrollVert = Scrollbar(
        frameNuevaVentana,
        command=tablaResultado.yview
    )

    scrollVert.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    r = correlacion(
        matriz[len(datosInt_X_Correlacion)][5],
        matriz[len(datosInt_X_Correlacion)][6],
        matriz[len(datosInt_X_Correlacion)][7],
        len(datosInt_X_Correlacion))

    tablaResultado.insert(
        END, f"\n\nDesviación estándar de X es: {round((matriz[len(datosInt_X_Correlacion)][5] / (len(datosInt_X_Correlacion) - 1))**0.5, 5)}")
    tablaResultado.insert(
        END, f"\nDesviación estándar de Y es: {round((matriz[len(datosInt_Y_Correlacion)][6] / (len(datosInt_Y_Correlacion) - 1))**0.5, 5)}")
    tablaResultado.insert(
        END, f"\n\nEl coeficiente de correlación (r) es: {r}")

    tablaResultado.insert(
        END, "\n\n(: Desarrollado con amor por Fernando Novillo & Edison Azogue :) \n\t\t\t\t<3")

    tablaResultado.config(yscrollcommand=scrollVert.set, state="disabled")


# ================================================FUNCION PRINCIPAL====================================3
def run():
    #====================================CREAR PESTAÑAS GENERALES=====================================#

    bloqueP = Notebook(raizVentana)

    p1 = Frame(bloqueP)
    p2 = Frame(bloqueP)
    p3 = Frame(bloqueP)
    p4 = Frame(bloqueP)
    p5 = Frame(bloqueP)

    bloqueP.add(p1, text="Inicio")
    bloqueP.add(p2, text="Datos No Agrupados")
    bloqueP.add(p3, text="Datos Agrupados")
    bloqueP.add(p4, text="Distribución Media Muestral")
    bloqueP.add(p5, text="Coeficiente de Correlación")

    bloqueP.pack()

    #========================================PESTAÑA PRINCIPAL================================================#
    #lineas separadoras

    canvas = Canvas(p1)
    canvas.create_line(0, 162, 1800, 162, width=2)
    canvas.create_line(0, 2, 1800, 2, width=3)
    canvas.create_line(0, 250, 1800, 250, width=2)
    canvas.create_line(0, 361, 1800, 361, width=2)



    #textos de las medidas
    Label(p1, text ="Medidas descriptivas ", font = "Helvetica 16 bold").place(x=278,y=6)
    Label(p1, text ="Datos no agrupados ", font = "Helvetica 8 bold").place(x=10,y=140)
    Label(p1, text ="Datos  agrupados ", font = "Helvetica 8 bold").place(x=685,y=140)


    Label(p1, text ="Media ", font = "Helvetica 8 bold",fg ="green3").place(x=290,y=40)
    Label(p1, text ="Mediana ", font = "Helvetica 8 bold",fg ="green3").place(x=380,y=40)
    Label(p1, text ="Moda ", font = "Helvetica 8 bold",fg ="green3").place(x=480,y=40)

    Label(p1, text ="Rango ", font = "Helvetica 8 bold",fg ="OrangeRed2").place(x=200,y=80)
    Label(p1, text ="Varianza ", font = "Helvetica 8 bold",fg ="OrangeRed2").place(x=290,y=80)
    Label(p1, text ="Desviación estandar ", font = "Helvetica 8 bold",fg ="OrangeRed2").place(x=380,y=80)
    Label(p1, text ="Desviación media" , font = "Helvetica 8 bold",fg ="OrangeRed2").place(x=530,y=80)

    Label(p1, text ="Cuartiles ", font = "Helvetica 8 bold",fg ="blue").place(x=150,y=120)
    Label(p1, text ="Deciles ", font = "Helvetica 8 bold",fg ="blue").place(x=260,y=120)
    Label(p1, text ="Percentiles ", font = "Helvetica 8 bold",fg ="blue").place(x=370,y=120)
    Label(p1, text ="Sesgo ", font = "Helvetica 8 bold",fg ="blue").place(x=500,y=120)
    Label(p1, text ="Curtosis   ", font = "Helvetica 8 bold",fg ="blue").place(x=610,y=120)



    #textos recuadro 2
    Label(p1, text ="Distribución Muestral de la Media ", font = "Helvetica 16 bold").place(x=214,y=165)


    #textos recuadro 3
    Label(p1, text ="Coeficiente de Correlación", font = "Helvetica 16 bold").place(x=260,y=253)

    #nombres
    Label(p1, text ="Desarrollado por Fernando Novillo & Edison Azogue", font = "Helvetica 7 bold").place(x=5,y=330)


    #====================================CREAR PESTAÑAS DENTRO DE DATOS NO AGRUPADOS=====================================#

    bloqueAgrupados = Notebook(p2)

    a1 = Frame(bloqueAgrupados)
    a2 = Frame(bloqueAgrupados)

    bloqueAgrupados.add(a1, text="LISTADOS")
    bloqueAgrupados.add(a2, text="EN TABLA")
    bloqueAgrupados.pack()

    #===================================CREACION DE FRAMES DATOS NO AGRUPADOS ENlISTADOS==================================#

    global frameSuperiorEnlistadosEnlistados_DatosNoAgrupados
    frameSuperiorEnlistadosEnlistados_DatosNoAgrupados = Frame(a1)
    frameSuperiorEnlistadosEnlistados_DatosNoAgrupados.pack()

    global frameTablaA1Enlistados_DatosNoAgrupados
    frameTablaA1Enlistados_DatosNoAgrupados = Frame(a1)
    frameTablaA1Enlistados_DatosNoAgrupados.pack()

    #===================================CREACION DE FRAMES DATOS NO AGRUPADOS EN TABLA==================================#

    global frameSuperiorTabla_DatosNoAgrupados
    frameSuperiorTabla_DatosNoAgrupados = Frame(a2)
    frameSuperiorTabla_DatosNoAgrupados.pack()

    global frameTablaA2_DatosNoAgrupados
    frameTablaA2_DatosNoAgrupados = Frame(a2)
    frameTablaA2_DatosNoAgrupados.pack()

    #===================================CREACION DE FRAMES DATOS AGRUPADOS==================================#

    global frameSuperior_DatosAgrupados
    frameSuperior_DatosAgrupados = Frame(p3)
    frameSuperior_DatosAgrupados.pack()

    global frameTabla_DatosAgrupados
    frameTabla_DatosAgrupados = Frame(p3)
    frameTabla_DatosAgrupados.pack()

    #===================================CREACION DE FRAMES MEDIA MUESTRAL==================================#

    global frameSuperior_MediaMuestral
    frameSuperior_MediaMuestral = Frame(p4)
    frameSuperior_MediaMuestral.pack()

    #===================================CREACION DE FRAMES CORRELACION==================================#

    global frameSuperior_Correlacion
    frameSuperior_Correlacion = Frame(p5)
    frameSuperior_Correlacion.pack()

    #=================================LABELS (SOLO ES TEXTO) DATOS NO AGRUPADOS LISTADOS================================#

    Label(
        frameSuperiorEnlistadosEnlistados_DatosNoAgrupados,
        text="CALCULADORA ESTADISTICA DE DATOS NO AGRUPADOS",
        padx=10,
        pady=10,
        font=("Comic Sans MS", 20)
    ).grid(
        row=0,
        column=0,)

    Label(
        frameSuperiorEnlistadosEnlistados_DatosNoAgrupados,
        text="PARA DATOS ENLISTADOS\nIngresa los datos separados solo por [,]",
        width=60,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=0)

    #=================================LABELS (SOLO ES TEXTO) DATOS NO AGRUPADOS EN TABLA================================#

    Label(
        frameSuperiorTabla_DatosNoAgrupados,
        text="CALCULADORA ESTADISTICA DE DATOS NO AGRUPADOS",
        padx=10,
        pady=10,
        font=("Comic Sans MS", 20)
    ).grid(
        row=0,
        column=0,
        columnspan=2)

    Label(
        frameSuperiorTabla_DatosNoAgrupados,
        text="PARA DATOS EN TABLA",
        width=60,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=0,
        pady=10,
        columnspan=2)

    Label(
        frameSuperiorTabla_DatosNoAgrupados,
        text="Número de valores distintos",
        width=25,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=2,
        column=0,
        columnspan=2)

    #=================================LABELS (SOLO ES TEXTO) DATOS AGRUPADOS================================#

    Label(
        frameSuperior_DatosAgrupados,
        text="CALCULADORA ESTADISTICA DE DATOS AGRUPADOS",
        padx=10,
        pady=10,
        font=("Comic Sans MS", 20)
    ).grid(
        row=0,
        column=0,
        columnspan=3)

    Label(
        frameSuperior_DatosAgrupados,
        text="Límite Inferior (Clase 1)",
        width=25,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=0)

    Label(
        frameSuperior_DatosAgrupados,
        text="Límite Superior (Clase 1)",
        width=25,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=1)

    Label(
        frameSuperior_DatosAgrupados,
        text="Número de clases",
        width=25,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=2)

    #=================================LABELS (SOLO ES TEXTO) MEDIA MUESTRAL================================#

    Label(
        frameSuperior_MediaMuestral,
        text="CALCULADORA DISTRIBUCION MUESTRAL DE LA MEDIA",
        padx=10,
        pady=10,
        font=("Comic Sans MS", 20)
    ).grid(
        row=0,
        column=0,)

    Label(
        frameSuperior_MediaMuestral,
        text="Ingresa los datos de la muestra separados solo por [,]",
        width=60,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=0)

    Label(
        frameSuperior_MediaMuestral,
        text="Ingresa el tamaño de la muestra",
        width=60,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=3,
        column=0)

    #=================================LABELS (SOLO ES TEXTO) CORRELACION================================#

    Label(
        frameSuperior_Correlacion,
        text="CALCULADORA COEFICIENTE DE CORRELACION",
        padx=10,
        pady=10,
        font=("Comic Sans MS", 20)
    ).grid(
        row=0,
        column=0,
        columnspan=3)

    Label(
        frameSuperior_Correlacion,
        text="Ingresa los datos de la variable (X) separados por [,]",
        width=40,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=0)

    Label(
        frameSuperior_Correlacion,
        text="Ingresa los datos de la variable (Y) separados por [,]",
        width=40,
        anchor="n",
        font=("Kristen ITC", 11)
    ).grid(
        row=1,
        column=1)

    #=====================================TEXT (INGRESO DE TEXTO) DATOS NO AGRUPADOS=========================#

    global entradaDatosEnlistados_DatosNoAgrupados

    entradaDatosEnlistados_DatosNoAgrupados = Text(
        frameSuperiorEnlistadosEnlistados_DatosNoAgrupados,
        width=40,
        height=10
    )

    entradaDatosEnlistados_DatosNoAgrupados.grid(
        pady=5,
        row=2,
        column=0
    )

    #=====================================TEXT MEDIA MUESTRAL (INGRESO DE TEXTO)=========================#

    global entradaDatos_MediaMuestral

    entradaDatos_MediaMuestral = Text(
        frameSuperior_MediaMuestral,
        width=40,
        height=10
    )

    entradaDatos_MediaMuestral.grid(
        pady=5,
        row=2,
        column=0
    )

    #=====================================TEXT (INGRESO DE TEXTO) CORRELACION=========================#

    global entradaDatos_X_Correlacion

    entradaDatos_X_Correlacion = Text(
        frameSuperior_Correlacion,
        width=30,
        height=8
    )

    entradaDatos_X_Correlacion.grid(
        pady=5,
        row=2,
        column=0
    )

    global entradaDatos_Y_Correlacion

    entradaDatos_Y_Correlacion = Text(
        frameSuperior_Correlacion,
        width=30,
        height=8
    )

    entradaDatos_Y_Correlacion.grid(
        pady=5,
        row=2,
        column=1
    )

    #=====================================ENTRYS (INGRESO DE TEXTO) DATOS AGRUPADOS EN LISTA=========================#

    Entry(
        # Se ingresa el límite inferior
        frameSuperior_DatosAgrupados,
        textvariable=inicioLI_DatosAgrupados,
        width=7,
        justify="center",
        bg="#e9e4eb",
        bd=2,
        relief="groove"
    ).grid(
        row=2,
        column=0,
        pady=10
    )

    Entry(
        # Se ingresa el límite superior
        frameSuperior_DatosAgrupados,
        width=7,
        textvariable=iniciolS_DatosAgrupados,
        justify="center",
        bg="#e9e4eb",
        bd=2,
        relief="groove"
    ).grid(
        row=2,
        column=1,
        pady=10
    )

    Entry(
        # Se ingresa el número de clases
        frameSuperior_DatosAgrupados,
        width=7,
        textvariable=numClases_DatosAgrupados,
        justify="center",
        bg="#e9e4eb",
        bd=2,
        relief="groove"
    ).grid(
        row=2,
        column=2,
        pady=10
    )

    #========================================ENTRYS (INGRESO DE TEXTO) DATOS NO AGRUPADOS EN TABLA=======================================#

    Entry(
        # Se ingresa el número de clases
        frameSuperiorTabla_DatosNoAgrupados,
        width=7,
        textvariable=numValoresTabla_DatosNoAgrupados,
        justify="center",
        bg="#e9e4eb",
        bd=2,
        relief="groove"
    ).grid(
        row=3,
        column=0,
        pady=10,
        columnspan=2
    )

    #=====================================ENTRYS (INGRESO DE TEXTO) MEDIA MUESTRAL=========================#

    global entradaTamanioMuestra

    entradaTamanioMuestra = Entry(
        frameSuperior_MediaMuestral,
        width=10,
        justify="center",
        textvariable=tamanioString_MediaMuestral
    )

    entradaTamanioMuestra.grid(
        pady=5,
        row=4,
        column=0
    )

    #========================================BOTONES DATOS NO AGRUPADOS ENLISTADOS=======================================#

    Button(
        frameSuperiorEnlistadosEnlistados_DatosNoAgrupados,
        text="CONFIRMAR DATOS",
        command=lambda: comprobarDatosInicioEnlistados_DatosNoAgrupados(),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    ).grid(
        row=3,
        column=0,
        columnspan=3
    )

    global botonConfirmarCalculosEnlistados_DatosNoAgrupados
    botonConfirmarCalculosEnlistados_DatosNoAgrupados = Button(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="CALCULAR",
        activebackground="#e8ca1e",
        command=lambda: revisarBotonesMedidasEnlistados_DatosNoAgrupados(),
        relief="ridge",
        bd=3
    )

    #========================================BOTONES DATOS NO AGRUPADOS EN TABLA=======================================#

    Button(
        frameSuperiorTabla_DatosNoAgrupados,
        text="CONFIRMAR DATOS",
        command=lambda: comprobarDatosInicioTabla_DatosNoAgrupados(),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    ).grid(
        row=4,
        column=0,
        columnspan=2
    )

    global botonLlenarTabla_DatosNoAgrupados
    botonLlenarTabla_DatosNoAgrupados = Button(
        frameTablaA2_DatosNoAgrupados,
        text="CONFIRMAR FRECUENCIAS",
        command=lambda: comprobarDatosTabla_DatosNoAgrupados(),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    )

    global botonConfirmarCalculosTabla_DatosNoAgrupados
    botonConfirmarCalculosTabla_DatosNoAgrupados = Button(
        frameTablaA2_DatosNoAgrupados,
        text="CALCULAR",
        activebackground="#e8ca1e",
        command=lambda: revisarBotonesMedidasTabla_DatosNoAgrupados(),
        relief="ridge",
        bd=3
    )

    #========================================BOTONES MEDIA MUESTRAL=======================================#

    Button(
        frameSuperior_MediaMuestral,
        text="CALCULAR",
        command=lambda: comprobarDatosInicio_MediaMuestral(),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    ).grid(
        row=5,
        column=0,
        columnspan=3
    )

    #========================================BOTONES CORRELACION=======================================#

    Button(
        frameSuperior_Correlacion,
        text="CALCULAR",
        command=lambda: comprobarDatosInicio_Correlacion(),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    ).grid(
        row=3,
        pady=5,
        column=0,
        columnspan=2
    )

    # ==========================================CHECK BUTTONS DATOS NO AGRUPADOS ENLISTADOS=======================

    global botonSeleccionarMediaEnlistados_DatosNoAgrupados
    botonSeleccionarMediaEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Media",
        variable=boolMediaEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarMedianaEnlistados_DatosNoAgrupados
    botonSeleccionarMedianaEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Mediana",
        variable=boolMedianaEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarModaEnlistados_DatosNoAgrupados
    botonSeleccionarModaEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Moda",
        variable=boolModaEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarRangoEnlistados_DatosNoAgrupados
    botonSeleccionarRangoEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Rango",
        variable=boolRangoEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarDesviacionMediaEnlistados_DatosNoAgrupados
    botonSeleccionarDesviacionMediaEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Desviacion Media",
        variable=boolDesviacionMediaEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarVarianzaEnlistados_DatosNoAgrupados
    botonSeleccionarVarianzaEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Varianza",
        variable=boolVarianzaEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarDesviacionEstandarEnlistados_DatosNoAgrupados
    botonSeleccionarDesviacionEstandarEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Desviacion Estandar",
        variable=boolDesviacionEstandarEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarSesgoEnlistados_DatosNoAgrupados
    botonSeleccionarSesgoEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Sesgo",
        variable=boolSesgoEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarCurtosisEnlistados_DatosNoAgrupados
    botonSeleccionarCurtosisEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Curtosis",
        variable=boolCurtosisEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarCuartilEnlistados_DatosNoAgrupados
    botonSeleccionarCuartilEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Cuartil",
        variable=boolCuartilEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoCuartilEnlistados_DatosNoAgrupados()
    )

    global botonSeleccionarDecilEnlistados_DatosNoAgrupados
    botonSeleccionarDecilEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Decil",
        variable=boolDecilEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoDecilEnlistados_DatosNoAgrupados()
    )

    global botonSeleccionarPercentilEnlistados_DatosNoAgrupados
    botonSeleccionarPercentilEnlistados_DatosNoAgrupados = Checkbutton(
        frameTablaA1Enlistados_DatosNoAgrupados,
        text="Percentil",
        variable=boolPercentilEnlistados_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoPercentilEnlistados_DatosNoAgrupados()
    )

    # ==========================================CHECK BUTTONS DATOS NO AGRUPADOS EN TABLA=======================

    global botonSeleccionarMediaTabla_DatosNoAgrupados
    botonSeleccionarMediaTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Media",
        variable=boolMediaTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarMedianaTabla_DatosNoAgrupados
    botonSeleccionarMedianaTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Mediana",
        variable=boolMedianaTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarModaTabla_DatosNoAgrupados
    botonSeleccionarModaTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Moda",
        variable=boolModaTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarRangoTabla_DatosNoAgrupados
    botonSeleccionarRangoTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Rango",
        variable=boolRangoTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarDesviacionMediaTabla_DatosNoAgrupados
    botonSeleccionarDesviacionMediaTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Desviacion Media",
        variable=boolDesviacionMediaTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarVarianzaTabla_DatosNoAgrupados
    botonSeleccionarVarianzaTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Varianza",
        variable=boolVarianzaTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarDesviacionEstandarTabla_DatosNoAgrupados
    botonSeleccionarDesviacionEstandarTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Desviacion Estandar",
        variable=boolDesviacionEstandarTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarSesgoTabla_DatosNoAgrupados
    botonSeleccionarSesgoTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Sesgo",
        variable=boolSesgoTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarCurtosisTabla_DatosNoAgrupados
    botonSeleccionarCurtosisTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Curtosis",
        variable=boolCurtosisTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarCuartilTabla_DatosNoAgrupados
    botonSeleccionarCuartilTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Cuartil",
        variable=boolCuartilTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoCuartilTabla_DatosNoAgrupados()
    )

    global botonSeleccionarDecilTabla_DatosNoAgrupados
    botonSeleccionarDecilTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Decil",
        variable=boolDecilTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoDecilTabla_DatosNoAgrupados()
    )

    global botonSeleccionarPercentilTabla_DatosNoAgrupados
    botonSeleccionarPercentilTabla_DatosNoAgrupados = Checkbutton(
        frameTablaA2_DatosNoAgrupados,
        text="Percentil",
        variable=boolPercentilTabla_DatosNoAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoPercentilTabla_DatosNoAgrupados()
    )

    # ========================================BOTONES DATOS AGRUPADOs=======================================#

    Button(
        frameSuperior_DatosAgrupados,
        text="ACTUALIZAR CLASES",
        command=lambda: comprobarDatosInicio_DatosAgrupados(
            inicioLI_DatosAgrupados.get(), iniciolS_DatosAgrupados.get()),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    ).grid(
        row=3,
        column=0,
        columnspan=3
    )

    global botonLlenarTabla_DatosAgrupados
    botonLlenarTabla_DatosAgrupados = Button(
        frameTabla_DatosAgrupados,
        text="CONFIRMAR FRECUENCIAS",
        command=lambda: comprobarDatosFrecuencia(1),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    )

    global botonConfirmarCalculos_DatosAgrupados
    botonConfirmarCalculos_DatosAgrupados = Button(
        frameTabla_DatosAgrupados,
        text="CALCULAR",
        command=lambda: comprobarDatosFrecuencia(2),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    )

    # ==========================================CHECK BUTTONS DATOS AGRUPADOs=======================

    global botonSeleccionarMedia_DatosAgrupados
    botonSeleccionarMedia_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Media",
        variable=boolMedia_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarMediana_DatosAgrupados
    botonSeleccionarMediana_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Mediana",
        variable=boolMediana_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarModa_DatosAgrupados
    botonSeleccionarModa_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Moda",
        variable=boolModa_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarRango_DatosAgrupados
    botonSeleccionarRango_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Rango",
        variable=boolRango_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarDesviacionMedia_DatosAgrupados
    botonSeleccionarDesviacionMedia_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Desviacion Media",
        variable=boolDesviacionMedia_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarVarianza_DatosAgrupados
    botonSeleccionarVarianza_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Varianza",
        variable=boolVarianza_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarDesviacionEstandar_DatosAgrupados
    botonSeleccionarDesviacionEstandar_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Desviacion Estandar",
        variable=boolDesviacionEstandar_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarSesgo_DatosAgrupados
    botonSeleccionarSesgo_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Sesgo",
        variable=boolSesgo_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarCurtosis_DatosAgrupados
    botonSeleccionarCurtosis_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Curtosis",
        variable=boolCurtosis_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarCuartil_DatosAgrupados
    botonSeleccionarCuartil_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Cuartil",
        variable=boolCuartil_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoCuartil_DatosAgrupados()
    )

    global botonSeleccionarDecil_DatosAgrupados
    botonSeleccionarDecil_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Decil",
        variable=boolDecil_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoDecil_DatosAgrupados()
    )

    global botonSeleccionarPercentil_DatosAgrupados
    botonSeleccionarPercentil_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Percentil",
        variable=boolPercentil_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9),
        command=lambda: mostrarCuadroTextoPercentil_DatosAgrupados()
    )

    global botonSeleccionarHistograma_DatosAgrupados
    botonSeleccionarHistograma_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Histograma",
        variable= boolHistograma_DatosAgrupados,
        cursor="heart",
        font=("Kristen ITC", 9)
    )


    #=======================================CICLO INFINITO==================================#

    raizVentana.mainloop()


if __name__ == '__main__':
    run()
