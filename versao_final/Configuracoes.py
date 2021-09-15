import pygame

class Configuracoes:
    def __init__(self):
        self.__volume_jogo = 3
        self.__volume_maximo = 5
    
    def aumentar_volume(self):
        if self.__volume_jogo < self.__volume_maximo:
            self.__volume_jogo += 1
            pygame.mixer.music.set_volume(self.__volume_jogo/10)
    
    def diminuir_volume(self):
        if self.__volume_jogo > 0:
            self.__volume_jogo -= 1
            pygame.mixer.music.set_volume(self.__volume_jogo/10)

    @property
    def volume_jogo(self):
        return self.__volume_jogo
