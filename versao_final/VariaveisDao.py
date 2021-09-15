import pickle


class VariaveisDAO:
    def __init__(self, datasource='jogo.pkl'):
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

    def add(self, variavel, valor):
        self.__object_cache[variavel] = valor
        self.__dump()

    def get(self, variavel):
        try:
            return self.__object_cache[variavel]
        except KeyError:
            return "KeyError"
