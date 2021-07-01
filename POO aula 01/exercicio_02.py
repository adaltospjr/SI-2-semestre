'''Crie uma classe que representa um triângulo.'''

class Triangulo:
    # atributos
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    # metodos
    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

teste_1 = Triangulo(a, b, c)        # criando objeto

print(teste_1.calcular_perimetro()) # utilizando o metodo da classe Triangulo