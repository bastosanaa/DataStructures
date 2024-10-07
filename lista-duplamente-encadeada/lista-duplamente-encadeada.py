
class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__sucessor = None
    def setSucessor(self, sucessor):
        self.__sucessor = sucessor
    def getSucessor(self):
        return self.__sucessor
    def setValor(self, valor):
        self.__valor = valor
    def getValor(self):
        return self.__valor

class EmptyListError(Exception):
    """Exceção levantada quando uma operação é realizada em uma lista encadeada vazia."""
    pass

class MinhaListaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__cursor = None

# operacoes de cursor
    def avançarKPosições(self, k ):
        if self.__inicio:
            avancar = k
            while avancar > 0:
                if not self.__cursor.getSucessor():
                    break
                self.__cursor = self.__cursor.getSucessor()
                avancar -= 1
        else:
            print('Lista vazia')

    def retrocederKPosições (self, k):
        return
    def __irParaPrimeiro(self):
        self.__cursor = self.__inicio

    def __irParaUltimo(self):
        while self.__cursor.getSucessor():
            self.__cursor = self.__cursor.getSucessor()



# operacoes na lista
    def acessarAtual(self):
        if self.__cursor:
            return self.__cursor.getValor()
        else:
            print('Lista vazia')

    #método da visão além do alcance
    def inserirAntesDoAtual (self, valorNovo):
        novo = Elemento(valorNovo)
        atual = self.__cursor
        if self.__cursor:
            if self.__cursor == self.__inicio:
                novo.setSucessor(self.__inicio)
                self.__inicio = novo
                self.__cursor = self.__inicio
            else:
                self.__irParaPrimeiro()
                proximo = self.__cursor.getSucessor()
                while proximo != atual:
                    self.__cursor = proximo
                    proximo = self.__cursor.getSucessor()
                novo.setSucessor(proximo)
                self.__cursor.setSucessor(novo)
                # cursor aponta novamente para o atual
                self.__cursor = proximo
        else:
            raise EmptyListError
        
    def inserirApósAtual (self, valorNovo):
        novo = Elemento(valorNovo)
        novo.setSucessor(self.__cursor.getSucessor())
        self.__cursor.setSucessor(novo)

    def inserirComoUltimo (self,valorNovo):
        novo = Elemento(valorNovo)
        if self.__inicio:
            self.__irParaUltimo()
            self.__cursor.setSucessor(novo)
            self.__cursor = novo
        else:
            self.__inicio = novo
            self.__cursor = self.__inicio

    def inserirComoPrimeiro (self, valorNovo):
        novo = Elemento(valorNovo)
        novo.setSucessor(self.__inicio)
        self.__inicio = novo

    def inserirNaPosicao ( k, novo ):
        return
    def excluirAtual ():
        return
    def excluirPrim ():
        return
    def excluirUlt ():
        return
    def excluirElem ( chave ):
        return
    def excluirApos ( k ):
        return
    def buscar ( chave ):
        return
