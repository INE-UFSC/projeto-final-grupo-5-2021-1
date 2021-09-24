from TelaJogo import TelaJogo
import pygame
from JogadorNave import Jogador


class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.font.init()
        self.__fonte_letreiros = pygame.font.SysFont('comicssans', 25)
        self.__tela = TelaJogo()

    def mostrar_nivel(self, nivel: int):
        nivel_atual_display = self.__fonte_letreiros.render("Nível: {}".format(nivel), True, (255, 255, 255))
        return self.__tela.janela.blit(nivel_atual_display, (self.__tela.largura - 80, 10))

    def mostrar_vida(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            vida_display = self.__fonte_letreiros.render("Vida: " + str(jogador.vida), True, (255, 0, 0))
            return self.__tela.janela.blit(vida_display, (0, 10))

    def mostrar_tempo(self, tempo: int):
        tempo_display = self.__fonte_letreiros.render("Tempo: " + str(int(tempo)), True,
                                                      (255, 255, 255))
        return self.__tela.janela.blit(tempo_display, (100, 10))

    def mostrar_inimigos_restantes(self, qtd_inimigos: str):
        inimigos_display = self.__fonte_letreiros.render("Inimigos: " + str(qtd_inimigos), True, (255, 255, 255))
        return self.__tela.janela.blit(inimigos_display, (220, 10))

    def mostrar_dinheiro_jogador(self, dinheiro_jogador):
        dinheiro_jogador_display = self.__fonte_letreiros.render('Dinheiro: $' + str(dinheiro_jogador), True, (255,255,255))
        return self.__tela.janela.blit(dinheiro_jogador_display, (0,30))
