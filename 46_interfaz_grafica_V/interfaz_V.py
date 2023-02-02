from tkinter import *

root = Tk()

mi_frame = Frame(root)
mi_frame.pack()

mi_nombre = StringVar()

nombre_label = Label(mi_frame, text='Nombre:')
nombre_label.grid(row=0, column=0, sticky='e', pady=10, padx=10)

apellido_label = Label(mi_frame, text='Apellido:')
apellido_label.grid(row=1, column=0, sticky='e', pady=10, padx=10)

direccion_label = Label(mi_frame, text='Dirección:')
direccion_label.grid(row=2, column=0, sticky='e', pady=10, padx=10)

password_label = Label(mi_frame, text='Password:')
password_label.grid(row=3, column=0, sticky='e', pady=10, padx=10)

comentarios_label = Label(mi_frame, text='Comentarios:')
comentarios_label.grid(row=4, column=0, sticky='e', pady=10, padx=10)

cuadro_nombre = Entry(mi_frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=0, column=1, pady=10, padx=10)
cuadro_nombre.config(fg='red', justify='center')

cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row=1, column=1, pady=10, padx=10)

cuadro_direccion = Entry(mi_frame)
cuadro_direccion.grid(row=2, column=1, pady=10, padx=10)

cuadro_password = Entry(mi_frame)
cuadro_password.grid(row=3, column=1, pady=10, padx=10)
cuadro_password.config(show='*')

text_comentario = Text(mi_frame, width=26, height=10)
text_comentario.grid(row=4, column=1)

scroll_vertical = Scrollbar(mi_frame, command=text_comentario.yview)
scroll_vertical.grid(row=4, column=2, sticky='nsew')

text_comentario.config(yscrollcommand=scroll_vertical.set)

def codigo_boton():
    mi_nombre.set('Jairo')

boton_enviar = Button(root, text='Enviar', command=codigo_boton)
boton_enviar.pack()


root.mainloop()