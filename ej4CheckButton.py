import tkinter as tk
from cProfile import label

root = tk.Tk()
root.title("Ejercicio 3")
root.geometry("300x200")


def mostrar_estado():
    estadoL = "Seleccionado" if var_leer.get() else "No seleccionado"
    labelL.config(text="Leer: " + estadoL)
    estadoD = "Seleccionado" if var_deporte.get() else "No seleccionado"
    labelD.config(text="Deporte: " + estadoD)
    estadoM = "Seleccionado" if var_musica.get() else "No seleccionado"
    labelM.config(text="Música: " + estadoM)


# CheckLeer
var_leer = tk.IntVar()
leer = tk.Checkbutton(root, text="Leer", variable=var_leer, command=mostrar_estado)
leer.place(x=0, y=0)
# CheckDeporte
var_deporte = tk.IntVar()
deporte = tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=mostrar_estado)
deporte.place(x=0, y=20)
# CheckMusica
var_musica = tk.IntVar()
musica = tk.Checkbutton(root, text="Música", variable=var_musica, command=mostrar_estado)
musica.place(x=0, y=40)

tk.Label().pack()

# Etiquetas
labelL = tk.Label(root, text="Leer: No seleccionado")
labelL.place(x=100, y=2)
labelD = tk.Label(root, text="Deporte: No seleccionado")
labelD.place(x=100, y=22)
labelM = tk.Label(root, text="Música: No seleccionado")
labelM.place(x=100, y=42)

root.mainloop()
