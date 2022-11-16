#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0
while True:
    num = int(input('Digite um número [999 para fechar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A quantidade de números que vc digitou foi de {cont} números. E a soma entre eles foi de {soma}')
print('Fim')
