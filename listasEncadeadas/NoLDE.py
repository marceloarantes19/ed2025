from Elemento import Elemento
class No:
  def __init__(self, e = None):
    self.__dados = e
    self.__ante  = None
    self.__prox  = None
  def getDados(self):
    return self.__dados 
  def setDados(self, d):
    self.__dados = d 
  def getProximo(self):
    return self.__prox 
  def setProximo(self, p):
    self.__prox = p
  def getAnterior(self):
    return self.__ante 
  def setAnterior(self, a):
    self.__ante = a
  def getChave(self):
    return self.getDados().getChave()
  def getNome(self):
    return self.getDados().getNome()
  def getValores(self):
    return self.getDados().getValores()