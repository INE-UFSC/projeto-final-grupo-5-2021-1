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
        self.atualizar(70)

    @property
    def botao_recomecar(self):
        return self.__botao_recomecar

    @property
    def botao_sair(self):
        return self.__botao_sair

    def textos(self, parametro1=None, parametro2=None):
        fonte_nome = pygame.font.SysFont('comicssans', 80)

        nome_jogo = fonte_nome.render("Fim de jogo!", True, (255,255,255))
        self.tela.janela.blit(nome_jogo, (self.tela.largura / 4 + 30, self.posicao_botao[1] - 100))

    def confirmacao(self):
        return pygame_gui.windows.UIConfirmationDialog(rect=pygame.Rect((self.tela.largura/2 - 100, self.tela.altura/2 - 50), (260, 200)), 
                                                manager=self.manager, action_long_desc='Deseja mesmo sair?', 
                                                window_title='Sair', action_short_name='Sim')
