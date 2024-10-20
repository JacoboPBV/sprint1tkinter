import tkinter as tk
from tkinter import messagebox

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 9")
root.geometry("500x400")


def insert_lines():
    for i in range(1, 100):
        cuadro_texto.insert(tk.END, str(i) + "\n")
    cuadro_texto.insert(tk.END, str(100))


# Texto largo
cuadro_texto = tk.Text(root, wrap="none")
cuadro_texto.grid(row=0, column=0, sticky="nsew")

# Scrollbar Vertical
scrollbar_v = tk.Scrollbar(root, orient="vertical", command=cuadro_texto.yview)
scrollbar_v.grid(row=0, column=1, sticky="ns")
cuadro_texto.config(yscrollcommand=scrollbar_v.set)

# Configuración para pegar el cuadro a la ventana
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Relleno del cuadro de texto
insert_lines()

# Mainloop
root.mainloop()
