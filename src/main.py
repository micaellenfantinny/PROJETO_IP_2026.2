import pygame
from pygame.locals import *
from sys import exit
from menu import Menu

pygame.init()

# config de tela
largura = 1050
altura = 730

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CIn Surfers')

capa =  pygame.image.load("assets/backgrounds/capa_claro.png")
capa = pygame.transform.scale(capa, (largura, altura))

# menu
menu = Menu(largura)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if menu.sair.click(event):
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

    tela.blit(capa, (0, 0))

    menu.jogar.bordas_caixa(tela)
    menu.instrucoes.bordas_caixa(tela)
    menu.creditos.bordas_caixa(tela)
    menu.sair.bordas_caixa(tela)

    pygame.display.update()

