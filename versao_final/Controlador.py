from TelaJogo import TelaJogo
from JogadorNave import Jogador
import pygame
from pygame.locals import *
import sys


class ControladorNivel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def fim_de_jogo(self, jogador: Jogador, tela: TelaJogo):
        if isinstance(jogador, Jogador) and isinstance(tela, TelaJogo):
            jogador.vida = 100
            jogador.rect.center = (tela.largura/2, tela.altura - 100)
        
        fonte_letreiros = pygame.font.SysFont('comicssans',100)
        fim_jogo = fonte_letreiros.render("Fim de jogo", True, (255,255,255))
        tela.janela.blit(fim_jogo, (tela.largura/4, tela.altura/2))

        morreu = True

        while morreu:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    morreu = False
                if event.type == pygame.QUIT:
                    sys.exit()

    def pausar(self):
        self.is_pausado = True

        while self.is_pausado:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                            self.is_pausado = False
                if event.type == pygame.QUIT:
                    sys.exit()