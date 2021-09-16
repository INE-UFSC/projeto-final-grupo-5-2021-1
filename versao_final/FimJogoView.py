from View import View
import pygame
import pygame_gui


class FimJogoView(View):
    def __init__(self):
        super().__init__()
        self.posicao_botao = ((self.tela.largura / 4) - 80, self.tela.altura/2 - 60)

        self.__botao_recomecar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.posicao_botao, self.tamanho_botao),
                                            text='Recomeçar',
                                            manager=self.manager)
        self.__botao_sair = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + self.tamanho_botao[1] + 20), self.tamanho_botao),
                                            text='Sair',
                                            manager=self.manager) 

        self.botoes = [self.__botao_recomecar, self.__botao_sair]
        self.atualizar()

    @property
    def botao_recomecar(self):
        return self.__botao_recomecar

    @property
    def botao_sair(self):
        return self.__botao_sair
