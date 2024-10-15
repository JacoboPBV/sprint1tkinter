import tkinter as tk

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 6")
root.geometry("300x250")


# Muestra las frutas seleccionadas de la lista
def mostrar_seleccion():
    seleccion = lista_de_frutas.curselection()
    label.config(text=f"Fruta(s) seleccionada(s): {', '.join(lista_de_frutas.get(i) for i in seleccion)}")


opciones = ["Manzana", "Banana", "Naranja"]

# Inicializa la lista
lista_de_frutas = tk.Listbox(root, selectmode=tk.MULTIPLE)
for opcion in opciones:
    lista_de_frutas.insert(tk.END, opcion)
lista_de_frutas.pack(pady=5)

# Establece un botón para obtener la selección
boton = tk.Button(text="Mostrar Selección", command=mostrar_seleccion)
boton.pack(pady=5)

# Establece una etiqueta para visualizar el contenido de la selección
label = tk.Label(text="Fruta(s) seleccionada(s): ")
label.pack()

# Mainloop
root.mainloop()
