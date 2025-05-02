from Lista import Lista
class FilaEncadeada(Lista):
    def filaVazia(self):
        return self.listaVazia()
    def enQueue(self, n):
        self.insereNoFim(n)
    def deQueue(self):
        return self.retiraNoInicio()
