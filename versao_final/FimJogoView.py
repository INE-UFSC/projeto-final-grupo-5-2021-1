import pygame
#import pygame_gui
from TelaJogo import TelaJogo
import sys


class FimJogoView:
    def __init__(self):
        self.tela = TelaJogo()
        self.__tamanho_botao = (self.tela.largura - 250, 80)
        self.__posicao_botao = ((self.tela.largura / 4) - 80, 100)
    
    def mensagens(self):
        fonte_mensagem = pygame.font.SysFont('comicssans', 100)
        fonte_botao = pygame.font.SysFont('comicssans', 70)

        fim_jogo = fonte_mensagem.render("Você perdeu!", True, (255,255,255))
        self.tela.janela.blit(fim_jogo, (self.tela.largura / 5 + 10, 80))

        botao_configuracao = fonte_botao.render("Recomeçar", True, (0,0,0))
        self.tela.janela.blit(botao_configuracao, (self.__posicao_botao[0] + 140, self.__posicao_botao[1] + self.__tamanho_botao[1] + 65))

        botao_sair = fonte_botao.render("Sair", True, (0,0,0))
        self.tela.janela.blit(botao_sair, (self.__posicao_botao[0] + 220, self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50) + 15))
    
    def botoes(self):
        pygame.draw.rect(self.tela.janela, (0,255,0), [self.__posicao_botao[0], self.__posicao_botao[1] + self.__tamanho_botao[1] + 50, self.__tamanho_botao[0], self.__tamanho_botao[1]])
        pygame.draw.rect(self.tela.janela, (255,0,0), [self.__posicao_botao[0], self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50), self.__tamanho_botao[0], self.__tamanho_botao[1]])
    
    def rodar(self):
        self.botoes()
        self.mensagens()
        
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and self.__posicao_botao[1] + 2 * self.__tamanho_botao[1] + 50 > mouse[1] > self.__posicao_botao[1] + self.__tamanho_botao[1] + 50:
                    return False
                elif self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and self.__posicao_botao[1] + 3 * self.__tamanho_botao[1] + 100 > mouse[1] > self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()