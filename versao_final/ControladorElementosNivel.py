from JogadorNave import Jogador
from AtributosDao import AtributosDAO
from TelaJogo import TelaJogo
from Inimigo import *
from Sprites import *
import random
from ControladorDinheiro import ControladorDinheiro
from EfeitosSonoros import EfeitosSonoros
from HUD import HUD


class ControladorElementosNivel:
    def __init__(self, atributos: AtributosDAO, dinheiro: ControladorDinheiro):
        if isinstance(atributos, AtributosDAO):
            self.__nivel = atributos.get('nivel')
        if isinstance(dinheiro, ControladorDinheiro):
            self.__controle_dinheiro = dinheiro
        self.tempo_fase = 0
        self.__explodir = False
        self.__tempo = 0
        self.__posicaox = 0
        self.__posicaoy = 0
        self.__imagem_explosao = None

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel
        
    @property
    def explodir(self):
        return self.__explodir

    @explodir.setter
    def explodir(self, explodir):
        self.__explodir = explodir

    @property
    def tempo(self):
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo
        
    def elementos_tela(self, tela: TelaJogo, hud: HUD, jogador: Jogador, dinheiro: ControladorDinheiro, tempo: int, FPS: int):
        if isinstance(tela, TelaJogo) and isinstance(hud, HUD) and isinstance(jogador, Jogador) and isinstance(dinheiro, ControladorDinheiro):
            tela.mostrar_fundo()
            hud.mostrar_nivel(self.nivel)
            hud.mostrar_vida(jogador)
            hud.mostrar_inimigos_restantes(len(sprites.inimigos))
            hud.mostrar_tempo(tempo)
            hud.mostrar_dinheiro_jogador(dinheiro.dinheiro)

            for inimigo in sprites.inimigos:
                inimigo.geracao(tela.janela)
                if isinstance(inimigo, Nave):
                    inimigo.tiro_temporizador += 1 / FPS
                    inimigo.disparar(tela.altura)
                    inimigo.tiros.draw(tela.janela)
                    inimigo.tiros.update()

        sprites.jogador.draw(surface=tela.janela)
        sprites.jogador.sprite.tiros.draw(tela.janela)

    def colisoes(self, jogador: Jogador, efeito_sonoro: EfeitosSonoros):
        if isinstance(jogador, Jogador) and isinstance(efeito_sonoro, EfeitosSonoros):
            for inimigo_acertado in jogador.colisao(sprites.inimigos, jogador.tiros):
                inimigo_acertado.vida -= sprites.jogador.sprite.dano
                if 0 >= inimigo_acertado.vida:
                    self.__controle_dinheiro.dinheiro += inimigo_acertado.recompensa
                    sprites.inimigos.remove(inimigo_acertado)

            for inimigo_colidido in jogador.colisao(sprites.jogador, sprites.inimigos).values():
                efeito_sonoro.tocar_som(efeito_sonoro.som_explosao)
                if isinstance(inimigo_colidido[0], Nave):
                    self.__explodir = True
                    self.__imagem_explosao = inimigo_colidido[0].imagem_explosao
                    self.__posicaox = inimigo_colidido[0].rect.x
                    self.__posicaoy = inimigo_colidido[0].rect.y
                    inimigo_colidido[0].explodir(jogador)
                else:
                    jogador.vida -= inimigo_colidido[0].dano_colisao
                    
            for inimigo in sprites.inimigos:
                if isinstance(inimigo, Nave):
                    if jogador.colisao(sprites.jogador, inimigo.tiros):
                        sprites.jogador.sprite.vida -= inimigo.dano


    def geracao_inimigos(self, largura_tela: int):
        if len(sprites.inimigos) == 0:
            self.__nivel += 1
            self.tempo_fase = 0
            for _ in range(0, (self.nivel * 2) + 3):
                escolha_inimigo = random.randint(1, 3)
                if escolha_inimigo == 1:
                    novo_inimigo = NaveComum(largura_tela)
                elif escolha_inimigo == 2:
                    novo_inimigo = Kamikaze(largura_tela)
                else:
                    novo_inimigo = Meteoro()
                sprites.inimigos.add(novo_inimigo)
                
    def explosao(self, tela):
        if self.__explodir:
            tela.blit(self.__imagem_explosao, (self.__posicaox, self.__posicaoy))
            self.__tempo += 1
        if self.__tempo >= 15:
            self.__explodir = False
            self.__tempo = 0

    def comportamento_inimigos(self, tela: TelaJogo):
        if isinstance(tela, TelaJogo):
            for inimigo in sprites.inimigos:
                if isinstance(inimigo, NaveComum):
                    inimigo.movimento(tela)
                else:
                    inimigo.movimento(sprites.inimigos, tela.altura)
