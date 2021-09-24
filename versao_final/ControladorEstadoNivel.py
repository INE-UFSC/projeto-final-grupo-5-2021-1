from AtributosDao import AtributosDAO
from ControladorDinheiro import ControladorDinheiro
from ControladorElementosNivel import ControladorElementosNivel
from ControladorMenu import ControladorMenu
from Sprites import *
from EfeitosSonoros import EfeitosSonoros
from Configuracoes import Configuracoes
from LojaDao import LojaDAO
from Loja import Loja
from AtributosDao import AtributosDAO
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

    def fim_de_jogo(self, jogador: Jogador, tela: TelaJogo, loja: Loja, efeito_sonoro: EfeitosSonoros, controle: ControladorElementosNivel, dinheiro: ControladorDinheiro):
        if isinstance(jogador, Jogador) and isinstance(tela, TelaJogo) and isinstance(loja, Loja) and isinstance(efeito_sonoro, EfeitosSonoros) \
            and isinstance(controle, ControladorElementosNivel) and isinstance(dinheiro, ControladorDinheiro):
            controle.nivel = 0
            jogador.tiros.empty()
            sprites.inimigos.empty()
            dinheiro.zerar_dinheiro()
            loja.compras_iniciais()
            jogador.atributos_iniciais()
            jogador.posicao_inicial()
            AtributosDAO().resetar_variaveis()
            LojaDAO().resetar_variaveis()

        efeito_sonoro.pausar_musica()
        efeito_sonoro.tocar_som(efeito_sonoro.som_morte)

        morreu = True

        while morreu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__view_fim_jogo.botao_recomecar:
                            efeito_sonoro.tocar_musica()
                            controle.explodir = False
                            controle.tempo = 0
                            morreu = False
                        elif event.ui_element == self.__view_fim_jogo.botao_sair:
                            self.__view_fim_jogo.confirmacao()
                    if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        pygame.quit()
                        sys.exit()

                self.__view_fim_jogo.ler_evento(event)
                self.__view_fim_jogo.window()

            pygame.display.update()

    def pausar(self, configuracoes: Configuracoes, efeito_sonoro: EfeitosSonoros, controle: ControladorElementosNivel, jogador: Jogador, sprite: Sprites):
        efeito_sonoro.pausar_musica()
   
        pausado = True
        
        if isinstance(configuracoes, Configuracoes) and isinstance(efeito_sonoro, EfeitosSonoros) and isinstance(controle, ControladorElementosNivel) and isinstance(jogador, Jogador):
            while pausado:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.__view_pausa.botao_continuar:
                                efeito_sonoro.despausar_musica()
                                pausado = False
                            elif event.ui_element == self.__view_pausa.botao_configurar:
                                try:
                                    configuracoes.configuracao(efeito_sonoro)
                                except AttributeError:
                                    print('Não possui esse método')
                            elif event.ui_element == self.__view_pausa.botao_menu:
                                ControladorMenu().voltar_menu(controle, jogador)
                                return 'menu'

                    self.__view_pausa.ler_evento(event)
                    self.__view_pausa.window()

                pygame.display.update()

    def proxima_rodada(self, dao: AtributosDAO, controle: ControladorElementosNivel, dinheiro: ControladorDinheiro, jogador: Jogador, loja: Loja, efeito_sonoro: EfeitosSonoros):
        if isinstance(dao, AtributosDAO) and isinstance(jogador, Jogador) and isinstance(controle, ControladorElementosNivel) and isinstance(dinheiro, ControladorDinheiro) \
            and isinstance(loja, Loja) and isinstance(efeito_sonoro, EfeitosSonoros):
            dao.salvar_variaveis(jogador.vida, jogador.dano, jogador.velocidade, dinheiro.dinheiro, controle.nivel)
            jogador.tiros.empty()
            if controle.nivel != 0:
                controle.explodir = False
                controle.tempo = 0
                loja.abrir_loja(dinheiro, efeito_sonoro)
                jogador.posicao_inicial()
