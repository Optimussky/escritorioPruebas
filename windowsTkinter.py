#windowsTkinter.py

import tkinter as tk
from tkinter import messagebox,Label

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    lbl1 = tk.Label(new_window,text="Esto es un label").pack()
    # Add widgets and functionality to the new window
    entrada = tk.Entry(new_window).pack()
    new_window.mainloop()

root = tk.Tk()
root.title("Multiple Windows App")

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open New Window", command=open_new_window)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)
# Label en la ventana principal
label_principal = tk.Label(root, text="Label en la ventana principal").pack()
#Boton para crear elementos a la ventana principal
boton = tk.Button(root, text="Agregar elementos", command=open_new_window)
boton.pack()


root.mainloop()
