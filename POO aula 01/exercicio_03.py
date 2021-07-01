'''Implemente a classe televisão'''

class Televisao:
    # atributos
    def __init__(self):
        self.canal = None
        self.volume = 0

    # metodos
    def aumentar_volume(self):
        self.volume += 1
        return 'teste aumentar volume'

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal

tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(tv.aumentar_volume())

#print(tv.volume)

#print(f'A tv está no canal {tv.canal}')
#print(f'A tv está no volume {tv.volume}')
