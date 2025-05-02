# Converte inteiro para Binário
from Elemento import Elemento 
from No import No 
from PilhaEncadeada import PilhaEncadeada 
pilha = PilhaEncadeada()
valor = int(input("Digite um valor inteiro: "))
while valor > 0:
    el = Elemento(valor % 2)
    no = No(el)
    pilha.push(no)
    valor = valor // 2
s = ""
while not pilha.pilhaVazia():
    s = s + str(pilha.pop().getChave())

print(s)