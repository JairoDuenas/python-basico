from tkinter import *

root=Tk()

barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

# ----------- Barra menú ----------------------------

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar")
bbdd_menu.add_command(label="Salir")

borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos")

crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear")
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")

ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de...")

barra_menu.add_cascade(label="Base Datos", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Atuda", menu=ayuda_menu)

# ----------- Comienzo de campos ----------------------------

mi_frame=Frame(root)
mi_frame.pack()

cuadro_id=Entry(mi_frame)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre=Entry(mi_frame)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="red", justify="right")

cuadro_password=Entry(mi_frame)
cuadro_password.grid(row=2, column=1, padx=10, pady=10)
cuadro_password.config(show="*")

cuadro_apellido=Entry(mi_frame)
cuadro_apellido.grid(row=3, column=1, padx=10, pady=10)

cuadro_direccion=Entry(mi_frame)
cuadro_direccion.grid(row=4, column=1, padx=10, pady=10)

texto_comentatio=Text(mi_frame, width=26, height=5)
texto_comentatio.grid(row=5, column=1, padx=10, pady=10)
scroll_vertical=Scrollbar(mi_frame, command=texto_comentatio.yview)
scroll_vertical.grid(row=5, column=2, sticky="nsew")

texto_comentatio.config(yscrollcommand=scroll_vertical.set)

root.mainloop()
