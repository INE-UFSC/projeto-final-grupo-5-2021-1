import pygame
import pygame_gui
from View import View
from JogadorNave import Jogador

class InterfaceLoja(View):
    def __init__(self):
        super().__init__()
        self.__botao_dano = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.posicao_botao, self.tamanho_botao),
                                            text='Aprimorar dano: +5 $100',
                                            manager=self.manager)
        self.__botao_velocidade = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + self.tamanho_botao[1] + 20), self.tamanho_botao),
                                            text='Aprimorar velocidade: +1 $100',
                                            manager=self.manager)
        self.__botao_vida = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + 2*(self.tamanho_botao[1] + 20)), self.tamanho_botao),
                                            text='Aumentar vida: +25 $100',
                                            manager=self.manager)
        self.__botao_continuar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.posicao_botao[0], self.posicao_botao[1] + 3*(self.tamanho_botao[1] + 20)), self.tamanho_botao),
                                            text='Continuar',
                                            manager=self.manager)

        self.botoes = [self.__botao_dano, self.__botao_velocidade, self.__botao_vida, self.__botao_continuar]
        self.atualizar(40)

        self.__saldo_insuficiente = False
        self.__compra_maxima = False

    @property
    def botao_dano(self):
        return self.__botao_dano

    @property
    def botao_velocidade(self):
        return self.__botao_velocidade

    @property
    def botao_vida(self):
        return self.__botao_vida

    @property
    def botao_continuar(self):
        return self.__botao_continuar
    
    @property
    def saldo_insuficiente(self):
        return self.__saldo_insuficiente

    @saldo_insuficiente.setter
    def saldo_insuficiente(self, insuficiente: bool):
        self.__saldo_insuficiente = insuficiente
        
    @property
    def compra_maxima(self):
        return self.__compra_maxima

    @compra_maxima.setter
    def compra_maxima(self, maxima: bool):
        self.__compra_maxima = maxima

    def fundos_insuficientes(self):
        fonte_mensagem = pygame.font.SysFont('comicssans', 40)
   
        mensagem_fundos_insuficientes = fonte_mensagem.render('Você não possui dinheiro suficiente!', True, (255,0,0))
        self.tela.janela.blit(mensagem_fundos_insuficientes, (self.posicao_botao[0] + 30, self.tela.altura - 50))
        
    def mensagem_maximo_compra(self):
        fonte_mensagem = pygame.font.SysFont('comicssans', 40)

        mensagem_maximo_compra = fonte_mensagem.render('Você já comprou o máximo possível!', True, (255, 0, 0))
        self.tela.janela.blit(mensagem_maximo_compra, (self.posicao_botao[0] + 30, self.tela.altura - 50))

    def textos(self, dinheiro: int, jogador: Jogador):
        fonte_mensagem = pygame.font.SysFont('comicssans', 70)
        fonte_atributos = pygame.font.SysFont('comicssans', 30)

        loja = fonte_mensagem.render("Loja", True, (255,255,255))
        self.tela.janela.blit(loja, (self.tela.largura / 3 + 70, 20))

        valor_dinheiro = fonte_atributos.render("Dinheiro: $" + str(dinheiro), True, (255,255,255))
        self.tela.janela.blit(valor_dinheiro, (10, 90))

        valor_dano = fonte_atributos.render("Dano: " + str(jogador.dano), True, (255,255,255))
        self.tela.janela.blit(valor_dano, (210 , 90))

        valor_velocidade = fonte_atributos.render("Velocidade: " + str(jogador.velocidade), True, (255,255,255))
        self.tela.janela.blit(valor_velocidade, (410, 90))

        valor_vida = fonte_atributos.render("Vida: " + str(jogador.vida), True, (255,255,255))
        self.tela.janela.blit(valor_vida, (630, 90))

    def window(self, dinheiro: int, jogador: Jogador):
        super().window(dinheiro, jogador)
        if self.__saldo_insuficiente:
            self.fundos_insuficientes()
        elif self.__compra_maxima:
            self.mensagem_maximo_compra()
