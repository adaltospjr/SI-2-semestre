lista = [4, 6, 8, 10]

def pilha_par_impar(pilha):
    pilha_par = []
    pilha_impar = []

    for i in range(len(pilha)):
        if pilha[i] % 2 == 0:
            pilha_par.append(pilha[i])
        else:
            pilha_impar.append(pilha[i])
    return pilha_par, pilha_impar

teste = pilha_par_impar(lista)
print(teste)
