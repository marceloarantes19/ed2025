from Elemento import Elemento
from No import No
class Lista:
  def __init__(self):
    self.__cabeca = No()
    self.__cabeca.setProximo(None)
  def getCabeca(self):
    return self.__cabeca
  def setCabeca(self, c):
    self.__cabeca = c 
  def listaVazia(self):
    return self.getCabeca().getProximo() == None
  def mostraLista(self):
    n = self.getCabeca().getProximo()
    while n != None:
      print(n.getValores())
      n = n.getProximo()
  def insereNoInicio(self, n):
    n.setProximo(self.getCabeca().getProximo())
    self.getCabeca().setProximo(n)
  def retiraNoInicio(self):
    ret = None
    if not self.listaVazia():
      ret = self.getCabeca().getProximo()
      self.getCabeca().setProximo(ret.getProximo())
      ret.setProximo(None)
    return ret
  def insereNoFim(self, n):
    atual = self.getCabeca()
    while atual.getProximo()!=None:
      atual = atual.getProximo()
    atual.setProximo(n)
  def retiraNoFim(self):
    ret = None 
    if not self.listaVazia():
      ant = self.getCabeca()
      ret = ant.getProximo()
      while ret.getProximo() != None:
        ant = ret 
        ret = ant.getProximo()
      ant.setProximo(None)
    return ret
