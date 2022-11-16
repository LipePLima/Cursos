#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

from time import sleep


print(f'{" TABUADA ":=^20}')
print()
while True:
    numero = int(input('Quer ver a tabuada de qual número?: '))
    if numero < 0:
        break
    print('-'*100)
    for contador in range(1, 11):
        print(f'{numero} X {contador} = {numero*contador}')
    print('-'*100)
print('O programa está encerrando...')
sleep(1)
print()
print('Obrigado por participar. Volte sempre!!')