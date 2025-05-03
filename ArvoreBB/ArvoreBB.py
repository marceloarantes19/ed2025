from Elemento import Elemento
from NoABB import NoABB 
class ArvoreBB:
    def __init__(self):
        self.__raiz = None 
    def getRaiz(self):
        return self.__raiz 
    def setRaiz(self, n):
        self.__raiz = n 
    def criaNo(self, chave = 0, nome = ""):
        e = Elemento(chave, nome)
        n = NoABB(e)
        return n 
    def arvoreVazia(self):
        return self.getRaiz() == None 
    def insereNo(self, chave = 0, nome = ""):
        no = self.criaNo(chave, nome)
        if self.arvoreVazia():
            self.setRaiz(no)
        else:
            self.insere(None, self.getRaiz(), no)
    def insere(self, pai, atual, no):
        if atual == None:
            if no.getChave() < pai.getChave():
                pai.setFe(no)
            else:
                pai.setFd(no)
        elif no.getChave() < atual.getChave():
            self.insere(atual, atual.getFe(), no)
        else:
            self.insere(atual, atual.getFd(), no)
    def emOrdem(self, no):
        if no != None:
            self.emOrdem(no.getFe())
            print(no.getValores())
            self.emOrdem(no.getFd())