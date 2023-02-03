from tkinter import *
from tkinter import messagebox
import sqlite3

# ----------- Funciones ----------------------------

def conexion_BBDD():
  mi_conexion=sqlite3.connect("Usuarios")
  mi_cursor=mi_conexion.cursor()

  try:
    mi_cursor.execute('''
        CREATE TABLE DATOSUSUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(10),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(100))
      ''')

    messagebox.showinfo("Base de datos", "Base de datos creada con éxito")

  except:
    messagebox.showwarning("¡Atención!", "La base de datos ya existe")

def salir_aplicacion():
  valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación")

  if valor=="yes":
    root.destroy()

# --------------------------------------------------

root=Tk()

barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

# ----------- Barra menú ----------------------------

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexion_BBDD)
bbdd_menu.add_command(label="Salir", command=salir_aplicacion)

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
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

# ----------- Comienzo de campos ----------------------------

mi_frame=Frame(root)
mi_frame.pack()

mi_id=StringVar()
mi_nombre=StringVar()
mi_apellido=StringVar()
mi_password=StringVar()
mi_direccion=StringVar()

cuadro_id=Entry(mi_frame, textvariable=mi_id)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre=Entry(mi_frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="red", justify="right")

cuadro_password=Entry(mi_frame, textvariable=mi_password)
cuadro_password.grid(row=2, column=1, padx=10, pady=10)
cuadro_password.config(show="*")

cuadro_apellido=Entry(mi_frame, textvariable=mi_apellido)
cuadro_apellido.grid(row=3, column=1, padx=10, pady=10)

cuadro_direccion=Entry(mi_frame, textvariable=mi_direccion)
cuadro_direccion.grid(row=4, column=1, padx=10, pady=10)

texto_comentatio=Text(mi_frame, width=26, height=5)
texto_comentatio.grid(row=5, column=1, padx=10, pady=10)
scroll_vertical=Scrollbar(mi_frame, command=texto_comentatio.yview)
scroll_vertical.grid(row=5, column=2, sticky="nsew")

texto_comentatio.config(yscrollcommand=scroll_vertical.set)

# ----------- Los Labels ----------------------------

id_label=Label(mi_frame, text="Id:")
id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombre_label=Label(mi_frame, text="Nombre:")
nombre_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

pass_label=Label(mi_frame, text="Password:")
pass_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellido_label=Label(mi_frame, text="Apellido:")
apellido_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccion_label=Label(mi_frame, text="Dirección:")
direccion_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarios_label=Label(mi_frame, text="Comentarios:")
comentarios_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# ----------- Botones CRUD ----------------------------

botones_frame=Frame(root)
botones_frame.pack()

boton_crear=Button(botones_frame, text="Create")
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_Leer=Button(botones_frame, text="Read")
boton_Leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar=Button(botones_frame, text="Update")
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(botones_frame, text="Delete")
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
