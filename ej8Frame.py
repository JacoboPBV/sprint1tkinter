import tkinter as tk

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 8")
root.geometry("800x500")


def mostrar_entry():
    res.config(text=entry.get())


def borrar_entry():
    entry.delete(0, entry.get().__len__())


# Frame1
frame1 = tk.Frame(root, bg="cyan", bd=2, relief="sunken")
frame1.pack(padx=20, pady=20, fill="both", expand=True)
# Frame2
frame2 = tk.Frame(root, bg="cyan", bd=2, relief="sunken")
frame2.pack(padx=20, pady=20, fill="both", expand=True)

# Etiquetas del Frame1
label1 = tk.Label(frame1, text="¡Bienvenido!", bg="cyan")
label1.pack()
label2 = tk.Label(frame1, text="Escribe tu nombre: ", bg="cyan")
label2.pack()

# Entry del Frame1
entry = tk.Entry(frame1)
entry.pack()

# Botones del Frame2
boton = tk.Button(frame2, text="Mostrar", command=mostrar_entry)
boton.pack()
boton = tk.Button(frame2, text="Borrar", command=borrar_entry)
boton.pack()

# Etiqueta del Frame2
res = tk.Label(frame2, bg="cyan")
res.pack()

# Mainloop
root.mainloop()
