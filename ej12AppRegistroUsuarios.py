import tkinter as tk

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 1")
root.geometry("720x500")


def registrar_usuario():
    usuarios.insert(tk.END, nombre.get(), edad.get(), var_genero.get())


# Entry
nombre = tk.Entry(root)
nombre.grid(row=0, column=0, columnspan=2)

# Scale
edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
edad.grid(row=1, column=0, columnspan=2)

# Inicializamos variable a compartir por los radiobuttons
var_genero = tk.StringVar()
var_genero.set(str(None))  # Paso None para que no esté seleccionado ningún valor
# El str() es para que no ponga ningún warning

# Radiobuttons
masculino = tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Hombre")
masculino.grid(row=2, column=0, sticky="w")
femenino = tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Mujer")
femenino.grid(row=3, column=0, sticky="w")
otro = tk.Radiobutton(root, text="Otro", variable=var_genero, value="No-Binario")
otro.grid(row=4, column=0, sticky="w")

registro = tk.Button(root, text="Registrarse", command=registrar_usuario)
registro.grid(row=5, column=1)

# Inicializa la lista
usuarios = tk.Listbox(root, selectmode=tk.BROWSE)
usuarios.grid(row=7, column=0, columnspan=2)

# Scrollbar Vertical
scrollbar_v = tk.Scrollbar(root, orient="vertical", command=usuarios.yview)
scrollbar_v.grid(row=7, column=2, sticky="ns")
usuarios.config(yscrollcommand=scrollbar_v.set)

# Mainloop
root.mainloop()
