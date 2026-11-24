import pygame
from pygame.locals import *
from sys import exit
from menu import Botao

pygame.init()

largura = 1050
altura = 730

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CIn Surfers')

capa =  pygame.image.load("assets/backgrounds/capa_claro.png")
capa = pygame.transform.scale(capa, (largura, altura))

# tamanho dos botões
largura_botao = 300
altura_botao = 55

x = largura - largura_botao - 100

jogar = Botao("JOGAR", x, 225, largura_botao, altura_botao)
instrucoes = Botao("INSTRUÇÕES", x, 300, largura_botao, altura_botao)
creditos = Botao("CRÉDITOS", x, 375, largura_botao, altura_botao)
sair = Botao("SAIR", x, 450, largura_botao, altura_botao)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(capa, (0, 0))

    jogar.bordas_caixa(tela)
    instrucoes.bordas_caixa(tela)
    creditos.bordas_caixa(tela)
    sair.bordas_caixa(tela)

    pygame.display.update()

