# Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenco = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    pergunta = int(input('Digite um número entre 0 e 20: '))
    if 0 <= pergunta <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {extenco[pergunta]}')
print()
continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
print()
while continuar != 'N':
    while True:
        pergunta = int(input('Digite um número entre 0 e 20: '))
        if 0 <= pergunta <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {extenco[pergunta]}')
    print()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print()
print('Obrigado por participar, volte sempre!')

