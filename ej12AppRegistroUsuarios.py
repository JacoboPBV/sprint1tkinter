import tkinter as tk
from operator import indexOf, index
from tkinter import messagebox

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 12")
root.geometry("300x500")


def registrar_usuario():
    if nombre.get() == "":
        messagebox.showinfo("ATENCIÓN", "No has puesto ningún nombre.")
    elif edad.get() == 0:
        messagebox.showinfo("Tu edad es 0", "¿Seguro que puedes estar aquí?")
    elif var_genero.get() == "None":
        messagebox.showinfo("ATENCIÓN", "No has seleccionado ningún género.")
    else:
        usuarios.insert(tk.END, nombre.get(), edad.get(), var_genero.get())


def eliminar_usuario():
    if usuarios.curselection():
        if usuarios.index(usuarios.curselection()) % 3 == 0:
            usuarios.delete(usuarios.index(usuarios.curselection()), usuarios.index(usuarios.curselection()) + 2)
        elif usuarios.index(usuarios.curselection()) % 3 == 1:
            usuarios.delete(usuarios.index(usuarios.curselection()) - 1, usuarios.index(usuarios.curselection()) + 1)
        elif usuarios.index(usuarios.curselection()) % 3 == 2:
            usuarios.delete(usuarios.index(usuarios.curselection()) - 2, usuarios.index(usuarios.curselection()))
        else:
            messagebox.showinfo("Not an option.")


def guardar_lista():
    messagebox.showinfo("Lista guardada", "La lista se ha guardado correctamente")


def cargar_lista():
    messagebox.showinfo("Lista cargada", "La lista se ha cargado correctamente")


def salir():
    root.destroy()


# Botón de Salir
salir = tk.Button(root, text="SALIR", command=salir)
salir.grid(row=0, column=4, sticky="ne")

# Entry de Nombre
nombre = tk.Entry(root)
nombre.grid(row=1, column=1, columnspan=2)

# Scale de Edad
edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
edad.grid(row=2, column=1, columnspan=2)

# Inicializamos variable a compartir por los radiobuttons
var_genero = tk.StringVar()
var_genero.set(str(None))  # Paso None para que no esté seleccionado ningún valor
# El str() es para que no ponga ningún warning

# Radiobuttons de género
masculino = tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Hombre")
masculino.grid(row=3, column=1, sticky="w")
femenino = tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Mujer")
femenino.grid(row=4, column=1, sticky="w")
otro = tk.Radiobutton(root, text="Otro", variable=var_genero, value="No-Binario")
otro.grid(row=5, column=1, sticky="w")

# Botón de Registrar Usuario
registro = tk.Button(root, text="Registrarse", command=registrar_usuario)
registro.grid(row=6, column=2)

tk.Label(root).grid(row=7)  # Espacio decorativo

# Inicializa la lista
usuarios = tk.Listbox(root, selectmode=tk.SINGLE)
usuarios.grid(row=8, column=1, columnspan=2)

# Scrollbar Vertical
scrollbar_v = tk.Scrollbar(root, orient="vertical", command=usuarios.yview)
scrollbar_v.grid(row=8, column=3, sticky="ns")
usuarios.config(yscrollcommand=scrollbar_v.set)

# Botón de Eliminar Usuario
eliminar = tk.Button(root, text="Eliminar usuario", command=eliminar_usuario)
eliminar.grid(row=9, column=2)

# Menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Crear submenú "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)

# Configuración del Grid
root.grid_rowconfigure(1, pad=20)
root.grid_rowconfigure(3, pad=10)
root.grid_rowconfigure(5, pad=10)
root.grid_rowconfigure(7, pad=15)
root.grid_rowconfigure(9, pad=15)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(10, weight=1)
root.grid_columnconfigure(4, weight=1)

# Mainloop
root.mainloop()
