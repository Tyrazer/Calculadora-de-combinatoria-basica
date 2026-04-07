import tkinter as tk
from tkinter import messagebox
from Operaciones import combinacion_sin_rep
from Operaciones import combinacion_con_rep
from Operaciones import stirling_second
from Operaciones import permutacion

def calcular():
    try:
        n=int(n_entry.get())
        k=int(k_entry.get()) 
        if n<0 or k<0:
            messagebox.showerror("Error", "Ingrese números no negativos")
            return
        if var_op.get()==1:
            resultado=combinacion_sin_rep(n,k)
            resultado_label.config(text="Resultado: " + str(resultado))
        elif var_op.get()==2:
            resultado=combinacion_con_rep(n,k)
            resultado_label.config(text="Resultado: " + str(resultado))
        elif var_op.get()==3:
            resultado=permutacion(n,k)
            resultado_label.config(text="Resultado: " + str(resultado))
        elif var_op.get()==4:
            resultado=stirling_second(n,k)
            resultado_label.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Ingrese números enteros válidos")
    except RecursionError:
        messagebox.showerror("Error", "Valores demasiado grandes para cálculo recursivo")

#Ventana
ventana=tk.Tk()
ventana.title("Calculadora de Combinatoria Básica")
ventana.geometry("500x400")
ventana.resizable(False, False)

#Titulo
titulo=tk.Label(ventana, text="Calculadora de Combinatoria Básica", font=("Arial",20), fg="#1e3a5f")
titulo.pack(pady=10)

#Frame para las entradas
frame_entradas=tk.Frame(ventana)
frame_entradas.pack(pady=10)

#Entradas de n y k
n_label=tk.Label(frame_entradas, text="n:",font=("Arial"),fg="#334e68", padx=10,pady=20)
n_label.grid(row=1,column=0)

n_entry=tk.Entry(frame_entradas, width=10)
n_entry.grid(row=1,column=1)

k_label=tk.Label(frame_entradas, text="k:",font=("Arial"),fg="#334e68", padx=10)
k_label.grid(row=1,column=2)

k_entry=tk.Entry(frame_entradas, width=10)
k_entry.grid(row=1,column=3)

#Selección de operación
var_op=tk.IntVar(value=1)

rb_comb_sin_rep=tk.Radiobutton(ventana,text="Combinación sin repetición",font=("Arial",12),variable=var_op, value=1,fg="#334e68")
rb_comb_con_rep=tk.Radiobutton(ventana,text="Combinación con repetición",font=("Arial",12),variable=var_op, value=2, fg="#334e68")
rb_perm=tk.Radiobutton(ventana, text="Permutación",font=("Arial",12), variable=var_op, value=3,fg="#334e68")
rb_stirling=tk.Radiobutton(ventana,text="Números de stirling de segunda clase",font=("Arial",12),variable=var_op, value=4, fg="#334e68")

rb_comb_sin_rep.pack()
rb_comb_con_rep.pack()
rb_perm.pack()
rb_stirling.pack()

#Boton de calcular
boton_calc=tk.Button(ventana,text="CALCULAR",bg="#0078D7",fg="white",font=("Arial", 20, "bold"), command=calcular)
boton_calc.pack(pady=15)

#Etiqueta para mostrar resultado
borde=tk.Frame(ventana, bg="#2c7da0", padx=2, pady=2, relief=tk.RIDGE)
borde.pack()
resultado_label=tk.Label(borde,text="Resultado:", fg="#2c7da0", font=("Arial", 20, "bold"))
resultado_label.pack()

#Mantiene la ventana abierta
ventana.mainloop()
