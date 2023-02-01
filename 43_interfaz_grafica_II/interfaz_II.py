from tkinter import *
import os

root = Tk()

root.iconbitmap('logo.png')
root.title('Ventana de prueba 2')
root.config(
    bg='yellow',
    relief='sunken',
    bd=35,
    cursor='pirate')

mi_frame = Frame()
# mi_frame.pack(side='bottom', anchor='e')
# mi_frame.pack(fill='y', expand='True')
mi_frame.pack()
mi_frame.config(
    bg='red',
    width='650',
    height='350',
    relief='groove',
    bd=35,
    cursor='hand2')

root.mainloop()