import pygame
import os

pygame.init()

# Classe para ícones laterais (botões)
class IconeBotao:
    def __init__(self, icone, posicao, altura, largura):
        self.icone = icone
        self.posicao = posicao
        self.img = pygame.image.load(icone)
        self.img = pygame.transform.scale(self.img, (altura, largura))
        self.rect = pygame.Rect(posicao, (altura, largura))

    def desenhar(self):
        screen.blit(self.img, self.posicao)

    def foi_clicado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)

# Configuração da tela
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
largura_tela = screen.get_width()
altura_tela = screen.get_height()

def encontrar_posicao_adicao(marcacao):
    FILE_CODIGO = "Teste.py"
    if not os.path.exists(FILE_CODIGO):
        return None

    with open(FILE_CODIGO, "r") as file:
        linhas = file.readlines()

    for i, linha in enumerate(linhas):
        if marcacao in linha:
            return i + 1  # Retorna a linha após a marcação

    return None  # Marcações não encontradas

def adicionar_codigo(codigo, marcacao):
    FILE_CODIGO = "Teste.py"

    if not os.path.exists(FILE_CODIGO):
        codigo_base()
        posicao = 0
    posicao = encontrar_posicao_adicao(marcacao)
    if posicao is None:
        posicao = len(codigo)  # Se não encontrou a marcação, adiciona no final

    with open(FILE_CODIGO, "r") as file:
        linhas = file.readlines()

    novas_linhas = linhas[:posicao] + [linha + "\n" for linha in codigo] + linhas[posicao:]

    with open(FILE_CODIGO, "w") as file:
        file.writelines(novas_linhas)

def codigo_base():
    codigo = [
        "#imports",
        "from tkinter import *",
        "#defs",
        "def acao_botao():",
        "    print('Botao foi clicado!')",
        "#labels/btns",
        "root = Tk()",
        "root.title('Titulo da janela')",
        "root.geometry('300x300')",
        "#packs",
        "root.mainloop()"
    ]

    FILE_CODIGO = "Teste.py"
    if os.path.exists(FILE_CODIGO):
        os.remove(FILE_CODIGO)
    with open(FILE_CODIGO, "w") as file:
        for linha in codigo:
            file.write(linha + "\n")

def codigo_tk_btn():
    btn_codigo = [
        "btn = Button(root, text='Clique aqui!',command=acao_botao)",
        "btn.pack()"
    ]
    adicionar_codigo(btn_codigo, "#packs")

def codigo_tk_btn_comando():
    comando_codigo = [
        "def acao_botao():",
        "    print('Botao foi clicado!')"
    ]
    adicionar_codigo(comando_codigo, "#defs")
    codigo_tk_btn()

def acao_play():
    print("Ícone Play foi clicado!")

def ajustar_icones():
    altura_barra_topo = 50
    espaco_entre_icones = 10

    icone_Play.posicao = (largura_tela - 50, 5)
    icone_Play.rect.topleft = icone_Play.posicao

    icone_1.posicao = (10, altura_barra_topo + espaco_entre_icones)
    icone_1.rect.topleft = icone_1.posicao

def barra_topo():
    pygame.draw.rect(screen, (240, 248, 255), (0, 0, largura_tela, 50))
    icone_Play.desenhar()

def barra_lateral():
    pygame.draw.rect(screen, (124, 252, 0), (0, 50, 100, altura_tela))
    icone_1.desenhar()

def janela_desenho():
    pygame.draw.rect(screen, (0, 0, 0), (100, 50, largura_tela - 100, altura_tela - 50))

icone_1 = IconeBotao("imgs/botao-de-inicio.png", (10, 10), 50, 50)
icone_Play = IconeBotao("imgs/botao-play.png", (10, 5), 40, 40)

ajustar_icones()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if icone_1.foi_clicado(event.pos):
                codigo_tk_btn_comando()
            elif icone_Play.foi_clicado(event.pos):
                acao_play()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            largura_tela, altura_tela = event.w, event.h
            screen = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE)
            ajustar_icones()

    screen.fill((255, 255, 255))

    barra_topo()
    barra_lateral()
    janela_desenho()

    pygame.display.flip()

pygame.quit()
