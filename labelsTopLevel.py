#labelsTopLevel.py

import tkinter as tk
from tkinter import ttk

def agregar_elementos():
    # Crear una nueva ventana Toplevel
    ventana = tk.Toplevel(root)
    
    # Crear un label en la ventana Toplevel
    label = ttk.Label(ventana, text="Hola, soy un label en el Toplevel!")
    label.pack()
    
    # Imprimir el texto del label en la ventana principal
    texto_label = label.cget("text")
    label_principal.config(text=texto_label)

# Crear la ventana principal
root = tk.Tk()

# Crear un label en la ventana principal
label_principal = ttk.Label(root, text="Hola, soy un label en la ventana principal!")
label_principal.pack()

# Crear un botón para agregar elementos a la ventana principal
boton = ttk.Button(root, text="Agregar elementos", command=agregar_elementos)
boton.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
