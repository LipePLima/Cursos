# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
maior = menor = 0
for ad in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {ad}: ')))
    if ad == 0:
        maior = menor = valores[ad]
    else:
        if valores[ad] > maior:
            maior = valores[ad]
        if valores[ad] < menor:
            menor = valores[ad]

print('-'*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} e encontra-se nas posições ', end='')
for ind, valor in enumerate(valores):
    if valor == maior:
        print(f'{ind}', end=' ')
print()
print(f'O menor valor digitado foi {min(valores)} e encontra-se nas posições ', end='')
for ind, valor in enumerate(valores):
    if valor == menor:
        print(f'{ind}', end=' ')