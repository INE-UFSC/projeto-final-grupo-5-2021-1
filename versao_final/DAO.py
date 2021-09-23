from abc import ABC, abstractmethod
import pickle

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource):
        super().__init__()
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, chave, valor):
        self.__object_cache[chave] = valor
        self.__dump()

    def get(self, chave):
        try:
            return self.__object_cache[chave]
        except KeyError:
            return "KeyError"
    
    @abstractmethod
    def salvar_variaveis(self):
        pass
    
    @abstractmethod
    def resetar_variaveis(self):
        pass
