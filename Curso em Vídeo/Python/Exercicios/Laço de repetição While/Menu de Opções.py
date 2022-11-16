'''Crie um programa que leia dois valores e mostre um menu na tela:
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep


print('_'*100)
maior = 0
pergunta1 = int(input('Digite o primeiro número: '))
pergunta2 = int(input('Digite o segundo número: '))
pergunta3 = 0
print('-'*100)
while pergunta3 != 7:
    print('    [1] Somar \n    [2] Diminuir \n    [3] Multiplicar \n    [4] Dividir \n    [5] Maior \n    [6] Novos números \n    [7] Encerrar programa')
    print('-'*100)
    pergunta3 = int(input('Qual opção deseja: '))
    print('-'*100)
    if pergunta3 == 1:
        print(f'A soma entre {pergunta1} e {pergunta2} é igual a {pergunta1 + pergunta2}')
    elif pergunta3 == 2:
        print(f'A subtração entre {pergunta1} e {pergunta2} é igual a {pergunta1 - pergunta2}')
    elif pergunta3 == 3:
        print(f'A multiplicação entre {pergunta1} e {pergunta2} é igual a {pergunta1 * pergunta2}')
    elif pergunta3 == 4:
        print(f'A divisão entre {pergunta1} e {pergunta2} é igual a {pergunta1 / pergunta2}')
    elif pergunta3 == 5:
        if pergunta1 > pergunta2:
            maior = pergunta1
            print(f'O maior número entre {pergunta1} e {pergunta2} é igual a {maior}')
        elif pergunta1 < pergunta2:
            maior = pergunta2
            print(f'O maior número entre {pergunta1} e {pergunta2} é igual a {maior}')
    elif pergunta3 == 6:
        print('Informe os novos número...')
        pergunta1 = int(input('Digite o primeiro número: '))
        pergunta2 = int(input('Digite o segundo número: '))
    elif pergunta3 > 7:
        print('ERRO: Opção inválida. Tente novamente!')
        print('_'*100)
print('Encerrando programa...')
sleep(2)
print('Programa encerrado!')