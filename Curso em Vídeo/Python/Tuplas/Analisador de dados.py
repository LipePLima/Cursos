'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Mais um número: '))
num4 = int(input('O último, prometo: '))
tot = (num1, num2, num3, num4)
print(f'O número 9 aparece {tot.count(9)}x')
if 3 in tot:
    print(f'O número 3 foi digitado na {tot.index(3)}° posição')
else:
    print('O valor 3 não foi encontrado')
print(f'Os valores pares são: ', end='')
for n in tot:
    if n % 2 == 0:
        print(f'{n}', end=' ')
