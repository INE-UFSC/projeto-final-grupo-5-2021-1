import pygame


class TelaJogo:
    def __init__(self):
        self.__largura = 800
        self.__altura = 600
        self.__janela = pygame.display.set_mode((self.__largura, self.__altura))
        self.fundo_tela = pygame.transform.scale(pygame.image.load('Imagens/space_background.jpg'), (self.__largura, self.__altura))

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, largura):
        self.__largura = largura
    
    @property
    def janela(self):
        return self.__janela
    
    def mostrar_fundo(self):
        return self.janela.blit(self.fundo_tela, (0, 0))
