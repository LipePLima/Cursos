'''
Criar a classe carro e ter no minimo 3 propriedades para a classe carro e 
ter no mínimo 3 métodos para ela
'''

class Carro:
    def __init__(self, marca, classe_carro, velocidade_maxima):
        self.marca = marca
        self.classe_carro = classe_carro
        self.velocidade_maxima = velocidade_maxima

    def Ligar(self):
        print('Liguei o carro')

    def Acelerar(self):
        print('Acelerando o carro')

    def Parar(self):
        print('Parando o carro')

    def Desligar(self):
        print('Desligando o carro')

    def ExibirInformacoesDoCarro(self):
        print('De acordo com os dados coletados, as informações do carro são:')
        print(self.marca, self.classe_carro, self.velocidade_maxima)

carro1 = Carro('Honda','SUV','220km/hr')
carro1.Ligar()
carro1.Acelerar()
carro1.Parar()
carro1.Desligar()
carro1.ExibirInformacoesDoCarro()
carro2 = Carro('Toyota', 'Sedan', '250km/hr')
carro2.Ligar()
carro2.Acelerar()
carro2.Parar()
carro2.Desligar()
carro2.ExibirInformacoesDoCarro()