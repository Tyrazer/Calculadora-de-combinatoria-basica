import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()
ventana.geometry("300x300")
etiqueta = tk.Label(ventana, text = "Hola Mundo", background="red")
etiqueta.pack(fill=tk.X)

etiqueta2= tk.Label(ventana)
etiqueta2.pack(side="left")
def saludopndejo():
    print("Hola Pendejo")

boton1= tk.Button(ventana, text="Saluda", command=saludopndejo)
boton1.pack(side="bottom")

cajatexto=tk.Entry(ventana)
cajatexto.pack(side="right")

def nombre():
    nombre=cajatexto.get()
    print(nombre)
    etiqueta2["text"]=nombre

boton2=tk.Button(ventana, text="Nombre", command=nombre)
boton2.pack(side="right")
ventana.mainloop()

