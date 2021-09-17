from ConfiguracaoView import ConfiguracaoView
import pygame
import pygame_gui
import sys

class Configuracoes:
    def __init__(self):
        self.__volume_jogo = 3
        self.__volume_maximo = 5
        self.__view_configuracao = ConfiguracaoView()
    
    def aumentar_volume(self):
        if self.__volume_jogo < self.__volume_maximo:
            self.__volume_jogo += 1
            pygame.mixer.music.set_volume(self.__volume_jogo/10)
    
    def diminuir_volume(self):
        if self.__volume_jogo > 0:
            self.__volume_jogo -= 1
            pygame.mixer.music.set_volume(self.__volume_jogo/10)

    @property
    def volume_jogo(self):
        return self.__volume_jogo
 
    def configuracao(self):
        menu = True

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__view_configuracao.botao_diminuir:
                            self.diminuir_volume()
                        elif event.ui_element == self.__view_configuracao.botao_aumentar:
                            self.aumentar_volume()
                        elif event.ui_element == self.__view_configuracao.botao_continuar:
                            menu = False

                self.__view_configuracao.ler_evento(event)
                self.__view_configuracao.window(self.volume_jogo)

            pygame.display.update()
