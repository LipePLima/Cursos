from random import randint
from time import sleep

valor_aleatorio = randint(1, 20)
acertou = False
while acertou == False:
    print()
    print('_'*100)
    print()
    chute = int(input('Chute um valor de 1 a 20: '))
    print('-'*100)
    print()
    sleep(1)
    print('PROCESSANDO...')
    print()
    sleep(1)
    if 1 < valor_aleatorio < chute < 20:
        print("Seu chute foi maior que o valor gerado, tente novamente!")
    elif 1 < chute < valor_aleatorio < 20:
        print('Seu chute foi menor que o valor gerado, tente novamente!')
    elif chute < 1:
        print('ERRO404: Seu chute foi menor que o valor mínimo exigido, tente novamente')
    elif chute > 20:
        print('ERRO405: Seu chute foi maior que o valor máximo exigido, tente novamente')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!!')