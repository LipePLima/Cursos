'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
lista_par = []
lista_impar = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    print()
    pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while pergunta not in 'SN':
        print('Digite Sim ou Não para continuar!')
        print()
        pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    if pergunta == 'N':
        break    
print('='*40)
print(f'Com todos os valores digitados acima, a lista completa fica desta forma {lista}')
print(f'Os pares desta lista são {lista_par}')
print(f'Os impares desta lista são {lista_impar}')
