'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
from time import sleep

valores = list()

while True:
    valor = int(input('Digite um número: '))
    print()
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else: 
        print('Valor já adicionado na lista. Digite outro!')
    pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print()
    while pergunta not in 'SN':
        print('ERRO: Digite Sim ou Não')
        pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        break
valores.sort()

print('='*40)
print(f'Os valores adicionados a lista foram {valores}')
print()
print('Obrigado por participar')
print()
sleep(1)
print('Fim do programa')
print('-'*40)
