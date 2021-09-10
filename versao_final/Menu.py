import pygame
import sys
from TelaJogo import TelaJogo


class MenuJogo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tela = TelaJogo()
        self.is_on_menu = True
        self.__tamanho_botao = (self.tela.largura - 250, 80)
        self.__posicao_botao = ((self.tela.largura / 4) - 80, 150)
    
    def mensagens(self):
        fonte_nome = pygame.font.SysFont('comicssans', 100)
        fonte_botao = pygame.font.SysFont('comicssans', 70)

        nome_jogo = fonte_nome.render("*Nome do Jogo", True, (255,255,255))
        self.tela.janela.blit(nome_jogo, (self.tela.largura / 6, 10))

        botao_iniciar = fonte_botao.render("Jogar", True, (0,0,0))
        self.tela.janela.blit(botao_iniciar, (self.__posicao_botao[0] + 200, self.__posicao_botao[1] + 15))

        botao_configuracao = fonte_botao.render("Configurações", True, (0,0,0))
        self.tela.janela.blit(botao_configuracao, (self.__posicao_botao[0] + 100, self.__posicao_botao[1] + self.__tamanho_botao[1] + 65))

        botao_sair = fonte_botao.render("Sair", True, (0,0,0))
        self.tela.janela.blit(botao_sair, (self.__posicao_botao[0] + 220, self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50) + 15))
    
    def botoes(self):
        pygame.draw.rect(self.tela.janela, (0,255,0), [self.__posicao_botao[0], self.__posicao_botao[1], self.__tamanho_botao[0], self.__tamanho_botao[1]])
        pygame.draw.rect(self.tela.janela, (128,128,128), [self.__posicao_botao[0], self.__posicao_botao[1] + self.__tamanho_botao[1] + 50, self.__tamanho_botao[0], self.__tamanho_botao[1]])
        pygame.draw.rect(self.tela.janela, (255,0,0), [self.__posicao_botao[0], self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50), self.__tamanho_botao[0], self.__tamanho_botao[1]])
    
    def menu(self):
        self.tela.mostrar_fundo()
        self.botoes()
        self.mensagens()

        while self.is_on_menu:
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and self.__posicao_botao[1] + self.__tamanho_botao[1] > mouse[1] > self.__posicao_botao[1]:
                        self.is_on_menu = False
                    elif self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and self.__posicao_botao[1] + 2 * self.__tamanho_botao[1] + 50 > mouse[1] > self.__posicao_botao[1] + self.__tamanho_botao[1] + 50:
                        pass
                    elif self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and self.__posicao_botao[1] + 3 * self.__tamanho_botao[1] + 100 > mouse[1] > self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50):
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()