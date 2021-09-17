from VariaveisDao import VariaveisDAO
from Configuracoes import Configuracoes
from TelaJogo import TelaJogo
from JogadorNave import Jogador
import pygame
from pygame.locals import *
import pygame_gui
import sys
from FimJogoView import FimJogoView
from PausaView import PausaView


class ControladorEstadoNivel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__view_fim_jogo = FimJogoView()
        self.__view_pausa = PausaView()

    def fim_de_jogo(self, jogador: Jogador, tela: TelaJogo):
        if isinstance(jogador, Jogador) and isinstance(tela, TelaJogo):
            VariaveisDAO().add('nivel', 0)
            VariaveisDAO().add('vida', 100)
            jogador.vida = 100
            jogador.rect.center = (tela.largura/2, tela.altura - 100)

        pygame.mixer.music.pause()

        morreu = True

        while morreu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__view_fim_jogo.botao_recomecar:
                            pygame.mixer.music.play(-1)
                            morreu = False
                        elif event.ui_element == self.__view_fim_jogo.botao_sair:
                            pygame.quit()
                            sys.exit()

                self.__view_fim_jogo.ler_evento(event)
                self.__view_fim_jogo.window()

            pygame.display.update()

    def pausar(self, configuracoes: Configuracoes):
        pygame.mixer.music.pause()
   
        pausado = True

        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__view_pausa.botao_continuar:
                            pygame.mixer.music.unpause()
                            pausado = False
                        elif event.ui_element == self.__view_pausa.botao_configurar:
                            try:
                                configuracoes.configuracao()
                            except AttributeError:
                                print('Não possui esse método')
                        elif event.ui_element == self.__view_pausa.botao_menu:
                            return 'menu'

                self.__view_pausa.ler_evento(event)
                self.__view_pausa.window()

            pygame.display.update()

    def proxima_rodada(self, dao: VariaveisDAO(), nivel: int, vida: int, escudo: int):
        if isinstance(dao, VariaveisDAO):
            dao.add('nivel', nivel)
            if dao.get('vida') != vida:
                dao.add('vida', vida)
            if dao.get('escudo') != escudo:
                dao.add('escudo', escudo)
  
