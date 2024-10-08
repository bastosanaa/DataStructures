
class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__sucessor = None
        self.__antecessor = None
    def setSucessor(self, sucessor):
        self.__sucessor = sucessor
    def getSucessor(self):
        return self.__sucessor
    def setAntecessor(self, antecessor):
        self.__antecessor = antecessor
    def getAntecessor(self):
        return self.__antecessor
    def setValor(self, valor):
        self.__valor = valor
    def getValor(self):
        return self.__valor

class MinhaListaDuplamenteEncadeada:
    def __init__(self) -> None:
        self.__inicio = None
        self.__fim = None
        self.__cursor = None

    #operações de cursor
    def __avancarKPosicoes(self, k):
        if self.__fim != self.__cursor != None:
            posicoes = k
            while posicoes > 0:
                if self.__cursor.getSucessor() == None:
                    break
                self.__cursor = self.__cursor.getSucessor()
                posicoes -= 1

    def __retrocederKPosicoes(self, k):
        if self.__inicio != self.__cursor != None:
            posicoes = k
            while posicoes > 0:
                if self.__cursor.getAntecessor() == None:
                    break
                self.__cursor = self.__cursor.getAntecessor()
                posicoes -= 1
    
    def __irParaPrimeiro(self):
        self.__cursor = self.__inicio

    def __irParaUltimo(self):
        self.__cursor = self.__fim

    #Funções de Lista
    def acessarAtual(self) -> Elemento:
        if self.__cursor:
            return self.__cursor.getValor()
        else:
            print('Lista Vazia')
    
    def inserirAntesAtual(self, valor) -> None:
        novo = Elemento(valor)
        if self.__cursor == self.__inicio:
            

