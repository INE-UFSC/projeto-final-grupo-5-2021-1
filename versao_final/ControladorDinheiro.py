from Sprites import *


class ControladorDinheiro:
    def __init__(self):
        self.__dinheiro_jogador = 0

    @property
    def dinheiro(self):
        return self.__dinheiro_jogador
    @dinheiro.setter
    def dinheiro(self, dinheiro):
        self.__dinheiro_jogador += dinheiro

    def zerar_dinheiro(self):
        self.__dinheiro_jogador = 0

    def gerar_recompensa(self):
        if len(sprites.inimigos) == 0:
            self.__dinheiro_jogador += 10