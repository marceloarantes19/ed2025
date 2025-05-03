from Elemento import Elemento 
class NoABB:
    def __init__(self, elemento = None):
        self.__dado = elemento 
        self.__fe = None
        self.__fd = None 
    def getDado(self):
        return self.__dado 
    def setDado(self, d):
        self.__dado = d 
    def getFe(self):
        return self.__fe 
    def setFe(self, fe):
        self.__fe = fe 
    def getFd(self):
        return self.__fd 
    def setFd(self, fd):
        self.__fd = fd 
    def getChave(self):
        return self.getDado().getChave()
    def getValores(self):
        return self.getDado().getValores()
