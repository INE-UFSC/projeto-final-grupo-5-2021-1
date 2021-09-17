from Configuracoes import Configuracoes
from VariaveisDao import VariaveisDAO
from Menu import MenuJogo
from TelaJogo import TelaJogo
from ControladorEstadoNivel import ControladorEstadoNivel
from ControladorElementosNivel import ControladorElementosNivel
# from Inimigo import Inimigo
import pygame
import random
import sys
from HUD import HUD
from JogadorNave import Jogador
# from Inimigo import *
from Sprites import *
from ControladorDinheiro import ControladorDinheiro
from Loja import *
from LojaView import InterfaceLoja


class Jogo:
    def __init__(self):
        self.variaveis = VariaveisDAO()
        self.tempo_fase = 0
        self.tempo_maximo = 240
        self.FPS = 60
        self.tempo = pygame.time.Clock()
        self.hud = HUD()
        self.tela = TelaJogo()
        self.jogador = Jogador()
        self.controle = ControladorEstadoNivel()
        self.controle_elementos = ControladorElementosNivel(self.variaveis)
        self.controle_dinheiro = ControladorDinheiro()
        self.loja = Loja(self.jogador)
        self.interface_loja = InterfaceLoja()
        self.configuracoes = Configuracoes()

    def elementos_tela(self):
        self.tela.mostrar_fundo()
        self.hud.mostrar_nivel(self.controle_elementos.nivel)
        self.hud.mostrar_vida(self.jogador)
        self.hud.mostrar_inimigos_restantes(len(sprites.inimigos))
        self.hud.mostrar_tempo(self.tempo_maximo, self.tempo_fase)
        self.hud.mostrar_dinheiro_jogador(self.controle_dinheiro.dinheiro)

        sprites.jogador.draw(surface=self.tela.janela)
        sprites.jogador.sprite.tiros.draw(self.tela.janela)
   
    def loop_jogo(self):
        if MenuJogo().menu(self.configuracoes) == 'recomecar':
            self.controle_elementos.nivel = 0
            self.jogador.vida = 100
            self.jogador.rect = Jogador().posicao

        pygame.mixer.music.load("trilhasonora.wav")
        pygame.mixer.music.set_volume(self.configuracoes.volume_jogo)
        pygame.mixer.music.play(-1)
   
        while True:
            self.tempo.tick(self.FPS)
            self.elementos_tela()
            sprites.jogador.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        if self.controle.pausar(self.configuracoes) == 'menu':
                            self.controle_elementos.nivel = self.variaveis.get('nivel')
                            self.jogador.vida = self.variaveis.get('vida')
                            self.jogador.rect.center = (self.tela.largura/2, self.tela.altura - 100)
                            self.jogador.tiros.empty()
                            sprites.inimigos.empty()
                            self.loop_jogo()
                if event.type == pygame.QUIT:
                    sys.exit()

            self.controle_elementos.geracao_inimigos(self.tela.largura)
            self.controle_elementos.comportamento_inimigos(self.tela.janela, self.tela.altura,self.jogador, self.FPS)
            self.controle_elementos.colisoes(self.jogador, self.controle_dinheiro)
            self.tempo_fase += 1 / self.FPS
            self.controle_dinheiro.gerar_recompensa()
            self.interface_loja.abrir_interface_loja(self.loja, self.controle_dinheiro)

            if len(sprites.inimigos) == 0:
                self.tempo_fase = 0
                if self.controle_elementos.nivel != 0:
                    self.controle.proxima_rodada(self.variaveis, self.controle_elementos.nivel, self.jogador.vida, self.jogador.escudo)
        
            if self.tempo_fase >= self.tempo_maximo or self.jogador.vida <= 0:
                self.controle_elementos.nivel = 0
                self.jogador.tiros.empty()
                sprites.inimigos.empty()
                self.tempo_fase = 0
                self.controle_dinheiro.zerar_dinheiro()
                self.controle.fim_de_jogo(self.jogador, self.tela)

            pygame.display.update()


jogo1 = Jogo()
jogo1.loop_jogo()
