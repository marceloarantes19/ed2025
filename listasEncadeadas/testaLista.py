from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
x = int(input("Digite uma chave [-1 para sair]: "))
while x != -1:
  nome = input("Digite o nome:")
  e = Elemento(x, nome)
  n = No(e)
  l.insereNoInicio(n)
  l.mostraLista()
  x = int(input("Digite uma chave [-1 para sair]: "))

print("Limpando a Lista")
while not l.listaVazia():
  n = l.retiraNoInicio()
  if n!=None:
    print(n.getValores())


