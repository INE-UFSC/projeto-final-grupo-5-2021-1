import pygame
from Entidades.Tiro import Tiro
from Persistencia.AtributosDao import AtributosDAO
from Componentes.TelaJogo import TelaJogo
from Componentes.EfeitosSonoros import EfeitosSonoros
from Componentes.Sprites import *


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__atributos_dao = AtributosDAO()
        self.__posicao = (TelaJogo().largura/2, TelaJogo().altura)
        self.image = pygame.transform.scale(pygame.image.load('Imagens/Ship_Player_PNG_01.png'), (60,60))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom = self.__posicao)
        self.__velocidade = self.__atributos_dao.get('velocidade')
        self.__limite_x = TelaJogo().largura
        self.__limite_y = TelaJogo().altura
        self.__tiro_pronto = True
        self.__tiro_temporizador = 0
        self.__cooldown_tiro = 600
        self.tiros = Sprites().tiros
        self.__vida = self.__atributos_dao.get('vida')
        self.__dano = self.__atributos_dao.get('dano')
        sprites.jogador.add(self)

    @property
    def dano(self):
        return self.__dano

    @dano.setter
    def dano(self, valor_dano):
        self.__dano = valor_dano

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    def atributos_iniciais(self):
        self.__vida = 100
        self.__dano = 25
        self.__velocidade = 5
    
    def posicao_inicial(self):
        self.rect = self.image.get_rect(midbottom = self.__posicao)

    def get_input(self, efeito_sonoro: EfeitosSonoros):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.__velocidade
        if keys[pygame.K_a]:
            self.rect.x -= self.__velocidade
        if keys[pygame.K_w]:
            self.rect.y -= self.__velocidade
        if keys[pygame.K_s]:
            self.rect.y += self.__velocidade

        if keys[pygame.K_SPACE] and self.__tiro_pronto:
            if isinstance(efeito_sonoro, EfeitosSonoros):
                efeito_sonoro.tocar_som(efeito_sonoro.som_disparo)
            self.atirar()
            self.__tiro_pronto = False
            self.__tiro_temporizador = pygame.time.get_ticks()

    def recarregar(self):
        if not self.__tiro_pronto:
            momento = pygame.time.get_ticks()
            if momento - self.__tiro_temporizador >= self.__cooldown_tiro:
                self.__tiro_pronto = True

    def atirar(self):
        self.tiros.add(Tiro(self.rect.center, -6, self.rect.bottom))

    def limite_x(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.__limite_x:
            self.rect.right = self.__limite_x

    def limite_y(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.__limite_y:
            self.rect.bottom = self.__limite_y

    def colisao(self, grupo1, grupo2):
        return pygame.sprite.groupcollide(grupo1, grupo2, False, True, pygame.sprite.collide_mask)

    def update(self, efeito_sonoro: EfeitosSonoros):
        if isinstance(efeito_sonoro, EfeitosSonoros):
            self.get_input(efeito_sonoro)
        self.limite_x()
        self.limite_y()
        self.recarregar()
        self.tiros.update()
