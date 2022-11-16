#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = cont = maior = menor = 0 
fim = 'S'
while fim in 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    media = soma/cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    fim = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
print(f'Você digitou {cont} números e a média entre eles foi de {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
