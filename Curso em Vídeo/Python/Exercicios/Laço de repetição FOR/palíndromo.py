#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inversao = juntar[::-1]
print(f'A frase "{frase}" invertida fica "{inversao}"')
if inversao == juntar:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')