from tkinter import *

root = Tk()
mi_frame = Frame(root, width=500, height=400)
mi_frame.pack()

mi_image = PhotoImage(file='/Users/jhonjairoduenasvega/logo/logo.png')

Label(
    mi_frame,
    text='Hola alumnos de Python',
    fg='#408BA9',
    image=mi_image,
    font=('Comic Sans MS', 18)).place(x=100, y=100)

root.mainloop()