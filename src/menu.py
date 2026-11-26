import pygame 
from botao import Botao


class Menu:
    def __init__(self, largura):

        # tamanho dos botões
        largura_botao = 300
        altura_botao = 55

        x = largura - largura_botao - 100
        self.jogar = Botao("JOGAR", x, 225, largura_botao, altura_botao)
        self.instrucoes = Botao("INSTRUÇÕES", x, 300, largura_botao, altura_botao)
        self.creditos = Botao("CRÉDITOS", x, 375, largura_botao, altura_botao)
        self.sair = Botao("SAIR", x, 450, largura_botao, altura_botao)

