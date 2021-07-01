# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Adalto de Almeida Linhares Santos
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


'''
Escreva uma função com o nome pertence, que recebe como argumentos de
entrada uma tupla e dois itens e retorna True, se os dois itens estiverem
armazenado na tupla, e False, caso contrário.
'''


def pertence(tupla, item1, item2):
    if item1 and item2 in tupla:
        return True
    else:
        return False


'''
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    for a in range(len(lista)):
        if velho == lista[a]:
            lista[a] = novo
    return lista


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de
entrada uma lista e um item, e retorna uma tupla contendo todas os índices
em que o item aparece na lista.
'''


def posicoes_lista(lista, item):
    posicao = []
    tupla = ()
    for i in range(len(lista)):
        if lista[i] == item:
            posicao.append(i)
            tupla = tuple(posicao)
    return tupla


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada reprovados que recebe como argumento de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados
(um aluno é reprovado quando a média das suas notas é inferior a 6).
'''


def reprovados(alunos):
    media = []
    for a in alunos:
        total = alunos[a]
        total = sum(total) / len(total)
        if total < 6:
            media.append(a)
    return media


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''


def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        for a, b in alunos.items():
            if nome == a:
                b.append(nota)
                return alunos
    else:
        return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada menores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com a
menor nota de cada aluno.
'''


def menores_notas(alunos):
    menor = []
    resultado = {}
    contador = 0
    for a, b in alunos.items():
        menor.append(min(b))
        resultado[a] = menor[contador]
        contador += 1
    return resultado
