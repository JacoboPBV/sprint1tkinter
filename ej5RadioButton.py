import tkinter as tk

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 5")
root.geometry("300x200")


# Cambiamos el color de la ventana directamente con el value del radiobutton escogido
def cambiar_color_ventana():
    root.config(bg=var_radio.get())


# Inicializamos variable a compartir por los radiobuttons
var_radio = tk.StringVar()
var_radio.set(str(None))  # Paso None para que no esté seleccionado ningún valor
# El str() es para que no ponga ningún warning

# Radiobuttons
rojo = tk.Radiobutton(root, text="Rojo", variable=var_radio, value="red", command=cambiar_color_ventana)
rojo.pack(expand=True)
verde = tk.Radiobutton(root, text="Verde", variable=var_radio, value="green", command=cambiar_color_ventana)
verde.pack(expand=True)
azul = tk.Radiobutton(root, text="Azul", variable=var_radio, value="blue", command=cambiar_color_ventana)
azul.pack(expand=True)

# Mainloop
root.mainloop()
