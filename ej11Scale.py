import tkinter as tk
from tkinter import messagebox

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 11")
root.geometry("300x150")


def actualizar_valor(val):
    label.config(text=f"Valor: {val}")


# Label para centrar el Scale
tk.Label(root).grid(row=0)

# Scale
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
scale.grid(row=1, column=0)

# Etiqueta del valor del Scale
label = tk.Label(root, text="Valor: 0")
label.grid(row=2, column=0)

# Label para centrar el Scale
tk.Label(root).grid(row=3)

# Configuración para centrar el Scale (no sé si se puede hacer de otra forma más fácil)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

# Mainloop
root.mainloop()
