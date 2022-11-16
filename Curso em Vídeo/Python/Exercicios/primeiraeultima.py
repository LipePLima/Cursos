from itertools import count


frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A primeira letra A é, está na posição: {frase.find("A")+1}')
print(f'A quantidade de letras A é igual a: {frase.count("A")}')
print(f'A última letra A, está na posição: {frase.rfind("A")+1}')