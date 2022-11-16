'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

from wsgiref.validate import validator


tot = [[], []]

for num in range(0, 7):
    pergunta = int(input(f'Digite {num+1}° número: '))
    if pergunta % 2 == 0:
        tot[0].append(pergunta)
    else:
        tot[1].append(pergunta)
tot[0].sort()
tot[1].sort()

print('='*40)
print(f'Os números pares são: {tot[0]}')
print(f'Os números ímpares são: {tot[1]}')