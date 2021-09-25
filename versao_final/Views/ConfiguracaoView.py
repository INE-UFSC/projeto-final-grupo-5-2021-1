from Views.View import View
import pygame
import pygame_gui


class ConfiguracaoView(View):
    def __init__(self):
        super().__init__()
        self.__botao_continuar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.tela.altura - self.tamanho_botao[1] - 20), self.tamanho_botao),
                                            text='Continuar',
                                            manager=self.manager)

        self.posicao_botao = (50, self.tela.altura/2 + 60)
        self.tamanho_botao = (50, 50)

        self.__botao_diminuir = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.posicao_botao, self.tamanho_botao),
                                            text='-',
                                            manager=self.manager)
        self.__botao_aumentar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0] + self.tamanho_botao[0] + 10, self.posicao_botao[1]), self.tamanho_botao),
                                            text='+',
                                            manager=self.manager) 

        self.botoes = [self.__botao_diminuir, self.__botao_aumentar, self.__botao_continuar]
        self.atualizar(70)

        self.__imagem_som = pygame.transform.scale(pygame.image.load('Imagens/volume.png'), (150,150))
        self.__fonte_mensagem = pygame.font.SysFont('comicssans', 100)
        self.__fonte_volume = pygame.font.SysFont('comicssans', 250)

    @property
    def botao_diminuir(self):
        return self.__botao_diminuir

    @property
    def botao_aumentar(self):
        return self.__botao_aumentar

    @property
    def botao_continuar(self):
        return self.__botao_continuar

    def textos(self, total_volume: int, parametro2=None):
        configuracao = self.__fonte_mensagem.render("Configurações", True, (255,255,255))
        self.tela.janela.blit(configuracao, (self.tela.largura / 5, 50))

        volume = '-' * total_volume
        qtd_volume = self.__fonte_volume.render(volume, True, (255,255,255))
        self.tela.janela.blit(qtd_volume, (220, (self.tela.altura/2) - 110))
    
    def window(self, volume: int):
        super().window(volume)
        self.tela.janela.blit(self.__imagem_som, (50, (self.tela.altura/2) - 100))
