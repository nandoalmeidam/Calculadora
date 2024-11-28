import tkinter as tk
from tkinter import messagebox

# FUNÇÃO PARA CALCULAR
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = entry_op.get()

        if op not in["+","-","*","/"]:
            messagebox.showerror("Erro", "Operação inválida! Use +, -, * ou /.")
            return

        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "*":
            resultado = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não é permitida!")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Erro", "Operação inválida! Use +, -, * ou /.")
            return
        
        label_result.config(text=f"Resultado: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")


# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Layout
tk.Label(janela, text="Número 1:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Operação (+, -, *, /):").grid(row=1, column=0, padx=10, pady=10)
entry_op = tk.Entry(janela)
entry_op.grid(row=1, column=1, padx=10, pady=0)

tk.Label(janela, text="Número 2:").grid(row=2, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(janela)
entry_num2.grid(row=2, column=1, padx=10, pady=10)

button_calcular = tk.Button(janela, text="Calcular", command=calcular)
button_calcular.grid(row=3, column=0, columnspan=2, pady=20)

label_result = tk.Label(janela, text="Resultado: ", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface
janela.mainloop()