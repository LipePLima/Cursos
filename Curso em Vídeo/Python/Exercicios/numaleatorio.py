# Voce quer escolher aleatóriamente um número de 10 a 100

import random


class NumeroAleatorio:
    def __init__(self):
        self.valor_aleatorio = 0
        self.numero_minimo = 10
        self.numero_maximo = 100

    def Iniciar(self):
        self.GerarValorAleatorio()

    def GerarValorAleatorio(self):
        Gerando = random.randint(self.numero_minimo, self.numero_maximo)
        print(Gerando)


Aleatorio = NumeroAleatorio()
Aleatorio.Iniciar()
