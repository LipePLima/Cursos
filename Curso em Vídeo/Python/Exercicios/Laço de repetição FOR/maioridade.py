'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date

totalmaior = 0
totalmenor = 0
for idade in range (1, 8):
    pergunta = int(input(f'Em que ano a {idade}° pessoa nasceu: '))
    calculo = date.today().year - pergunta
    if calculo >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print('-'*54)
print(f'Ao todo, tem-se {totalmaior} pessoas maiores de idade \nE {totalmenor} menores de idade.')
