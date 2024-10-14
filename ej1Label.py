import tkinter as tk

#Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 1")
root.geometry("720x500")

#Cambiar texto de etiqueta3
def cambiar_texto():
    etiqueta3.config(text="Soy Jacobo Pita")

#Etiquetas
etiqueta1 = tk.Label(root, text="Bienvenido!")
etiqueta1.pack(pady=5)
etiqueta2 = tk.Label(root, text="Soy Jacobo Pita")
etiqueta2.pack(pady=5)
etiqueta3 = tk.Label(root, text="Bienvenido!")
etiqueta3.pack(pady=30)

#Botón
boton = tk.Button(root, text="Siguiente", command=cambiar_texto)
boton.pack(pady=5)

#Iniciamos el mainloop
root.mainloop()
