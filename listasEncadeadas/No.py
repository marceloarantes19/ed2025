from Elemento import Elemento
class No:
  def __init__(self, e = None):
    self.__dados = e
    self.__prox  = None
  def getDados(self):
    return self.__dados 
  def setDados(self, d):
    self.__dados = d 
  def getProximo(self):
    return self.__prox 
  def setProximo(self, p):
    self.__prox = p
  def getChave(self):
    return self.getDados().getChave()
  def getNome(self):
    return self.getDados().getNome()
  def getValores(self):
    return self.getDados().getValores()