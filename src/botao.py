import pygame


class Botao:
    def __init__(self, txt, x, y, largura, altura):
        self.texto = txt
        self.retangulo = pygame.Rect(x, y, largura, altura)
        self.fonte = pygame.font.SysFont("bodonimtblack", 26)

        # paleta
        self.vermelho = (149, 27, 60)
        self.hover = (200, 62, 96)
        self.sombra = (80, 12, 36)
        self.borda = (232, 165, 174)
        self.branco = (255, 240, 232)

    def bordas_caixa(self, tela):
        sombreado_rect = pygame.Rect(
            self.retangulo.x,
            self.retangulo.bottom,
            self.retangulo.width,
            6
        )

        pygame.draw.rect(tela, self.sombra, sombreado_rect)

        caixa = pygame.Surface(self.retangulo.size, pygame.SRCALPHA)

        mouse = pygame.mouse.get_pos()

        # aplicando o conceito aprendido de operador ternário
        caixa.fill((*self.hover, 255) if self.retangulo.collidepoint(mouse) else (*self.vermelho, 255))

        cor_txt = self.branco

        tela.blit(caixa, self.retangulo.topleft)

        pygame.draw.rect(tela, self.borda, self.retangulo, 3)

        txt_botao = self.fonte.render(self.texto, True, cor_txt)
        posicao_txt = txt_botao.get_rect(center=self.retangulo.center)
        tela.blit(txt_botao, posicao_txt)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.retangulo.collidepoint(event.pos):
                    return True
        return False