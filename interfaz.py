import tkinter as tk
from tkinter import messagebox
from Operaciones import combinacion
from Operaciones import stirling_second

def calcular():
    try:
        n=int(n_entry.get())
        k=int(k_entry.get()) 
        if var_op.get()==1:
            resultado=combinacion(n,k)
            resultado_label.config(text="Resultado: " + str(resultado))
        elif var_op.get()==2:
            resultado=stirling_second(n,k)
            resultado_label.config(text="Resultado: " + str(resultado))
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

#Selección de operación
var_op=tk.IntVar(value=1)
rb_comb=tk.Radiobutton(ventana,text="Combinación",variable=var_op, value=1)
rb_stirling=tk.Radiobutton(ventana,text="Stirling 2da clase", variable=var_op, value=2)
rb_comb.pack()
rb_stirling.pack()

#Boton de calcular
boton_calc=tk.Button(ventana,text="CALCULAR",bg="blue",fg="white",font=("Arial", 12, "bold"), command=calcular)
boton_calc.pack(pady=15)

#Etiqueta para mostrar resultado
resultado_label=tk.Label(ventana,text="Resultado:", fg="Green", font=("Arial", 12, "bold"))
resultado_label.pack(side="bottom")


#Mantiene la ventana abierta
ventana.mainloop()
