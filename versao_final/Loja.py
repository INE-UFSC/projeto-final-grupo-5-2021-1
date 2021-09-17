from VariaveisDao import VariaveisDAO
from JogadorNave import Jogador
from ControladorDinheiro import ControladorDinheiro
from LojaView import InterfaceLoja
import pygame
import pygame_gui
import sys

class Loja:
    #valores de dinheiro do jogador podem e devem ser alterados
    def __init__(self, jogador:Jogador):
        self.__jogador = jogador
        self.__view_loja = InterfaceLoja()
        self.__custo_escudo = 100
        self.__custo_dano = 100
        self.__custo_velocidade = 100

    def comprar_escudo(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.vida += 25
        controlador_dinheiro.dinheiro -= self.__custo_escudo

    def aumentar_dano(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.dano += 15
        controlador_dinheiro.dinheiro -= self.__custo_dano

    def aumentar_velocidade(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.velocidade += 10
        controlador_dinheiro.dinheiro -= self.__custo_velocidade

    def abrir_loja(self, controlador_dinheiro: ControladorDinheiro):
        loja = True
        self.__view_loja.saldo_insuficiente = False

        while loja:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__view_loja.botao_dano:
                            if controlador_dinheiro.dinheiro >= self.__custo_dano:
                                self.aumentar_dano(controlador_dinheiro)
                                VariaveisDAO().add('dano', self.__jogador.dano)
                            else:
                                self.__view_loja.saldo_insuficiente = True
                        elif event.ui_element == self.__view_loja.botao_velocidade:
                            if controlador_dinheiro.dinheiro >= self.__custo_velocidade:
                                self.aumentar_velocidade(controlador_dinheiro)
                                VariaveisDAO().add('valocidade', self.__jogador.velocidade)
                            else:
                                self.__view_loja.saldo_insuficiente = True
                        elif event.ui_element == self.__view_loja.botao_vida:
                            if controlador_dinheiro.dinheiro >= self.__custo_escudo:
                                self.comprar_escudo(controlador_dinheiro)
                                VariaveisDAO().add('vida', self.__jogador.vida)
                            else:
                                self.__view_loja.saldo_insuficiente = True
                        elif event.ui_element == self.__view_loja.botao_continuar:
                            loja = False

                self.__view_loja.ler_evento(event)
                self.__view_loja.window(controlador_dinheiro.dinheiro, self.__jogador)

            pygame.display.update()
