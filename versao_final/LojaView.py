import sys
import pygame as sg
import pygame.font
from TelaJogo import TelaJogo
from Loja import Loja
from Sprites import *
from ControladorDinheiro import ControladorDinheiro

class InterfaceLoja:
    def __init__(self):
        self.__container = []
        self.__tela = TelaJogo()
        self.__is_on_loja = True
        self.__tamanho_botao = (self.__tela.largura - 250, 80)
        self.__posicao_botao = ((self.__tela.largura / 4) - 80, 150)
        self.__click = False



    def mensagens(self, dinheiro: ControladorDinheiro):
        fonte_botao = pygame.font.SysFont('comicssans', 30)
        fonte_loja = pygame.font.SysFont('comicssans', 70)
        fonte_dinheiro = pygame.font.SysFont('comicssans', 35)

        nome_loja = fonte_loja.render('Loja', True, (255,0,0))
        self.__tela.janela.blit(nome_loja, (self.__tela.largura / 6, 10))

        dinheiro_jogador = fonte_dinheiro.render('Dinheiro: {}'.format(dinheiro.dinheiro), True, (255,0,0))
        self.__tela.janela.blit(dinheiro_jogador, (self.__tela.largura/ 3 + 100, 10))

        botao_dano = fonte_botao.render('Aprimorar dano: +15 $100', True, (255,0,0))
        self.__tela.janela.blit(botao_dano, (self.__posicao_botao[0] + 140, self.__posicao_botao[1] + 15))

        botao_velocidade = fonte_botao.render('Aprimorar velocidade: +1 $100', True, (255,0,0))
        self.__tela.janela.blit(botao_velocidade, (self.__posicao_botao[0] + 140, self.__posicao_botao[1] + self.__tamanho_botao[1] + 65))

        botao_escudo = fonte_botao.render('Aumentar vida: +25 $100', True, (255,0,0))
        self.__tela.janela.blit(botao_escudo, (self.__posicao_botao[0] + 140, self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50)+15))

        botao_continuar = fonte_botao.render('Continuar',True, (255,0,0))
        self.__tela.janela.blit(botao_continuar, (self.__posicao_botao[0] +200, self.__posicao_botao[1] + 2 *(self.__tamanho_botao[1] + 100)+25))



#0,1,2 em ordem, botao 3 canto inferior direito
    def botoes(self):
        #botao 0 = aprimorar dano
        pygame.draw.rect(self.__tela.janela, (255,165,0),
        [self.__posicao_botao[0], self.__posicao_botao[1], self.__tamanho_botao[0], self.__tamanho_botao[1]])
        #botao 1 = aprimorar velocidade
        pygame.draw.rect(self.__tela.janela, (255,165,0),
                         [self.__posicao_botao[0], self.__posicao_botao[1] + self.__tamanho_botao[1] + 50,
                          self.__tamanho_botao[0], self.__tamanho_botao[1]])
        #botao 2 = comprar escudo
        pygame.draw.rect(self.__tela.janela,(255,165,0),
                         [self.__posicao_botao[0], self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50),
                          self.__tamanho_botao[0], self.__tamanho_botao[1]]
                         )
        #botao 3 = continuar
        pygame.draw.rect(self.__tela.janela,(255,165,0),
                         [self.__posicao_botao[0], self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 100),
                          self.__tamanho_botao[0], self.__tamanho_botao[1]]
                         )

    def fundos_insuficientes(self):
        fonte_mensagem = pygame.font.SysFont('comicssans', 40)
        mensagem_fundos_insuficientes = fonte_mensagem.render('Você não possui dinheiro suficiente', True, (255,0,0))
        self.__tela.janela.blit(mensagem_fundos_insuficientes, (self.__posicao_botao[0] + 50, self.__posicao_botao[1] + self.__tamanho_botao[1] + 30))




    def abrir_interface_loja(self, loja:Loja, controlador_dinheiro: ControladorDinheiro):
        if len(sprites.inimigos) == 0:
            self.__tela.mostrar_fundo()
            self.botoes()
            self.mensagens(controlador_dinheiro)

            while self.__is_on_loja:
                pygame.display.update()
                mouse = pygame.mouse.get_pos()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #botao 0
                        if self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and \
                                self.__posicao_botao[1] + self.__tamanho_botao[1] > mouse[1] > self.__posicao_botao[1]:
                            if controlador_dinheiro.dinheiro > 100:
                                loja.aumentar_dano(controlador_dinheiro)
                                return False
                            else:
                                self.fundos_insuficientes()
                            print(event)

                        #botao 1
                        elif self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and \
                                self.__posicao_botao[1] + 2 * self.__tamanho_botao[1] + 50 > mouse[1] > \
                                self.__posicao_botao[1] + self.__tamanho_botao[1] + 50:
                            if controlador_dinheiro.dinheiro > 100:
                                loja.aumentar_velocidade(controlador_dinheiro)
                                return False
                            else:
                                self.fundos_insuficientes()
                            print(event)

                        #botao 2
                        elif self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and \
                                self.__posicao_botao[1] + 3 * self.__tamanho_botao[1] + 100 > mouse[1] > \
                                self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1] + 50):
                            if controlador_dinheiro.dinheiro > 100:
                                loja.comprar_escudo(controlador_dinheiro)
                                return False
                            else:
                                self.fundos_insuficientes()
                            print(event)

                        #2: 150 até 670 mais ou menos no X
                        #2: 414 até 487 no y mais ou menos
                        #botao 3
                        elif self.__posicao_botao[0] + self.__tamanho_botao[0] > mouse[0] > self.__posicao_botao[0] and self.__posicao_botao[1] + 3 * self.__tamanho_botao[1] + 150 > mouse[1] > \
                            self.__posicao_botao[1] + 2 * (self.__tamanho_botao[1]+50):
                            print(event)
                            return False

                        elif pygame.event == pygame.QUIT:
                            sys.exit()


    def ver_botoes(self):
        return "{}, {}, {}, {}".format(self.__posicao_botao[0],self.__tamanho_botao[0], self.__posicao_botao[1], self.__tamanho_botao[1])

