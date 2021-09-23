from MenuView import MenuView
from Configuracoes import Configuracoes
import pygame
import pygame_gui
import sys
from TelaJogo import TelaJogo


class MenuJogo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tela = TelaJogo()
        self.is_on_menu = True
        self.__view_menu = MenuView()
    
    def menu(self, configuracoes: Configuracoes):
        while self.is_on_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__view_menu.botao_iniciar:
                            self.is_on_menu = False
                            return 'recomecar'
                        elif event.ui_element == self.__view_menu.botao_continuar:
                            self.is_on_menu = False
                        elif event.ui_element == self.__view_menu.botao_configurar:
                            try:
                                configuracoes.configuracao()
                            except AttributeError:
                                print('Não possui esse método')
                        elif event.ui_element == self.__view_menu.botao_sair:
                            self.__view_menu.confirmacao()
                    if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        pygame.quit()
                        sys.exit()

                self.__view_menu.ler_evento(event)
                self.__view_menu.window()

            pygame.display.update()
   
