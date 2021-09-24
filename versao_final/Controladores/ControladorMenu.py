from Componentes.Sprites import *
from Persistencia.AtributosDao import AtributosDAO
from Controladores.ControladorDinheiro import ControladorDinheiro
from LogicaInterface.Loja import Loja
from Entidades.JogadorNave import Jogador
from Controladores.ControladorElementosNivel import ControladorElementosNivel


class ControladorMenu:
    def __init__(self):
        pass

    def recomecar(self, controle: ControladorElementosNivel, jogador: Jogador, loja: Loja, dinheiro: ControladorDinheiro):
        if isinstance(controle, ControladorElementosNivel) and isinstance(jogador, Jogador) and isinstance(loja, Loja) and isinstance(dinheiro, ControladorDinheiro):
            controle.nivel = 0
            controle.explodir = False
            controle.tempo = 0
            jogador.atributos_iniciais()
            jogador.posicao_inicial()
            loja.compras_iniciais()
            dinheiro.zerar_dinheiro()

    def voltar_menu(self, controle: ControladorElementosNivel, jogador: Jogador):
        if isinstance(controle, ControladorElementosNivel) and isinstance(jogador, Jogador):
            controle.nivel = AtributosDAO().get('nivel')
            controle.explodir = False
            controle.tempo = 0
            jogador.posicao_inicial()
            jogador.tiros.empty()
            sprites.inimigos.empty()
