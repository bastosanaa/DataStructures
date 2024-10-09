
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
    def __inserirPrimeiro(self, elemento):
        self.__inicio = elemento
        self.__fim = elemento
        self.__cursor = elemento
    
    # listar
    def acessarAtual(self) -> Elemento:
        if self.__cursor:
            return self.__cursor.getValor()
        print('Lista Vazia')

    def listaTodos(self):
        print('-------')
        if self.__cursor:
            self.__irParaPrimeiro()
            print(self.__cursor.getValor())
            while self.__cursor != self.__fim:
                self.__avancarKPosicoes(1)
                print(self.__cursor.getValor())
        else:
            print('lista vazia')
        print('-------')

    # inserir
    def inserirAntesAtual(self, valor) -> None:
        novo = Elemento(valor)
        if self.__cursor:
            novo.setAntecessor(self.__cursor.getAntecessor())
            novo.setSucessor(self.__cursor)
            if self.__cursor == self.__inicio:
                self.__inicio = novo
            else:
                self.__cursor.getAntecessor().setSucessor(novo)
            self.__cursor.setAntecessor(novo)
            self.__cursor = novo
        else:
            self.__inserirPrimeiro(novo)
            
    def inserirAposAtual(self, valor) -> None:
        novo = Elemento(valor)
        if self.__cursor:
            novo.setAntecessor(self.__cursor)
            novo.setSucessor(self.__cursor.getSucessor())
            if self.__cursor == self.__fim:
                self.__fim = novo
            else:
                self.__cursor.getSucessor().setAntecessor(novo)
            self.__cursor.setSucessor(novo)
            self.__cursor = novo
        else:
            self.__inserirPrimeiro(novo)

    def inserirPorUltimo(self, valor) -> None:
        novo = Elemento(valor)
        if self.__fim:
            novo.setAntecessor(self.__fim)
            self.__fim.setSucessor(novo)
        self.__fim = novo
        self.__cursor = self.__fim
    
    def inserirPorPrimeiro(self, valor) -> None:
        novo = Elemento(valor)
        if self.__inicio:
            novo.setSucessor(self.__inicio)
            self.__inicio.setAntecessor(novo)
        self.__inicio = novo
        self.__cursor = self.__inicio

    def inserirNaPosicao(self,k ,valor) -> None:
        if self.__cursor:
            self.__irParaPrimeiro()
            self.__avancarKPosicoes(k-1)
            self.inserirAposAtual(valor)
        else:
            novo = Elemento(valor)
            self.__inserirPrimeiro(novo)
    
    # excluir
    def excluirAtual(self) -> None:
        if self.__cursor:
            if self.__cursor == self.__fim:
                return self.excluirUltimo()
            if self.__cursor == self.__inicio:
                return self.excluirPrimeiro()
            antecessor = self.__cursor.getAntecessor()
            sucessor = self.__cursor.getSucessor()
            antecessor.setSucessor(sucessor)
            sucessor.setAntecessor(antecessor)
            self.__cursor = antecessor

    def excluirPrimeiro(self) -> None:
        if self.__inicio and self.__inicio.getSucessor():
            self.__inicio = self.__inicio.getSucessor()
            self.__inicio.setAntecessor(None)
        else:
            self.__inicio = None
        self.__cursor = self.__inicio

    def excluirUltimo(self) -> None:
        if self.__fim and self.__fim.getAntecessor():
            self.__fim = self.__fim.getAntecessor()
            self.__fim.setSucessor(None)
        else:
            self.__fim = None
        self.__cursor = self.__fim
    
    def excluirElemento(self, valor) -> None:
        self.__irParaPrimeiro()
        while self.__cursor.getValor() != valor:
            if self.__cursor == self.__fim:
                break
            self.__avancarKPosicoes(1)
        self.excluirAtual()
    
    def excluirDaPosicao(self, posicao) -> None:
        self.__irParaPrimeiro()
        self.__avancarKPosicoes(posicao)
        self.excluirAtual()


l1 = MinhaListaDuplamenteEncadeada()

# realizando insercoes na lista
l1.inserirNaPosicao(0, 20) #insere 20 como primeiro elemento
l1.inserirAposAtual(40) #insere 40 apos 20
l1.inserirAntesAtual(30) #insere 30 antes do 40
l1.inserirPorPrimeiro(10) #insere 10 como primeiro, antes do 20
l1.inserirPorUltimo(50) # insere 50 como ultimo, depois do 40
l1.listaTodos()
# saida esperada = 10, 20, 30, 40, 50

#cursor no 50
#realizando exclusoes na lista
l1.excluirAtual() #exclui 50
l1.excluirDaPosicao(1) #exclui 20
l1.excluirElemento(30) #exclui 30
l1.excluirPrimeiro() #exclui 10
l1.excluirUltimo() #exclui 40
l1.listaTodos()
#saida esperada = lista vazia



