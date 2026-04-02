import tkinter as tk
from tkinter import messagebox
from Operaciones import combinacion

def calcular():
    try:
        n=int(n_entry.get())
        k=int(k_entry.get()) 
        resultado=combinacion(n,k)
        resultado_label["text"]=resultado
    except ValueError:
        messagebox.showerror("Error", "Ingrese números enteros válidos")
    except RecursionError:
        messagebox.showerror("Error", "Valores demasiado grandes para cálculo recursivo")

#Ventana
ventana=tk.Tk()
ventana.title("Calculadora de Combinatoria Básica")
ventana.geometry("400x300")
ventana.resizable(False, False)

#Titulo
titulo=tk.Label(ventana, text="Calculadora de Combinatoria Básica", font=("Arial",12))
titulo.pack(pady=10)

#Frames
frame_entradas=tk.Frame(ventana)
frame_entradas.pack(pady=10)

#Entradas de n y k
n_label=tk.Label(frame_entradas, text="n:",font=("Arial"), padx=10)
n_label.grid(row=0,column=0)

n_entry=tk.Entry(frame_entradas, width=10)
n_entry.grid(row=0,column=1)

k_label=tk.Label(frame_entradas, text="k:",font=("Arial"), padx=10)
k_label.grid(row=0,column=2)

k_entry=tk.Entry(frame_entradas, width=10)
k_entry.grid(row=0,column=3)

#Boton de calcular
boton_calc=tk.Button(ventana,text="CALCULAR",bg="blue",fg="white",font=("Arial", 12, "bold"), command=calcular)
boton_calc.pack(pady=15)

#Etiqueta para mostrar resultado
resultado_label=tk.Label(ventana,text="Resultado:", fg="Green", font=("Arial", 12, "bold"))
resultado_label.pack(side="bottom")

#Mantiene la ventana abierta
ventana.mainloop()
