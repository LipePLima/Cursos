'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$200, R$ 100, R$50, R$20, R$10, R$ 5 e R$1.'''

print('='*60)
print(f'{" Banco FL ":^60}')
print('='*60)
valor = int(input('Digite o valor que deseja sacar: '))
total = valor
cedula = 200
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de {cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break 
print('='*60)
print('Tenha um bom dia e volte sempre!')
