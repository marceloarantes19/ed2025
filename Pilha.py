class Pilha:
  def __init__(self):
    self.__pilha = []

  def pilhaVazia(self):
    return len(self.__pilha) == 0
  
  def push(self, v):
    self.__pilha.append(v)

  def pop(self):
    ret = None
    if not self.pilhaVazia():
      ret = self.__pilha.pop()
    return ret
  