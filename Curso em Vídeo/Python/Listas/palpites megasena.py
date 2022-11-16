'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from time import sleep
from random import randint


print('-'*40)
print(f'{"JOGUE NA MEGA SENA":^40}')
print('-'*40)

jogos = int(input('Quantos jogos deseja sortear?: '))
print()
print('-='*6, f'SORTEANDO {jogos} JOGOS', '-='*6)
for sorteio in range(0, jogos):
    lista = [randint(1, 60), randint(1, 60), randint(1, 60),
             randint(1, 60), randint(1, 60), randint(1, 60)]
    lista.sort()
    print(f'Jogo {sorteio+1}: {lista}')
    sleep(2)
print('-='*6, '< BOA SORTE >', '-='*6)
