from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
x = int(input("Digite uma chave [-1 para sair]: "))
while x != -1:
  nome = input("Digite o nome:")
  e = Elemento(x, nome)
  n = No(e)
  p = int(input("Digite a posiçao: "))
  l.insereNaPosicao(n, p)
  l.mostraLista()
  x = int(input("Digite uma chave [-1 para sair]: "))

print("Limpando a Lista")
x = int(input("Digite a posicao para retirada de elemento da lista [-1 para sair]: "))
while x != -1:
  n = l.retiraNaPosicao(x)
  if n!=None:
    print(n.getValores())
  else:
    print(x, " Não existe na lista")
  print("\nLista atual") 
  l.mostraLista() 
  x = int(input("Digite uma chave para retirada de elemento da lista [-1 para sair]: "))

