import tkinter as tk

#Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 2")
root.geometry("720x500")

#Cambiar texto del botón1
def cambiar_texto():
    boton1.config(text="¡Bien hecho!")

#Finaliza el programa destruyendo todo de raíz con el botón2
def cerrar():
    root.destroy()

#Botones
boton1 = tk.Button(root, text="¡Pulsa Aquí!", command=cambiar_texto)
boton1.pack(pady=5)
boton2 = tk.Button(root, text="Cerrar", command=cerrar)
boton2.pack(padx=5)

#Mainloop
root.mainloop()
