class Elemento:
  def __init__(self, chave = 0, nome = ""):
    self.__chave = chave
    self.__nome = nome
  def getChave(self):
    return self.__chave
  def setChave(self, c):
    self.__chave = c
  def getNome(self):
    return self.__nome 
  def setNome(self, n):
    self.__nome = n 
  def getValores(self):
    return self.getChave(), self.getNome()