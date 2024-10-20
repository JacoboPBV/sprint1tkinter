import tkinter as tk
from tkinter import messagebox

# Inicializamos el TKinter
root = tk.Tk()
root.title("Ejercicio 9")
root.geometry("800x500")


def salir():
    root.quit()


def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Te informo de que no te puedo ofrecer ayuda")


# Menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Crear submenú "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Crear submenú "Ayuda"
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)

# Mainloop
root.mainloop()
