from Persistencia.DAO import DAO


class LojaDAO(DAO):
    def __init__(self):
        super().__init__(datasource='loja.pkl')
    
    def salvar_variaveis(self, compra_dano: int, compra_velocidade: int):
        self.add('compradano', compra_dano)
        self.add('compravelocidade', compra_velocidade)

    def resetar_variaveis(self):
        self.add('compradano', 0)
        self.add('compravelocidade', 0)
