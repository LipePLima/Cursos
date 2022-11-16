'''Crie um programa que declare uma matriz de dimensão 3 x 3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta. 
A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna. 
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = maior = 0

#Laço de repetição para forma uma matriz 3x3
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número [{l}, {c}]: '))
        #Soma dos valores pares
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        #Soma dos valores da terceira coluna
        if matriz[l][2]:
            soma += matriz[l][2]
        #Maior valor da segunda linha
        if matriz[1][c]:
            maior == matriz[1][c]
            if matriz[1][c] > maior:
                maior = matriz[1][c]


print('-'*40)
#Laço de repetição para formar a matriz no console
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


print('-'*40)
print(f'A soma de todos os valores pares digitados é {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')