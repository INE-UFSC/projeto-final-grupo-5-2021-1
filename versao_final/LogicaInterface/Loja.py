from Persistencia.LojaDao import LojaDAO
from Entidades.JogadorNave import Jogador
from Componentes.EfeitosSonoros import EfeitosSonoros
from Controladores.ControladorDinheiro import ControladorDinheiro
from Views.LojaView import InterfaceLoja
import pygame
import pygame_gui
import sys

class Loja:
    def __init__(self, jogador:Jogador):
        self.__jogador = jogador
        self.__view_loja = InterfaceLoja()
        self.__custo_escudo = 100
        self.__custo_dano = 100
        self.__maximo_compra_dano = 4
        self.__compra_dano = LojaDAO().get('compradano')
        self.__custo_velocidade = 100
        self.__maximo_compra_velocidade = 2
        self.__compra_velocidade = LojaDAO().get('compravelocidade')

    def comprar_escudo(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.vida += 25
        controlador_dinheiro.dinheiro -= self.__custo_escudo

    def aumentar_dano(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.dano += 5
        controlador_dinheiro.dinheiro -= self.__custo_dano

    def aumentar_velocidade(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.velocidade += 1
        controlador_dinheiro.dinheiro -= self.__custo_velocidade

    def compras_iniciais(self):
        self.__compra_dano = 0
        self.__compra_velocidade = 0

    def abrir_loja(self, controlador_dinheiro: ControladorDinheiro, efeitos_sonoros: EfeitosSonoros):
        efeitos_sonoros.pausar_musica()

        loja = True
        self.__view_loja.saldo_insuficiente = False
        self.__view_loja.compra_maxima = False

        while loja:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__view_loja.botao_dano:
                            if controlador_dinheiro.dinheiro >= self.__custo_dano:
                                if self.__maximo_compra_dano >= self.__compra_dano:
                                    self.__view_loja.compra_maxima = False
                                    self.__compra_dano += 1
                                    self.aumentar_dano(controlador_dinheiro)
                                else:
                                    self.__view_loja.compra_maxima = True
                            else:
                                self.__view_loja.saldo_insuficiente = True
                        elif event.ui_element == self.__view_loja.botao_velocidade:
                            if controlador_dinheiro.dinheiro >= self.__custo_velocidade:
                                if self.__maximo_compra_velocidade >= self.__compra_velocidade:
                                    self.__view_loja.compra_maxima = False
                                    self.__compra_velocidade += 1
                                    self.aumentar_velocidade(controlador_dinheiro)
                                else:
                                    self.__view_loja.compra_maxima = True
                            else:
                                self.__view_loja.saldo_insuficiente = True
                        elif event.ui_element == self.__view_loja.botao_vida:
                            self.__view_loja.compra_maxima = False
                            if controlador_dinheiro.dinheiro >= self.__custo_escudo:
                                self.comprar_escudo(controlador_dinheiro)
                            else:
                                self.__view_loja.saldo_insuficiente = True
                        elif event.ui_element == self.__view_loja.botao_continuar:
                            LojaDAO().salvar_variaveis(self.__compra_dano, self.__compra_velocidade)
                            efeitos_sonoros.despausar_musica()
                            loja = False

                self.__view_loja.ler_evento(event)
                self.__view_loja.window(controlador_dinheiro.dinheiro, self.__jogador)

            pygame.display.update()
