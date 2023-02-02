from tkinter import *

root=Tk()

var_opcion=IntVar()

def imprimir():
    #print(var_opcion.get())
    if var_opcion.get()==1:
        etiqueta.config(text='Has elegido masculino')
    elif var_opcion.get()==2:
        etiqueta.config(text='Has elegido femenino')
    else:
        etiqueta.config(text='Has elegido otros')

Label(root, text='Género:').pack()

Radiobutton(root, text='Masculino', variable=var_opcion, value=1, command=imprimir).pack()
Radiobutton(root, text='Femenino', variable=var_opcion, value=2, command=imprimir).pack()
Radiobutton(root, text='Otros', variable=var_opcion, value=3, command=imprimir).pack()


etiqueta=Label(root)
etiqueta.pack()


root.mainloop()