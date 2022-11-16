'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

from time import sleep

print('-'*60)
print(f'{"LOJA TÁ BARATO DEMAIS":^60}')
print('-'*60)
total = cont = mais_barato = mais_de_1000 = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor:R$ '))
    total += valor
    cont += 1
    print()
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja passar mais algum produto? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print()
            print('ERRO: Digite apenas Sim ou não')
            print()
    print()
    if valor > 1000:
        mais_de_1000 += 1
    if cont == 1 or valor < mais_barato:
        mais_barato = valor
        barato = nome
    if escolha == 'N':
        break
print(f'''O total gasto na compra foi de R${total}
O número de produtos com valor acima de R$1000 foi de {mais_de_1000:.2f}
E o nome do produto mais barato é {barato} e o valor foi de R${mais_barato:.2f}''')
    