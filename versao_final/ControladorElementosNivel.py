from JogadorNave import Jogador
from VariaveisDao import VariaveisDAO
from Inimigo import *
from Sprites import *
import random


class ControladorElementosNivel():
    def __init__(self, variavel: VariaveisDAO):
        if isinstance(variavel, VariaveisDAO):
            self.__nivel = variavel.get('nivel')
        self.tempo_fase = 0
  
    @property
    def nivel(self):
        return self.__nivel
 
    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    def colisoes(self, jogador:Jogador):
        for inimigo_acertado in jogador.colisao(sprites.inimigos, jogador.tiros):
            inimigo_acertado.vida -= sprites.jogador.sprite.dano
            if inimigo_acertado.vida == 0:
                if isinstance(inimigo_acertado, Nave):
                    jogador.naves_destruidas += 1
                elif isinstance(inimigo_acertado, Meteoro):
                    jogador.meteoros_destruidos.append(inimigo_acertado.recompensa)
                sprites.inimigos.remove(inimigo_acertado)

        for inimigo_colidido in jogador.colisao(sprites.jogador, sprites.inimigos).values():
            if isinstance(inimigo_colidido[0], Kamikaze):
                inimigo_colidido[0].explodir(jogador)
                jogador.vida -= inimigo_colidido[0].dano_explosao
            elif isinstance(inimigo_colidido[0], NaveComum) or isinstance(inimigo_colidido[0], Meteoro):
                jogador.vida -= inimigo_colidido[0].dano * 2


    def geracao_inimigos(self, largura_tela):
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

    def comportamento_inimigos(self, janela, altura_janela, jogador:Jogador, FPS):
        for inimigo in sprites.inimigos:
            inimigo.geracao(janela)
            if isinstance(inimigo, Meteoro):
                inimigo.movimento(sprites.inimigos, altura_janela)
            else:
                inimigo.tiro_temporizador += 1 / FPS
                if isinstance(inimigo, Kamikaze):
                    inimigo.movimento(sprites.inimigos, altura_janela)
                else:
                    inimigo.movimento()
                inimigo.disparar(altura_janela)
                inimigo.tiros.draw(janela)
                inimigo.tiros.update()
                if jogador.colisao(sprites.jogador, inimigo.tiros):
                    sprites.jogador.sprite.vida -= inimigo.dano
        # Vale a pena replicar repetir uma parte do código p/ deixar draw em elementos_tela e a colisão dos tiros em colisoes?
        #por questão de organização faria sentido, mas podemos deixar isso para o momento de refinar o código

