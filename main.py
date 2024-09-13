import tkinter as tk
import os

from tkinter import messagebox

def comando(botao_texto):
    try:
        if botao_texto == "Sair":
            exit()
        if botao_texto != "":
            File = f"{botao_texto}/main.py"
            os.system(f"python {File}")
        else:
            messagebox.showerror("Erro", "Erro ao executar o comando\nArquivo não encontrado ou nao existe")
    except:
        messagebox.showerror("Erro", "Erro ao executar o comando\nArquivo não encontrado ou nao existe")

def main():
    janela = tk.Tk()
    janela.title("Janela Principal")
    janela.geometry("800x600")

    botoes = {
        "Calculadora": "Calculadora/main.py",
        "Botao2": "Botao 2",
        "Botao3": "Botao 3"
    }
    
    for botao_texto in botoes:
        botao = tk.Button(janela, text=botao_texto, command=lambda texto=botao_texto: comando(texto))
        botao.pack()
    
    janela.mainloop()

if __name__ == "__main__":
    main()
