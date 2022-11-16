#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print(f'{" PAR ou ÍMPAR ":=^60}')
print()
cont = 0
while True:
    print('-'*100)
    num = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = num + computador
    tipo = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    print('-'*100)
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você ganhou!!!')
            cont += 1
        elif soma % 2 == 1:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 0:
            print('Você perdeu')
            break
        elif soma % 2 == 1:
            print('Você ganhou!!')
            cont += 1
    elif tipo != 'P' and 'I':
        print('ERRO: Digite Par ou Ímpar')
    print()
    print('Vamos jogar novamente!!')
print('-'*100)
print(f'GAME OVER! Você ganhou {cont} vezes')
print('_'*100)