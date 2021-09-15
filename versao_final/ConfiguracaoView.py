from Configuracoes import Configuracoes
from TelaJogo import TelaJogo
import pygame
import sys

class ConfiguracaoView:
    def __init__(self):
        self.__tela = TelaJogo()
        self.__configuracoes = Configuracoes()
        self.__imagem_som = pygame.transform.scale(pygame.image.load('volume.png'), (150,150))
    
    def mensagens(self):
        fonte_mensagem = pygame.font.SysFont('comicssans', 100)
        fonte_botao = pygame.font.SysFont('comicssans', 70)
        fonte_volume = pygame.font.SysFont('comicssans', 250)

        configuracao = fonte_mensagem.render("Configurações", True, (255,255,255))
        self.__tela.janela.blit(configuracao, (self.__tela.largura / 5, 50))

        botao_iniciar = fonte_botao.render("Voltar", True, (0,0,0))
        self.__tela.janela.blit(botao_iniciar, ((self.__tela.largura / 2) - 80, self.__tela.altura - 100))

        volume = '-' * self.__configuracoes.volume_jogo
        qtd_volume = fonte_volume.render(volume, True, (255,255,255))
        self.__tela.janela.blit(qtd_volume, (220, (self.__tela.altura/2) - 110))
    
    def botoes(self):
        pygame.draw.rect(self.__tela.janela, (0,0,0), [50, (self.__tela.altura/2) + 80, 60, 20])
        pygame.draw.rect(self.__tela.janela, (0,0,0), [130, (self.__tela.altura/2) + 80, 60, 20])
        pygame.draw.rect(self.__tela.janela, (0,0,0), [150, (self.__tela.altura/2) + 60, 20, 60])

        pygame.draw.rect(self.__tela.janela, (128,128,128), [(self.__tela.largura / 4) - 80, self.__tela.altura - 120, self.__tela.largura - 250, 80])

    def rodar(self):
        menu = True

        while menu:
            mouse = pygame.mouse.get_pos()

            self.__tela.mostrar_fundo()
            self.__tela.janela.blit(self.__imagem_som, (50, (self.__tela.altura/2) - 100))
            self.botoes()
            self.mensagens()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 110 > mouse[0] > 60 and (self.__tela.altura/2) + 100 > mouse[1] > (self.__tela.altura/2) + 80:
                        self.__configuracoes.diminuir_volume()                    
                    elif 190 > mouse[0] > 130 and (self.__tela.altura/2) + 120 > mouse[1] > (self.__tela.altura/2) + 60:
                        self.__configuracoes.aumentar_volume()
                    elif ((self.__tela.largura / 4) - 80 + self.__tela.largura - 250) > mouse[0] > (self.__tela.largura / 4) - 80 and self.__tela.altura - 40 > mouse[1] > self.__tela.altura - 120:
                        menu = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
