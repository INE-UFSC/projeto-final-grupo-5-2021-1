import pygame


class EfeitosSonoros:
    def __init__(self):
        self.som_disparo = pygame.mixer.Sound("ataque.wav")
        self.som_explosao = pygame.mixer.Sound("explosao.wav")
        self.som_morte = pygame.mixer.Sound("morte.wav")

        self.__sons = [self.som_disparo, self.som_explosao, self.som_morte]

    @property
    def sons(self):
        return self.__sons
    
    def carregar_musica(self, musica):
        try:
            pygame.mixer.music.load(musica)
        except Exception as e:
            print('Erro: ', e)
    
    def tocar_musica(self):
        try:
            pygame.mixer.music.play(-1)
        except FileNotFoundError:
            print('Arquivo de música não encontrado')
    
    def pausar_musica(self):
        try:
            pygame.mixer.music.pause()
        except FileNotFoundError:
            print('Arquivo de música não encontrado')
    
    def despausar_musica(self):
        try:
            pygame.mixer.music.unpause()
        except FileNotFoundError:
            print('Arquivo de música não encontrado')
    
    def tocar_som(self, efeito_sonoro):
        try:
            pygame.mixer.Sound.play(efeito_sonoro)
        except FileNotFoundError:
            print('Arquivo de som não encontrado')