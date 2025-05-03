from ArvoreBB import ArvoreBB 
a = ArvoreBB()
x = int(input("Digite uma chave [-1 para sair]: "))
while x != -1:
    a.insereNo(x)
    a.emOrdem(a.getRaiz())
    x = int(input("Digite uma chave [-1 para sair]: "))
