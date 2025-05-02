from Elemento import Elemento 
from No import No 
from FilaEncadeada import FilaEncadeada 
f = FilaEncadeada()
c = int(input("Digite o valor da chave [-1 para sair]: "))
while c != -1:
    nome = input("Digite um nome: ")
    e = Elemento(c, nome)
    n = No(e)
    f.enQueue(n)
    print("Fila Atual: ")
    f.mostraLista()
    c = int(input("\n\nDigite o valor da chave [-1 para sair]: "))

print("\n\nDesenfileirando\n")
while not f.filaVazia():
    print(f.deQueue().getValores())

