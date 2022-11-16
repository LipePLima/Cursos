#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

contador = 0
soma = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        contador += 1
        soma += impar
print(f'A quantidade de valores solicitador foi de {contador}. E a soma de todos eles foi de {soma}')