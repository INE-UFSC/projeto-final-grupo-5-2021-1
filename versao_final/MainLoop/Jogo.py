from Componentes.EfeitosSonoros import EfeitosSonoros
from LogicaInterface.Configuracoes import Configuracoes
from Persistencia.AtributosDao import AtributosDAO
from LogicaInterface.Menu import MenuJogo
from Componentes.TelaJogo import TelaJogo
from Controladores.ControladorEstadoNivel import ControladorEstadoNivel
from Controladores.ControladorElementosNivel import ControladorElementosNivel
import pygame
import sys
from Componentes.HUD import HUD
from Entidades.JogadorNave import Jogador
from Componentes.Sprites import *
from Controladores.ControladorDinheiro import ControladorDinheiro
from LogicaInterface.Loja import Loja


pygame.init()
pygame.display.set_caption('Space Conqueror')
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('Imagens/Ship_Player_PNG_01.png'), (10,10)))

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
        self.controle_dinheiro = ControladorDinheiro()
        self.controle_elementos = ControladorElementosNivel(self.atributos, self.controle_dinheiro)
        self.loja = Loja(self.jogador)
        self.configuracoes = Configuracoes()
        self.efeitos_sonoros = EfeitosSonoros()
   
    def loop_jogo(self):
        MenuJogo().menu(self.configuracoes, self.efeitos_sonoros, self.controle_elementos, self.jogador, self.loja, self.controle_dinheiro)

        self.efeitos_sonoros.carregar_musica("Sons/trilhasonora.wav")
        
        pygame.mixer.music.set_volume(self.configuracoes.volume_jogo/10)
        for som in self.efeitos_sonoros.sons:
            som.set_volume(self.configuracoes.volume_jogo/10)

        self.efeitos_sonoros.tocar_musica()
   
        while True:
            self.tempo.tick(self.FPS)
            self.controle_elementos.elementos_tela(self.tela, self.hud, self.jogador, self.controle_dinheiro, self.tempo_maximo - self.tempo_fase, self.FPS)
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
            self.controle_elementos.comportamento_inimigos(self.tela)
            self.controle_elementos.colisoes(self.jogador, self.efeitos_sonoros)
            self.tempo_fase += 1 / self.FPS
            self.controle_dinheiro.gerar_recompensa()

            if self.tempo_fase >= self.tempo_maximo or self.jogador.vida <= 0:
                self.tempo_fase = 0
                self.controle.fim_de_jogo(self.jogador, self.tela, self.loja, self.efeitos_sonoros, self.controle_elementos, self.controle_dinheiro)

            if len(sprites.inimigos) == 0:
                self.tempo_fase = 0
                self.controle.proxima_rodada(self.atributos, self.controle_elementos, self.controle_dinheiro, self.jogador, self.loja, self.efeitos_sonoros)

            pygame.display.update()


jogo1 = Jogo()
jogo1.loop_jogo()
