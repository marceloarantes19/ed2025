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
  def insereOrdenado(self, n):
    ant = self.getCabeca()
    atu = ant.getProximo()
    while atu!=None and n.getChave() > atu.getChave():
      ant = atu
      atu = ant.getProximo()
    n.setProximo(atu)
    ant.setProximo(n)
  def retiraPelaChave(self, c):
    ret = None
    if not self.listaVazia():
      ant = self.getCabeca()
      atu = ant.getProximo()
      while atu != None and atu.getChave() != c:
        ant = atu
        atu = ant.getProximo()
      if atu != None:
        ant.setProximo(atu.getProximo())
        atu.setProximo(None)
        ret = atu
    return ret
  
  # Correção do Exercício 3
  def getQuantidade(self):
    q = 0
    n = self.getCabeca().getProximo()
    while n != None:
      q = q + 1
      n = n.getProximo()
    return q
  
  # Correção do Exercício 4
  def mostraListaRecusrivo(self, n):
    if n != None:
      print(n.getValores())
      self.mostraListaRecusrivo(n.getProximo())
  
  # Correção do Exercício 5
  def mostraListaInvertida(self, n):
    if n != None:
      self.mostraListaInvertida(n.getProximo())
      print(n.getValores())
  
  # Correção do Exercício 6
  def insereNaPosicao(self, n, p):
    if p > 0 and p <= self.getQuantidade() + 1:
      pa = 1
      ant = self.getCabeca()
      atu = ant.getProximo()
      while atu!=None and pa < p:
        ant = atu
        atu = ant.getProximo()
        pa = pa + 1
      n.setProximo(atu)
      ant.setProximo(n)
  
  # Correção do Exercício 7
  def retiraNaPosicao(self, p):
    ret = None
    if not self.listaVazia() and p <= self.getQuantidade():
      pa = 1
      ant = self.getCabeca()
      atu = ant.getProximo()
      while atu != None and pa < p:
        ant = atu
        atu = ant.getProximo()
        pa = pa + 1
      ant.setProximo(atu.getProximo())
      atu.setProximo(None)
      ret = atu
    return ret

  # Correçaão do Exercício 8
  def limpaLista(self, n):
    if n != None:
      self.limpaLista(n.getProximo())
      n.setProximo(None)
