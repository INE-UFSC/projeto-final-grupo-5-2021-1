from Menu import MenuJogo
from TelaJogo import TelaJogo
from Controlador import ControladorNivel
#from Inimigo import Inimigo
import pygame
import random
import sys
from HUD import HUD
from JogadorNave import Jogador
from Inimigo import *
from Sprites import *


class Jogo:
    def __init__(self):
        self.tempo_fase = 0
        self.tempo_maximo = 240
        self.nivel = 0
        self.FPS = 60
        self.tempo = pygame.time.Clock()
        self.hud = HUD()
        self.tela = TelaJogo()
        self.jogador = Jogador()
        self.controle = ControladorNivel()

    def elementos_tela(self):
        self.tela.mostrar_fundo()
        self.hud.mostrar_nivel(self.nivel)
        self.hud.mostrar_vida(self.jogador)
        self.hud.mostrar_inimigos_restantes(len(sprites.inimigos))
        self.hud.mostrar_tempo(self.tempo_maximo, self.tempo_fase)

        sprites.jogador.draw(surface=self.tela.janela)
        sprites.jogador.sprite.tiros.draw(self.tela.janela)
    
    def colisoes(self):
        for inimigo_acertado in self.jogador.colisao(sprites.inimigos, self.jogador.tiros):
            inimigo_acertado.vida -= sprites.jogador.sprite.dano
            if inimigo_acertado.vida == 0:
                sprites.inimigos.remove(inimigo_acertado)

        for inimigo_colidido in self.jogador.colisao(sprites.jogador, sprites.inimigos).values():
            if isinstance(inimigo_colidido[0], Kamikaze):
                inimigo_colidido[0].explodir(self.jogador)
                self.jogador.vida -= inimigo_colidido[0].dano_explosao
            elif isinstance(inimigo_colidido[0], NaveComum) or isinstance(inimigo_colidido[0], Meteoro):
                self.jogador.vida -= inimigo_colidido[0].dano * 2
    
    def geracao_inimigos(self):
        if len(sprites.inimigos) == 0:
            self.nivel += 1
            self.tempo_fase = 0
            for _ in range(0,(self.nivel*2)+3):
                escolha_inimigo = random.randint(1,3)
                if escolha_inimigo == 1:
                    novo_inimigo = NaveComum(self.tela.largura)
                elif escolha_inimigo == 2:
                    novo_inimigo = Kamikaze(self.tela.largura)
                else:
                    novo_inimigo = Meteoro()
                sprites.inimigos.add(novo_inimigo)

    def comportamento_inimigos(self):
        for inimigo in sprites.inimigos:
            inimigo.geracao(self.tela.janela)
            if isinstance(inimigo, Meteoro):
                inimigo.movimento(sprites.inimigos, self.tela.altura)
            else:
                inimigo.tiro_temporizador += 1/self.FPS
                if isinstance(inimigo, Kamikaze):
                    inimigo.movimento(sprites.inimigos, self.tela.altura)
                else:
                    inimigo.movimento()
                inimigo.disparar(self.tela.altura)
                inimigo.tiros.draw(self.tela.janela)
                inimigo.tiros.update()
                if self.jogador.colisao(sprites.jogador, inimigo.tiros):
                    sprites.jogador.sprite.vida -= inimigo.dano
                #Vale a pena replicar repetir uma parte do código p/ deixar draw em elementos_tela e a colisão dos tiros em colisoes?

    def loop_jogo(self):
        while True:
            self.tempo.tick(self.FPS)
            self.elementos_tela()
            sprites.jogador.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.controle.pausar()
                if event.type == pygame.QUIT:
                    sys.exit()

            self.geracao_inimigos()
            self.comportamento_inimigos()            
            self.colisoes()
            
            if self.tempo_fase >= self.tempo_maximo or self.jogador.vida <= 0:
                self.nivel = 0
                self.jogador.tiros.empty()
                sprites.inimigos.empty()
                self.controle.fim_de_jogo(self.jogador, self.tela)

            self.tempo_fase += 1/self.FPS 
            pygame.display.update()

jogo1 = Jogo()
menu = MenuJogo()
menu.menu()
jogo1.loop_jogo()