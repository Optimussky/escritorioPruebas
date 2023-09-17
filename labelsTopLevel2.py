#

import tkinter as tk
from tkinter import ttk

def agregar_elementos():
    # Crear una nueva ventana Toplevel
    ventana = tk.Toplevel(root)
    
    def imprimir_label():
        # Obtener el texto del Entry
        texto = entrada.get()
        
        # Crear un label en la ventana principal con el texto del Entry
        label_principal.config(text=texto)
    
    # Crear un Entry en la ventana Toplevel
    entrada = ttk.Entry(ventana)
    entrada.pack()
    
    # Crear un botón para imprimir el label en la ventana principal
    boton_imprimir = ttk.Button(ventana, text="Imprimir", command=imprimir_label)
    boton_imprimir.pack()


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

