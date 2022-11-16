from random import randint
from time import sleep


computador = randint(0, 10)
print('Sou seu computador!\nAcabei de pensar em um número entre 0 e 10, tente advinhar!')
acertou = False
tentativa = 0
while not acertou:
    escolha = int(input('Escolha um número: '))
    tentativa += 1
    if escolha == computador:
        acertou = True
    elif escolha > 10:
        print('OPS! Seu número foi maior que 10, tente novamente!')    
    else:
        if escolha < computador:
            print('Seu número é menor que o meu, tente novamente!')
        elif 10 > escolha > computador:
            print('Seu número é maior que o meu, tente novamente!') 
print(f'Você acertou! Mas precisou de {tentativa} tentativas')
