from Persistencia.DAO import DAO


class AtributosDAO(DAO):
    def __init__(self):
        super().__init__(datasource='jogo.pkl')

    def salvar_variaveis(self, vida: int, dano: int, velocidade: int, dinheiro: int, nivel: int):
        self.add('nivel', nivel)
        self.add('vida', vida)
        self.add('dano', dano)
        self.add('velocidade', velocidade)
        self.add('dinheiro', dinheiro)
    
    def resetar_variaveis(self):
        self.add('nivel', 0)
        self.add('vida', 100)
        self.add('dano', 25)
        self.add('velocidade', 5)
        self.add('dinheiro', 0)
