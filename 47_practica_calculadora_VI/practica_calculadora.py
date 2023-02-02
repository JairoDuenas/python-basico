from tkinter import *

root=Tk()

mi_frame=Frame(root)
mi_frame.pack()

operacion=''
resultado=0

reset_pantalla=False

# pantalla -------------------------------------

numero_pantalla=StringVar()

pantalla=Entry(mi_frame, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background='black', fg='#03f943', justify='right')

# pulsaciones teclado --------------------------
def numero_pulsado(numero):
    global operacion
    global reset_pantalla

    if reset_pantalla != False:
        numero_pantalla.set(numero)
        reset_pantalla=False
    else:
        numero_pantalla.set(numero_pantalla.get() + numero)

# función suma ---------------------------------

def suma(numero):
    global operacion
    global resultado
    global reset_pantalla

    resultado += int(numero)
    operacion='suma'
    reset_pantalla=True
    numero_pantalla.set(resultado)

# función el_resultado ---------------------------------
def el_resultado():
    global resultado
    numero_pantalla.set(resultado+int(numero_pantalla.get()))
    resultado=0

# fila 1 ----------------------------------------
boton_7=Button(mi_frame, text='7', width=3, command=lambda:numero_pulsado('7'))
boton_7.grid(row=2, column=1)

boton_8=Button(mi_frame, text='8', width=3, command=lambda:numero_pulsado('8'))
boton_8.grid(row=2, column=2)

boton_9=Button(mi_frame, text='9', width=3, command=lambda:numero_pulsado('9'))
boton_9.grid(row=2, column=3)

boton_dividir=Button(mi_frame, text='/', width=3)
boton_dividir.grid(row=2, column=4)

# fila 2 ----------------------------------------
boton_4=Button(mi_frame, text='4', width=3, command=lambda:numero_pulsado('4'))
boton_4.grid(row=3, column=1)

boton_5=Button(mi_frame, text='5', width=3, command=lambda:numero_pulsado('5'))
boton_5.grid(row=3, column=2)

boton_6=Button(mi_frame, text='6', width=3, command=lambda:numero_pulsado('6'))
boton_6.grid(row=3, column=3)

boton_multiplicar=Button(mi_frame, text='x', width=3)
boton_multiplicar.grid(row=3, column=4)

# fila 3 ----------------------------------------
boton_1=Button(mi_frame, text='1', width=3, command=lambda:numero_pulsado('1'))
boton_1.grid(row=4, column=1)

boton_2=Button(mi_frame, text='2', width=3, command=lambda:numero_pulsado('2'))
boton_2.grid(row=4, column=2)

boton_3=Button(mi_frame, text='3', width=3, command=lambda:numero_pulsado('3'))
boton_3.grid(row=4, column=3)

boton_restar=Button(mi_frame, text='-', width=3)
boton_restar.grid(row=4, column=4)

# fila 4 ----------------------------------------
boton_0=Button(mi_frame, text='0', width=3, command=lambda:numero_pulsado('0'))
boton_0.grid(row=5, column=1)

boton_coma=Button(mi_frame, text=',', width=3, command=lambda:numero_pulsado(','))
boton_coma.grid(row=5, column=2)

boton_igual=Button(mi_frame, text='=', width=3, command=lambda:el_resultado())
boton_igual.grid(row=5, column=3)

boton_suma=Button(mi_frame, text='+', width=3, command=lambda:suma(numero_pantalla.get()))
boton_suma.grid(row=5, column=4)

root.mainloop()