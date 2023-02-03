from tkinter import *
from tkinter import messagebox

root=Tk()

def info_Adicional():
    messagebox.showinfo('Procesador de Jairo', 'Procesador de textos 2023')

def aviso_licencia():
    messagebox.showwarning('Licencia', 'Producto bajo licencia GNU')

def salir_aplicación():
    #valor=messagebox.askquestion('Salir', 'Salir de la aplicación')
    """ if valor=='yes':
        root.destroy() """

    valor=messagebox.askokcancel('Salir', '¿Desea salir de la aplicación?')
    if valor==True:
        root.destroy()

def cerrar_documento():
    valor=messagebox.askretrycancel('Reintentar', 'No es posible cerrar documento. Documento bloqueado')
    if valor==False:
        root.destroy()


barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

archivo_menu=Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label='Nuevo')
archivo_menu.add_command(label='Guardar')
archivo_menu.add_command(label='Guardar como')
archivo_menu.add_separator()
archivo_menu.add_command(label='Cerrar', command=cerrar_documento)
archivo_menu.add_command(label='Salir', command=salir_aplicación)

archivo_edicion=Menu(barra_menu, tearoff=0)
archivo_edicion.add_command(label='Copiar')
archivo_edicion.add_command(label='Cortar')
archivo_edicion.add_command(label='Pegar')

archivo_herramientas=Menu(barra_menu, tearoff=0)
archivo_herramientas.add_command(label='Avanzadas')

archivo_ayuda=Menu(barra_menu, tearoff=0)
archivo_ayuda.add_command(label='Licencia', command=aviso_licencia)
archivo_ayuda.add_command(label='Acerca de...', command=info_Adicional)

barra_menu.add_cascade(label='Archivo', menu=archivo_menu)
barra_menu.add_cascade(label='Edición', menu=archivo_edicion)
barra_menu.add_cascade(label='Herramientas', menu=archivo_herramientas)
barra_menu.add_cascade(label='Ayuda', menu=archivo_ayuda)

root.mainloop()