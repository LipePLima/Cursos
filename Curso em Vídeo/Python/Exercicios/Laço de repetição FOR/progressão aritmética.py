#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1)*razao
for cont in range(primeiro, decimo + razao, razao):
    print(cont, end=' ')
print('ACABOU')