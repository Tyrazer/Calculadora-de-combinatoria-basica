import tkinter as tk
from tkinter import messagebox
from operaciones import combinacion_sin_rep
from operaciones import combinacion_con_rep
from operaciones import stirling_second
from operaciones import permutacion
from operaciones import permutacion_con_rep
from operaciones import permutacion_con_repetidos

def actualizar_campo_frecuencias():
    if var_op.get() == 5:
        label_frecuencias.pack(pady=5)
        entry_frecuencias.pack(pady=5)
        k_label.config(text="k (coloque 1 si usa frecuencias):")
    else:
        label_frecuencias.pack_forget()
        entry_frecuencias.pack_forget()
        k_label.config(text="k:")

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
        elif var_op.get()==5:
            frecuencias_texto = entry_frecuencias.get().strip()
            if not frecuencias_texto:
                messagebox.showerror("Error", "Ingrese las frecuencias separadas por coma")
                return
                
            frecuencias = [int(x.strip()) for x in frecuencias_texto.split(",")]
            
            if sum(frecuencias) != n:
                messagebox.showerror("Error", "La suma de las frecuencias debe ser igual a n")
                return
                
            resultado = permutacion_con_rep(n, frecuencias)
            resultado_label.config(text="Resultado: " + str(resultado))
        elif var_op.get()==6:
            resultado=permutacion_con_repetidos(n,k)
            resultado_label.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Ingrese números enteros válidos")
    except RecursionError:
        messagebox.showerror("Error", "Valores demasiado grandes para cálculo recursivo")
#Ventana
ventana=tk.Tk()
ventana.title("Calculadora de Combinatoria Básica")
ventana.geometry("500x500")
ventana.resizable(False, False)
#Título
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
#Entrada de las frecuencias (Para permutaciones con frecuencias)
label_frecuencias = tk.Label(ventana, text="Frecuencias (separadas por coma):", font=("Arial", 10), fg="#334e68")
entry_frecuencias = tk.Entry(ventana, width=30)
#Selección de operación
var_op=tk.IntVar(value=1)
rb_comb_sin_rep=tk.Radiobutton(ventana,text="Combinación sin repetición",font=("Arial",12),variable=var_op, value=1,fg="#334e68", command=actualizar_campo_frecuencias)
rb_comb_con_rep=tk.Radiobutton(ventana,text="Combinación con repetición",font=("Arial",12),variable=var_op, value=2, fg="#334e68", command=actualizar_campo_frecuencias)
rb_perm=tk.Radiobutton(ventana, text="Permutación",font=("Arial",12), variable=var_op, value=3,fg="#334e68", command=actualizar_campo_frecuencias)
rb_stirling=tk.Radiobutton(ventana,text="Números de stirling de segunda clase",font=("Arial",12),variable=var_op, value=4, fg="#334e68", command=actualizar_campo_frecuencias)
rb_perm_con_rep=tk.Radiobutton(ventana,text="Permutación con frecuencias",font=("Arial",12),variable=var_op, value=5, fg="#334e68", command=actualizar_campo_frecuencias)
rb_perm_con_repetidos=tk.Radiobutton(ventana,text="Permutación con repetidos",font=("Arial",12),variable=var_op, value=6, fg="#334e68", command=actualizar_campo_frecuencias)
rb_comb_sin_rep.pack()
rb_comb_con_rep.pack()
rb_perm.pack()
rb_perm_con_rep.pack()
rb_perm_con_repetidos.pack()
rb_stirling.pack()
#Botón de calcular
boton_calc=tk.Button(ventana,text="CALCULAR",bg="#0078D7",fg="white",font=("Arial", 20, "bold"), command=calcular)
boton_calc.pack(pady=15)
borde=tk.Frame(ventana, bg="#2c7da0", padx=2, pady=2, relief=tk.RIDGE)
borde.pack()
#Etiqueta con el resultado
resultado_label=tk.Label(borde,text="Resultado:", fg="#2c7da0", font=("Arial", 20, "bold"))
resultado_label.pack()

actualizar_campo_frecuencias()
ventana.mainloop()