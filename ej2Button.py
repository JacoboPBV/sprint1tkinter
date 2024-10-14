import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 1")
root.geometry("720x500")

def cambiar_texto():
    boton1.config(text="¡Bien hecho!")

def cerrar():
    root.destroy()

boton1 = tk.Button(root, text="¡Pulsa Aquí!", command=cambiar_texto)
boton1.pack(pady=5)

boton2 = tk.Button(root, text="Cerrar", command=cerrar)
boton2.pack(padx=5)


root.mainloop()