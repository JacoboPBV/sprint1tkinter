import tkinter as tk

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 7")
root.geometry("800x500")


def crear_circulo():
    # Indices del primer Entry
    x0 = float(inicio.get().split(",").__getitem__(0))
    y0 = float(inicio.get().split(",").__getitem__(1))
    # Indices del segundo Entry
    x1 = float(final.get().split(",").__getitem__(0))
    y1 = float(final.get().split(",").__getitem__(1))

    canvas.create_oval(x0, y0, x1, y1)


def crear_rectangulo():
    # Indices del primer Entry
    x0 = float(inicio.get().split(",").__getitem__(0))
    y0 = float(inicio.get().split(",").__getitem__(1))
    # Indices del segundo Entry
    x1 = float(final.get().split(",").__getitem__(0))
    y1 = float(final.get().split(",").__getitem__(1))

    canvas.create_rectangle(x0, y0, x1, y1)


# Canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Entry 1
label0 = tk.Label(root, text="X0, Y0:")
label0.pack()
inicio = tk.Entry(root)
inicio.pack()
# Entry 2
label1 = tk.Label(root, text="X1, Y1:")
label1.pack()
final = tk.Entry(root)
final.pack()

# Botones para crear figuras
boton1 = tk.Button(root, text="Crear círculo", command=crear_circulo)
boton1.pack()
boton2 = tk.Button(root, text="Crear rectángulo", command=crear_rectangulo)
boton2.pack()

# Mainloop
root.mainloop()
