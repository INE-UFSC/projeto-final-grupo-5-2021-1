import pygame
import pygame_gui
from TelaJogo import TelaJogo
from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def __init__(self):
        self.__tela = TelaJogo()
        self.__manager = pygame_gui.UIManager((self.__tela.largura, self.__tela.altura))
        self.__posicao_botao = ((self.tela.largura / 4) - 80, 150)
        self.__tamanho_botao = ((self.tela.largura - 250, 80))
        self.__botoes = []

    def atualizar(self):
        for botao in self.__botoes:
            try:
                botao.font = pygame.font.SysFont('comicssans', 70)
                botao.rebuild()
            except AttributeError:
                print('Não possui esse método')

    def window(self):
        self.__manager.update(pygame.time.Clock().tick(60))
        self.__manager.draw_ui(self.__tela.janela)

    def ler_evento(self, evento):
        return self.__manager.process_events(evento)

    @property
    def tela(self):
        return self.__tela
    
    @property
    def manager(self):
        return self.__manager
    
    @property
    def posicao_botao(self):
        return self.__posicao_botao
    
    @posicao_botao.setter
    def posicao_botao(self, posicao):
        self.__posicao_botao = posicao
    
    @property
    def tamanho_botao(self):
        return self.__tamanho_botao
    
    @tamanho_botao.setter
    def tamanho_botao(self, tamanho):
        self.__tamanho_botao = tamanho

    @property
    def botoes(self):
        return self.__botoes
    
    @botoes.setter
    def botoes(self, botao):
        self.__botoes = botao