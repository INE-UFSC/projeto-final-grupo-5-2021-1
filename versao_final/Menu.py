from AtributosDao import AtributosDAO
from Loja import Loja
from ControladorDinheiro import ControladorDinheiro
from JogadorNave import Jogador
from ControladorElementosNivel import ControladorElementosNivel
from ControladorMenu import ControladorMenu
from EfeitosSonoros import EfeitosSonoros
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
    
    def menu(self, configuracoes: Configuracoes, efeitos_sonoros: EfeitosSonoros, controle: ControladorElementosNivel, jogador: Jogador, loja: Loja, dinheiro: ControladorDinheiro):
        if isinstance(configuracoes, Configuracoes) and isinstance(efeitos_sonoros, EfeitosSonoros) and isinstance(controle, ControladorElementosNivel) \
            and isinstance(jogador, Jogador) and isinstance(loja, Loja) and isinstance(dinheiro, ControladorDinheiro):
            while self.is_on_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.__view_menu.botao_iniciar:
                                self.is_on_menu = False
                                ControladorMenu().recomecar(controle, jogador, loja, dinheiro)
                                AtributosDAO().resetar_variaveis()
                            elif event.ui_element == self.__view_menu.botao_continuar:
                                self.is_on_menu = False
                            elif event.ui_element == self.__view_menu.botao_configurar:
                                try:
                                    configuracoes.configuracao(efeitos_sonoros)
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
   
