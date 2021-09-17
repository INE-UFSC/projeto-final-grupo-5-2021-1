from View import View
import pygame
import pygame_gui


class PausaView(View):
    def __init__(self):
        super().__init__()
        self.__botao_continuar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.posicao_botao, self.tamanho_botao),
                                            text='Continuar',
                                            manager=self.manager)
        self.__botao_configurar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + self.tamanho_botao[1] + 20), self.tamanho_botao),
                                            text='Configuração',
                                            manager=self.manager)
        self.__botao_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + 2*(self.tamanho_botao[1] + 20)), self.tamanho_botao),
                                            text='Menu',
                                            manager=self.manager)

        self.botoes = [self.__botao_continuar, self.__botao_configurar, self.__botao_menu]
        self.atualizar(70)

    @property
    def botao_continuar(self):
        return self.__botao_continuar

    @property
    def botao_configurar(self):
        return self.__botao_configurar

    @property
    def botao_menu(self):
        return self.__botao_menu
  
