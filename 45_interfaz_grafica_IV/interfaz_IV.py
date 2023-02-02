from tkinter import *

root = Tk()

mi_frame = Frame(root)
mi_frame.pack()

cuadro_nombre = Entry(mi_frame)
cuadro_nombre.grid(row=0, column=1, pady=10, padx=10)
cuadro_nombre.config(fg='red', justify='center')

cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row=1, column=1, pady=10, padx=10)

cuadro_direccion = Entry(mi_frame)
cuadro_direccion.grid(row=2, column=1, pady=10, padx=10)

cuadro_password = Entry(mi_frame)
cuadro_password.grid(row=3, column=1, pady=10, padx=10)
cuadro_password.config(show='*')

nombre_label = Label(mi_frame, text='Nombre:')
nombre_label.grid(row=0, column=0, sticky='e', pady=10, padx=10)

apellido_label = Label(mi_frame, text='Apellido:')
apellido_label.grid(row=1, column=0, sticky='e', pady=10, padx=10)

direccion_label = Label(mi_frame, text='Dirección:')
direccion_label.grid(row=2, column=0, sticky='e', pady=10, padx=10)

password_label = Label(mi_frame, text='Password:')
password_label.grid(row=3, column=0, sticky='e', pady=10, padx=10)


root.mainloop()