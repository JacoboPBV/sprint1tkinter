import tkinter as tk

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 3")
root.geometry("200x50")


# Crea una nueva etiqueta para saludar a la persona
def saludar():
    if entry.get() != '':
        saludo = tk.Label(root, text="¡Hola, " + entry.get() + "!")
        saludo.grid(row=1, column=1)


# Labels
label = tk.Label(root, text="Nombre:")
label.grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)
boton = tk.Button(root, text="SALUDAR", command=saludar)
boton.grid(row=1, column=0)

# Mainloop
root.mainloop()
