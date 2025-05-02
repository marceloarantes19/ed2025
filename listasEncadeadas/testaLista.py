from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
x = int(input("Digite uma chave [-1 para sair]: "))
while x != -1:
  nome = input("Digite o nome: ")
  e = Elemento(x, nome)
  n = No(e)
  l.insereNoInicio(n)
  l.mostraLista()
  print("\nQuantidade de elementos na lista: "+str(l.getQuantidade()))
  x = int(input("Digite uma chave [-1 para sair]: "))

print("Lista Recursiva ")
l.mostraListaRecusrivo(l.getCabeca().getProximo())

print("Mostra Lista Invertida ")
l.mostraListaInvertida(l.getCabeca().getProximo())

print("Limpando a Lista")
while not l.listaVazia():
  n = l.retiraNoInicio()
  if n!=None:
    print(n.getValores())


