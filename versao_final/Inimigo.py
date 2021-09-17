import pygame
from pygame.locals import *
from abc import ABC, abstractmethod
import random
from Tiro import Tiro
from Sprites import Sprites


class Inimigo(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.__velocidade = 5
        self.__dano = 5
        self.__vida = 50
        self.__image = pygame.transform.scale(pygame.image.load("nave_inimiga.png"), (80,80))
        self.__rect = self.__image.get_rect()
        self.mask = pygame.mask.from_surface(self.__image)
        self.__posicoesx = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700]
        self.__posicoesy = [80,160,240]
        self.__rect.center = (0, self.__posicoesy[random.randint(0,len(self.__posicoesy)-1)])

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property
    def dano(self):
        return self.__dano
    
    @dano.setter
    def dano(self, dano):
        self.__dano = dano

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, imagem):
        self.__image = imagem
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    @property
    def posicoesx(self):
        return self.__posicoesx

    @property
    def posicoesy(self):
        return self.__posicoesy

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def movimento(self):
        pass
    
    def geracao(self, display):
        display.blit(self.__image, (self.__rect.x,self.__rect.y))

class Nave(Inimigo, pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, largura):
        super().__init__()
        self.__direcao = random.randint(0,1)
        if self.__direcao == 0:
            self.rect.x = random.randint(-500, -10)
        else:
            self.rect.x = random.randint(largura+10, largura+500)
        self.__maxiposi = self.posicoesx[random.randint(0,len(self.posicoesx)-1)]
        self.tiros = Sprites().tiros
        self.__tiro_temporizador = 0
        self.__cooldown_tiro = 2
    
    @property
    def tiro_temporizador(self):
        return self.__tiro_temporizador
    
    @tiro_temporizador.setter
    def tiro_temporizador(self, tiro_temporizador):
        self.__tiro_temporizador = tiro_temporizador

    @property
    def maxiposi(self):
        return self.__maxiposi
    
    @property
    def direcao(self):
        return self.__direcao

    def disparar(self, janela):
        if self.__tiro_temporizador >= self.__cooldown_tiro:
            self.tiros.add(Tiro(self.rect.center, 6, janela))
            self.__tiro_temporizador = 0

    def movimento(self):
        if self.__direcao == 0:
            if self.rect.x < self.__maxiposi:
                self.rect.x += self.velocidade
        else:
            if self.rect.x > self.__maxiposi:
                self.rect.x -= self.velocidade

class NaveComum(Nave, pygame.sprite.Sprite):
    def __init__(self, largura):
        super().__init__(largura)

class Kamikaze(Nave, pygame.sprite.Sprite):
    def __init__(self, largura):
        super().__init__(largura)
        self.image = pygame.transform.scale(pygame.image.load("kamikaze_nave.png"), (70,70))
        self.__dano_explosao = 20
    
    @property
    def dano_explosao(self):
        return self.__dano_explosao

    @dano_explosao.setter
    def dano_explosao(self, dano_explosao):
        self.__dano_explosao = dano_explosao
    
    def explodir(self, jogador):
        if jogador.rect.x <= self.rect.x+self.rect.width/2:
            jogador.rect.x -= 50
        else:
            jogador.rect.x += 50
        if jogador.rect.y+jogador.rect.bottom <= self.rect.y+self.rect.height/2:
            jogador.rect.y -= 100
        else:
            jogador.rect.y += 100

    def movimento(self, inimigos, altura):
        super().movimento()
        if self.direcao == 0:
            if self.rect.x >= self.maxiposi:
                if self.rect.y <= altura:
                    self.rect.y += self.velocidade
                else:
                    inimigos.remove(self)
        else:
            if self.rect.x <= self.maxiposi:
                if self.rect.y <= altura:
                    self.rect.y += self.velocidade
                else:
                    inimigos.remove(self)

class Meteoro(Inimigo, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("meteoro.png"), (50,60))
        self.__recompensa = random.randint(1,10)
        self.rect.x = self.posicoesx[random.randint(0,len(self.posicoesx)-1)]
        self.rect.y = random.randint(-500,-10)

    @property
    def recompensa(self):
        return self.__recompensa
    
    def movimento(self, inimigos, altura):
        if self.rect.y < altura+10:
            self.rect.y += self.velocidade
        else:
            inimigos.remove(self)