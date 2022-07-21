from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
from pygal import Histogram
from pygal.style import Style

from funcionesEstadisticasAgrupados import *
from funcionesNuevaVentanaAgrupados import *

import numpy as np

# ================================VARIABLES GLOBALES====================================#
global raiz_DatosAgrupados
raiz_DatosAgrupados = Tk()
raiz_DatosAgrupados.title("ESTADISTICA")

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

# ======================================Funciones=======================================#


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
        fAc_DatosAgrupados.append(0)

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
            pady=2,
            font=("Kristen ITC", 11))
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


def calcularLimiteSuperior(inferior):
    rango = transformarStringAEntero(
        iniciolS_DatosAgrupados.get()) - transformarStringAEntero(inicioLI_DatosAgrupados.get())
    suma = transformarStringAEntero(inferior) + rango
    suma = str(suma)

    a = StringVar(value=suma)

    return a


def comprobarDatosFrecuencia():
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
        mostrarDatos_DatosAgrupados()


def mostrarDatos_DatosAgrupados():

    mostrarBotonesDeOpciones_DatosAgrupados()

    #num = transformarStringAEntero(numClases_DatosAgrupados.get())

    calcularFrecuenciaAcumulada()
    calcularMarcaClase()

    """for i in range(0, num):

        print(
            f"En  {i + 1} --- lI_DatosAgrupados = {lI_DatosAgrupados[i].get()}",
            f"- lS_DatosAgrupados = {lS_DatosAgrupados[i].get()}",
            f"- fI_DatosAgrupados = {fI_DatosAgrupados[i].get()}",
            f"- FI_DatosAgrupados = {fAc_DatosAgrupados[i]}",
            f"- mC_DatosAgrupados = {mC_DatosAgrupados[i]}")"""


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
        row=5,
        column=2,
        sticky="w"
    )

    
    botonConfirmarCalculos_DatosAgrupados.grid(
        row=transformarStringAEntero(numClases_DatosAgrupados.get()) + 5,
        column=2,
        pady=15,
        columnspan=3
    )


def calcularFrecuenciaAcumulada():
    fAc_DatosAgrupados[0] = transformarStringAEntero(
        fI_DatosAgrupados[0].get())

    for i in range(1, transformarStringAEntero(numClases_DatosAgrupados.get())):

        anterior = fAc_DatosAgrupados[i - 1]
        """print(type(anterior))"""

        actual = fI_DatosAgrupados[i].get()
        actual = int(actual)

        suma = anterior + actual

        fAc_DatosAgrupados[i] = suma


def calcularMarcaClase():
    for i in range(transformarStringAEntero(numClases_DatosAgrupados.get())):
        limI = transformarStringAEntero(lI_DatosAgrupados[i].get())
        limS = transformarStringAEntero(lS_DatosAgrupados[i].get())
        mC_DatosAgrupados.append((limI + limS) / 2)
        """print(f"en calcularMarcaClase ---- i vale {i} ----- ")"""


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
        """print(type(posC))"""

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
        texto_extra += f"\n-> El Histograma es: {crearHistograma_DatosAgrupados()}"
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

    estilo = Style(colors=['#F2AB6D']) # creamos un estilo para darle color a las barras

    # creamos el histograma y añadimos los datos
    histograma = Histogram(title='Histograma\nDesarrollado por Fernando Novillo & Edison Azogue',
                        x_title='intervalos', 
                        y_title='frecuencias', 
                        style=estilo)

    histograma.add('frecuencias', datos)

    histograma.render_in_browser();


def crearVentana_DatosAgrupados(texto):
    #==================================CREACION VENTANA=====================================#
    num = transformarStringAEntero(numClases_DatosAgrupados.get())
    ventanaNueva = Toplevel()

    ventanaNueva.title("Tabla de Frecuencias")

    frameNuevaVentana = Frame(ventanaNueva)
    frameNuevaVentana.grab_set()
    frameNuevaVentana.focus_set()
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
        END, "\n\nDesarrollado con amor por Fernando Novillo & Edison Azoqgue")

    tablaResultado.config(yscrollcommand=scrollVert.set, state="disabled")


def run():
    #====================================Crear Pestañas=====================================#

    bloqueP = Notebook(raiz_DatosAgrupados)

    p1 = Frame(bloqueP)
    p2 = Frame(bloqueP)
    p3 = Frame(bloqueP)

    bloqueP.add(p1, text="Inicio")
    bloqueP.add(p2, text="Datos No Agrupados")
    bloqueP.add(p3, text="Datos Agrupados")

    bloqueP.pack()

    #===================================CREACION DE FRAMES==================================#

    global frameSuperior_DatosAgrupados
    frameSuperior_DatosAgrupados = Frame(p3)
    frameSuperior_DatosAgrupados.pack()

    global frameTabla_DatosAgrupados
    frameTabla_DatosAgrupados = Frame(p3)
    frameTabla_DatosAgrupados.pack()

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

    #=====================================ENTRYS (INGRESO DE TEXTO) DATOS AGRUPADOS=========================#

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

    # ========================================BOTONES DATOSA AGRUPADOs=======================================#

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
        command=lambda: comprobarDatosFrecuencia(),
        activebackground="#e8ca1e",
        relief="ridge",
        bd=3
    )

    global botonConfirmarCalculos_DatosAgrupados
    botonConfirmarCalculos_DatosAgrupados = Button(
        frameTabla_DatosAgrupados,
        text="CALCULAR",
        command=lambda: revisarBotonesMedidas_DatosAgrupados(),
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
        command=lambda: mostrarCuadroTextoCuartil_DatosAgrupados(),
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarDecil_DatosAgrupados
    botonSeleccionarDecil_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Decil",
        variable=boolDecil_DatosAgrupados,
        cursor="heart",
        command=lambda: mostrarCuadroTextoDecil_DatosAgrupados(),
        font=("Kristen ITC", 9)
    )

    global botonSeleccionarPercentil_DatosAgrupados
    botonSeleccionarPercentil_DatosAgrupados = Checkbutton(
        frameTabla_DatosAgrupados,
        text="Percentil",
        variable=boolPercentil_DatosAgrupados,
        cursor="heart",
        command=lambda: mostrarCuadroTextoPercentil_DatosAgrupados(),
        font=("Kristen ITC", 9)
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

    raiz_DatosAgrupados.mainloop()


if __name__ == '__main__':
    run()
