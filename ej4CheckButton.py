import tkinter as tk
from cProfile import label

root = tk.Tk()
root.title("Ejercicio 3")
root.geometry("300x150")

def mostrar_estado():
    estadoL = "Seleccionado" if var_leer.get() else "No seleccionado"
    labelL.config(text="Leer: " + estadoL)
    estadoD = "Seleccionado" if var_deporte.get() else "No seleccionado"
    labelD.config(text="Deporte: " + estadoD)
    estadoM = "Seleccionado" if var_musica.get() else "No seleccionado"
    labelM.config(text="Música: " + estadoM)

var_leer = tk.IntVar()
leer = tk.Checkbutton(root, text="Leer", variable=var_leer, command=mostrar_estado)
leer.pack()

var_deporte = tk.IntVar()
deporte = tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=mostrar_estado)
deporte.pack()

var_musica = tk.IntVar()
musica = tk.Checkbutton(root, text="Música", variable=var_musica, command=mostrar_estado)
musica.pack()

labelL = tk.Label(root, text="Leer: No seleccionado")
labelL.pack()
labelD = tk.Label(root, text="Deporte: No seleccionado")
labelD.pack()
labelM = tk.Label(root, text="Música: No seleccionado")
labelM.pack()


root.mainloop()