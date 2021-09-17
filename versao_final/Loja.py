from JogadorNave import Jogador
from ControladorDinheiro import ControladorDinheiro

class Loja:
    #valores de dinheiro do jogador podem e devem ser alterados
    def __init__(self, jogador:Jogador):
        self.__jogador = jogador

    def comprar_escudo(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.vida += 25
        controlador_dinheiro.dinheiro = -100

    def aumentar_dano(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.dano += 15
        controlador_dinheiro.dinheiro = -100

    def aumentar_velocidade(self, controlador_dinheiro: ControladorDinheiro):
        self.__jogador.velocidade += 10
        controlador_dinheiro.dinheiro = -100




