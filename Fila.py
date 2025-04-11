class Fila:
  def __init__(self):
    self.__fila = []

  def filaVazia(self):
    return len(self.__fila) == 0
  
  def enQueue(self, v):
    self.__fila.append(v)

  def deQueue(self):
    ret = None
    if not self.filaVazia():
      ret = self.__fila.pop(0)
    return ret
