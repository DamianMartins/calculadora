import tkinter as tk 
from tkinter import messagebox
import sys

#################################################
def convertir(dato):
    try:
        dato=int (dato)
        return dato
    except ValueError:
        try:
            dato=float(dato)
            return dato
        except ValueError:
            dato="error"
            return dato


def sumar():
    cTres.delete(0,tk.END)
    a=cUno.get()
    a=convertir(a)
    b=cDos.get()
    b=convertir(b)
    if a!="error" and b!="error":
        c=a+b
        cTres.insert(0,c)
    else:
        messagebox.showerror(title="Error!",message="Error de datos")
        cTres.insert(0,"error")


def restar():
    cTres.delete(0,tk.END)
    a=cUno.get()
    a=convertir(a)
    b=cDos.get()
    b=convertir(b)
    if a!="error" and b!="error":
        c=a-b
        cTres.insert(0,c)
    else:
        messagebox.showerror(title="Error!",message="Error de datos")
        cTres.insert(0,"error")


def multiplicar():
    cTres.delete(0,tk.END)
    a=cUno.get()
    a=convertir(a)
    b=cDos.get()
    b=convertir(b)
    if a!="error" and b!="error":
        c=a*b
        cTres.insert(0,c)
    else:
        messagebox.showerror(title="Error!",message="Error de datos")
        cTres.insert(0,"error")


def dividir():
    cTres.delete(0,tk.END)
    a=cUno.get()
    a=convertir(a)
    b=cDos.get()
    b=convertir(b)
    if a!="error" and b!="error" and b!=0 and a!=0:
        c=a/b
        cTres.insert(0,c)
    else:
        messagebox.showerror(title="Error!",message="Data error")
        cTres.insert(0,"error")


def pedir_info():
    messagebox.showerror(title="Information",message="myCalculadora: 01/04/2021")

def salir():
    respuesta=messagebox.askyesno(title="Question",message="Do you want to exit?")
    if respuesta:
        sys.exit()






##################################################

ventana=tk.Tk()
ventana.config(width=300,height=300)
ventana.title("myCalculadora")
cUno=tk.Entry()
cUno.place(x=20,y=60)

cDos=tk.Entry()
cDos.place(x=160,y=60)

bSuma=tk.Button(text=" + ",command=sumar)
bSuma.place(x=20,y=120)

bResta=tk.Button(text=" - ",command=restar)
bResta.place(x=100,y=120)

bMultiplicacion=tk.Button(text=" x ",command=multiplicar)
bMultiplicacion.place(x=170,y=120)

bDivision=tk.Button(text=" % ",command=dividir)
bDivision.place(x=240,y=120)

cTres=tk.Entry()
cTres.place(x=90,y=200)

bSalir=tk.Button(text="Salir",command=salir)
bSalir.place(x=200,y=250,width=80,height=40)

bInfo=tk.Button(text="Info",command=pedir_info)
bInfo.place(x=30,y=250,width=80,height=40)

eUno=tk.Label(text="Dato uno")
eUno.place(x=20,y=30)

eDos=tk.Label(text="Dato dos")
eDos.place(x=160,y=30)

resultado=tk.Label(text="Resultado")
resultado.place(x=90,y=170)



ventana.mainloop()




