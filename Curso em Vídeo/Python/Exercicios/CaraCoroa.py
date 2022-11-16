# Voce quer simular a opção de jogar uma moeda e resultar em cara ou cora

import random
import time


class CaraCora:
    def __init__(self):
        self.valor1 = 1
        self.valor2 = 2
        self.pergunta = 'Escolha cara ou coroa: '

    def Iniciar(self):
        acertou = False
        while acertou == False:
            print('_'*100)
            print()
            escolhendo = random.randint(self.valor1, self.valor2)
            escolha = input(self.pergunta).upper()
            print('-'*100)
            time.sleep(1)
            print()
            if escolhendo == 1:
                print('CARA')
                if escolha == 'CARA':
                    print('Você acertou!')
                    acertou = True
                else:
                    print('Você errou, tente novamente!')
            else:
                print('COROA')
                if escolha == 'COROA':
                    print()
                    print('Você acertou!')
                    acertou = True
                else:
                    print('Você errou, tente novamente!')
            print()
            print('_'*100)


Jogo = CaraCora()
Jogo.Iniciar()
