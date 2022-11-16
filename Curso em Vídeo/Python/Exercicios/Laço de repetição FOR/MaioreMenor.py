#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pessoas in range(1, 5):
    peso = float(input(f'Digite o peso da {pessoas}° pessoa: '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg \nE o menor peso lido foi de {menor}Kg.')
