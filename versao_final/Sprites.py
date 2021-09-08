import pygame


class Sprites:
    def __init__(self):
        self.__jogador = pygame.sprite.GroupSingle()
        self.__inimigos = pygame.sprite.Group()
        self.__tiros = pygame.sprite.Group()
    
    @property
    def jogador(self):
        return self.__jogador

    @property
    def inimigos(self):
        return self.__inimigos
    
    @property
    def tiros(self):
        return self.__tiros

sprites = Sprites()