from View import View
import pygame
import pygame_gui


class MenuView(View):
    def __init__(self):
        super().__init__()
        self.__botao_iniciar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.posicao_botao, self.tamanho_botao),
                                            text='Iniciar',
                                            manager=self.manager)
        self.__botao_continuar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + self.tamanho_botao[1] + 20), self.tamanho_botao),
                                            text='Continuar',
                                            manager=self.manager)
        self.__botao_configurar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + 2*(self.tamanho_botao[1] + 20)), self.tamanho_botao),
                                            text='Configuração',
                                            manager=self.manager)
        self.__botao_sair = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + 3*(self.tamanho_botao[1] + 20)), self.tamanho_botao),
                                            text='Sair',
                                            manager=self.manager)

        self.botoes = [self.__botao_iniciar, self.__botao_continuar, self.__botao_configurar, self.__botao_sair]
        self.atualizar()

    @property
    def botao_iniciar(self):
        return self.__botao_iniciar

    @property
    def botao_continuar(self):
        return self.__botao_continuar

    @property
    def botao_configurar(self):
        return self.__botao_configurar

    @property
    def botao_sair(self):
        return self.__botao_sair

    def textos(self):
        fonte_nome = pygame.font.SysFont('comicssans', 100)

        nome_jogo = fonte_nome.render("*Nome do Jogo", True, (255,255,255))
        self.tela.janela.blit(nome_jogo, (self.tela.largura / 6, 10))
    
    def window(self):
        self.tela.mostrar_fundo()
        self.textos()
        super().window()