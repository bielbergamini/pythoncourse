# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Gabriel', 'Bergamini')
# p1.nome = 'Gabriel'
# p1.sobrenome = 'Bergamini'

p2 = Pessoa('Bianca', 'Dias')
# p2.nome = 'Bianca'
# p2.sobrenome = 'Dias'

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

car1 = Carro('Fiat', 'Uno')



