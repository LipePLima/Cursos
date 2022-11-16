#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('Começando a contagem regressiva...')
for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print('FELIZ ANO NOVO!!!!\U0001f4a5 \U0001f4a5 \U0001f4a5 \U0001f4a5')

