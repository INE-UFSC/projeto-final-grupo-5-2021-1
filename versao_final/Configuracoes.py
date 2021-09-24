from ConfiguracaoView import ConfiguracaoView
from EfeitosSonoros import EfeitosSonoros
import pygame
import pygame_gui
import sys

class Configuracoes:
    def __init__(self):
        self.__volume_jogo = 3
        self.__volume_maximo = 5
        self.__view_configuracao = ConfiguracaoView()
    
    def aumentar_volume(self, efeito_sonoro: EfeitosSonoros):
        if self.__volume_jogo < self.__volume_maximo:
            self.__volume_jogo += 1
            pygame.mixer.music.set_volume(self.__volume_jogo/10)
            
            if isinstance(efeito_sonoro, EfeitosSonoros):
                for som in efeito_sonoro.sons:
                    som.set_volume(self.__volume_jogo/10)
    
    def diminuir_volume(self, efeito_sonoro: EfeitosSonoros):
        if self.__volume_jogo > 0:
            self.__volume_jogo -= 1
            pygame.mixer.music.set_volume(self.__volume_jogo/10)
            
            if isinstance(efeito_sonoro, EfeitosSonoros):
                for som in efeito_sonoro.sons:
                    som.set_volume(self.__volume_jogo/10)

    @property
    def volume_jogo(self):
        return self.__volume_jogo
 
    def configuracao(self, efeito_sonoro: EfeitosSonoros):
        menu = True
        
        if isinstance(efeito_sonoro, EfeitosSonoros):
            while menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.__view_configuracao.botao_diminuir:
                                self.diminuir_volume(efeito_sonoro)
                            elif event.ui_element == self.__view_configuracao.botao_aumentar:
                                self.aumentar_volume(efeito_sonoro)
                            elif event.ui_element == self.__view_configuracao.botao_continuar:
                                menu = False

                    self.__view_configuracao.ler_evento(event)
                    self.__view_configuracao.window(self.volume_jogo)

                pygame.display.update()
