'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''


lista = []

for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if cont == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('='*40)
print(f'Os valores digitados em ordem crescente são: {lista}')