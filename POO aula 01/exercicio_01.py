'''Implemente a classe Livro, conforme o diagrama a seguir. 
   No programa principal, crie dois objetos da classe Livro.'''

class Livro:
    # atributos
    def __init__(self, titulo, autor, quantidade_paginas):         # construtor
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas
    # metodos

print('-' * 25)

saraiva = Livro('The Witcher', 'Andrzej Sapkowski', 500)

print('Autor: ', saraiva.autor)
print('Livro: ', saraiva.titulo)
print('Páginas: ', saraiva.quantidade_paginas)

print('-' * 25)

manga = Livro('Naruto', 'Masashi Kishimoto', 200)

print('Mangá: ', manga.titulo)
print('Autor: ', manga.autor)
print('Páginas: ', manga.quantidade_paginas)

print('-' * 25)