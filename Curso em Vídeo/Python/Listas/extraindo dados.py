'''Crie um programa que vai ler vários números e colocar em uma lista. 
    Depois disso, mostre: 
        A) Quantos números foram digitados.                                                                                                   B) A lista de valores, ordenada de forma decrescente.                                                                                         
        C) Se o valor 5 foi digitado e está ou não na lista.'''


lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    print()
    pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        print('-'*40)
        print(f'A quantidade de números inseridos na lista foi de {len(lista)}')
        lista.sort(reverse=True)
        print(f'Os valores inseridos em ordem decrescente são {lista}')
        if 5 in lista:
            print('O valor "5" foi encontrado na lista')
        else:
            print('O valor "5" não foi encontrado na lista')
        break
