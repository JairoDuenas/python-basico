from tkinter import *

root=Tk()

root.title('Ejemplo')

playa=IntVar()
montagna=IntVar()
turismo_rural=IntVar()

def opciones_viaje():
    opcion_escondida=''

    if (playa.get()==1):
        opcion_escondida+='Playa'
    if (montagna.get()==1):
        opcion_escondida+='Montaña'
    if (turismo_rural.get()==1):
        opcion_escondida+='Turismo rural'

    texto_Final.config(text=opcion_escondida)

foto=PhotoImage(file='/Users/jhonjairoduenasvega/logo/logo.png')
Label(root, image=foto, width=200, height=200).pack()


frame=Frame(root)
frame.pack()

Label(frame, text='Elige destinos', width=50).pack()

Checkbutton(frame, text='Playa', variable=playa, onvalue=1, offvalue=0, command=opciones_viaje).pack()
Checkbutton(frame, text='Montaña', variable=montagna, onvalue=1, offvalue=0, command=opciones_viaje).pack()
Checkbutton(frame, text='Turismo rural', variable=turismo_rural, onvalue=1, offvalue=0, command=opciones_viaje).pack()

texto_Final=Label(frame)
texto_Final.pack()

root.mainloop()