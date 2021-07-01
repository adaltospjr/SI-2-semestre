'''
Exercício 1

A - o maior número da lista
B - o menor número da lista
C - a quantidade de números pares contidos na lista
D - a média dos números contidos na lista
E - todos os números menores do que a média calculada no item anterior

'''
'''
par = 0
lista = []
numero = 0
for a in range(3):
    numero = int(input("Digite um número: "))
    lista.append(numero)
'''
'''
A
print(max(lista))

'''
'''
B
print(min(lista))

'''

'''
C

for a in lista:
    if a % 2 == 0:
        par += 1

print(lista)
print(par)
'''
'''
media = sum(lista) / len(lista)
print(media)

'''

# Exercício 2

'''
lista = [1, 2, 3, 4, 5]
lista_par = []
lista_impar = []

for a in lista:
    if a % 2 == 0:
        lista_par.append(a)
    else:
        lista_impar.append(a)

print("Lista par: ", lista_par)
print("Lista impar: ", lista_impar)
'''
'''
tupla_1 = (3, 1, 5, 3, 5)
tupla_2 = (5, 5, 7, 3, 1)

tupla_3 = tupla_1 + tupla_2

print(tupla_3)
'''

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = []
'''lista_1.insert(1, lista_2[0])
lista_1.insert(3, lista_2[1])
lista_1.insert(5, lista_2[2])'''

for a in range(1, len(lista_1) + 1):
    for b in range(1, len(lista_2) + 1):
        lista_3.insert(b, lista_1[b])

print(lista_3)