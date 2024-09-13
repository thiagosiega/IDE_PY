#imports
from tkinter import *
#defs
def acao_botao():
    print('Botao foi clicado!')
def acao_botao():
    print('Botao foi clicado!')
#labels/btns
root = Tk()
root.title('Titulo da janela')
root.geometry('300x300')
#packs
btn = Button(root, text='Clique aqui!',command=acao_botao)
btn.pack()
root.mainloop()
