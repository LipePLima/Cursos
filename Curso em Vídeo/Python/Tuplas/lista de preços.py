''' Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista = ('Lápis', 1.50, 'Borracha', 0.50, 'Caneta', 1.75, 'Apontador', 2.30, 'Estojo', 13.50, 'Mochila', 179.99)

print('-'*30)
print('      Lista de Preços ')
print('-'*30)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$ {lista[pos]:>2}')