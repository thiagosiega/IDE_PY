def acao_botao():    print('Bot�o foi clicado!')from tkinter import *
root = Tk()
root.title('Titulo da janela')
root.geometry('300x300')
btn = Button(root, text='Clique aqui!')
btn.pack()
btn = Button(root, text='Clique aqui!')
btn.pack()
btn = Button(root, text='Clique aqui!')
btn.pack()
btn = Button(root, text='Clique aqui!')
btn.pack()
root.mainloop()
