from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('{:=^60}'.format(' JOKENPO '))
print('''Suas opções:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA
''')
jogador = int(input('Escolha: '))
print('-'*100)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOOOURA')
print('-'*100)
sleep(1)
print(f'Computador jogou {itens[computador]}')
sleep(1)
print(f'Jogador jogou {itens[jogador]}')
print('-'*100)
sleep(1)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O jogador VENCEU')
    elif jogador == 2:
        print('O jogador PERDEU')
    else:
        print('ERRO: Jogada INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('O jogador PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O jogador VENCEU')
    else:
        print('ERRO: Jogada INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('O jogador VENCEU')
    elif jogador == 1:
        print('O jogador PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('ERRO: Jogada INVÁLIDA')
print('_'*100)
