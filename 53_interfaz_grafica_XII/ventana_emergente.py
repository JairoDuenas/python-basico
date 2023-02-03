from tkinter import *

root=Tk()

barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

archivo_menu=Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label='Nuevo')
archivo_menu.add_command(label='Guardar')
archivo_menu.add_command(label='Guardar como')
archivo_menu.add_separator()
archivo_menu.add_command(label='Cerrar')
archivo_menu.add_command(label='Salir')

archivo_edicion=Menu(barra_menu, tearoff=0)
archivo_edicion.add_command(label='Copiar')
archivo_edicion.add_command(label='Cortar')
archivo_edicion.add_command(label='Pegar')

archivo_herramientas=Menu(barra_menu, tearoff=0)
archivo_herramientas.add_command(label='Avanzadas')

archivo_ayuda=Menu(barra_menu, tearoff=0)
archivo_ayuda.add_command(label='Licencia')
archivo_ayuda.add_command(label='Acerca de...')

barra_menu.add_cascade(label='Archivo', menu=archivo_menu)
barra_menu.add_cascade(label='Edición', menu=archivo_edicion)
barra_menu.add_cascade(label='Herramientas', menu=archivo_herramientas)
barra_menu.add_cascade(label='Ayuda', menu=archivo_ayuda)

root.mainloop()