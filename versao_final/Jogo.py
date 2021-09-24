from EfeitosSonoros import EfeitosSonoros
from Configuracoes import Configuracoes
from AtributosDao import AtributosDAO
from Menu import MenuJogo
from TelaJogo import TelaJogo
from ControladorEstadoNivel import ControladorEstadoNivel
from ControladorElementosNivel import ControladorElementosNivel
import pygame
import sys
from HUD import HUD
from JogadorNave import Jogador
from Sprites import *
from ControladorDinheiro import ControladorDinheiro
from Loja import Loja


pygame.init()
pygame.display.set_caption('Space Conqueror')

class Jogo:
    def __init__(self):
        self.atributos = AtributosDAO()
        self.tempo_fase = 0
        self.tempo_maximo = 240
        self.FPS = 60
        self.tempo = pygame.time.Clock()
        self.hud = HUD()
        self.tela = TelaJogo()
        self.jogador = Jogador()
        self.controle = ControladorEstadoNivel()
        self.controle_elementos = ControladorElementosNivel(self.atributos, self.controle_dinheiro)
        self.controle_dinheiro = ControladorDinheiro()
        self.loja = Loja(self.jogador)
        self.configuracoes = Configuracoes()
        self.efeitos_sonoros = EfeitosSonoros()

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
        MenuJogo().menu(self.configuracoes, self.efeitos_sonoros, self.controle_elementos, self.jogador, self.loja, self.controle_dinheiro)

        self.efeitos_sonoros.carregar_musica("trilhasonora.wav")
        
        pygame.mixer.music.set_volume(self.configuracoes.volume_jogo/10)
        for som in self.efeitos_sonoros.sons:
            som.set_volume(self.configuracoes.volume_jogo/10)

        self.efeitos_sonoros.tocar_musica()
   
        while True:
            self.tempo.tick(self.FPS)
            self.elementos_tela()
            self.controle_elementos.explosao(self.tela.janela)
            sprites.jogador.update(self.efeitos_sonoros)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        if self.controle.pausar(self.configuracoes, self.efeitos_sonoros, self.controle_elementos, self.jogador) == 'menu':
                            self.loop_jogo()
                if event.type == pygame.QUIT:
                    sys.exit()

            self.controle_elementos.geracao_inimigos(self.tela.largura)
            self.controle_elementos.comportamento_inimigos(self.tela.janela, self.tela.altura,self.jogador, self.FPS)
            self.controle_elementos.colisoes(self.jogador, self.efeitos_sonoros)
            self.tempo_fase += 1 / self.FPS
            self.controle_dinheiro.gerar_recompensa()

            if self.tempo_fase >= self.tempo_maximo or self.jogador.vida <= 0:
                self.tempo_fase = 0
                self.controle.fim_de_jogo(self.jogador, self.tela, self.loja, self.efeitos_sonoros, self.controle_elementos, self.controle_dinheiro)

            if len(sprites.inimigos) == 0:
                self.tempo_fase = 0
                self.controle.proxima_rodada(self.variaveis, self.controle_elementos, self.controle_dinheiro, self.jogador, self.loja, self.efeitos_sonoros)

            pygame.display.update()


jogo1 = Jogo()
jogo1.loop_jogo()
