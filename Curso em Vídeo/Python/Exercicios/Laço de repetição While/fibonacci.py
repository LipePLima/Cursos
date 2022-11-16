'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8'''

print('-'*100)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*100)
n = int(input('Digite a quantidade de termos que deve aparecer: '))
print('-'*100)
ter1 = 0
ter2 = 1
print(f'{ter1} - {ter2}', end=' ')
cont = 3
while cont <= n:
    ter3 = ter1 + ter2
    cont += 1
    print(f'- {ter3}', end=' ')
    ter1 = ter2
    ter2 = ter3
print('Fim')
print('_'*100)