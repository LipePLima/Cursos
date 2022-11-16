'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
A)Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

#Variáveis
info = []
dados = []
pesomaior = pesomenor = 0

#Laço de repetição para informar nome e idade
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    if len(info) == 0:
        pesomaior = pesomenor = dados[1]
    else:
        if dados[1] > pesomaior:
            pesomaior = dados[1]
        if dados[1] < pesomenor:
            pesomenor = dados[1]

    info.append(dados[:])
    dados.clear()
    pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while pergunta not in 'SN':
        print('Digite Sim ou Não para continuar!')
        print()
        pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        break

print('='*40)
print(f'Foram cadastradas {len(info)} pessoas nesta lista')
print(f'O maior peso foi {pesomaior}. E foi de ', end='')
for person in info:
    if person[1] == pesomaior:
        print(f'{person[0]} ', end='')
    
print()
print(f'O menor pesso foi {pesomenor}. Foi de ', end='')
for person in info:
    if person[1] == pesomenor:
            print(f'{person[0]} ', end='')
print()
