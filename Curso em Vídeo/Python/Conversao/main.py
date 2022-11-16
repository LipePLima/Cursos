num = int(input('digite um número inteiro: '))
print('-='*50)
print('''Esculha uma conversão:
[1] Converter para HEXADECIMAL
[2] Converter para OCTAL
[3] Converter para BINÁRIO ''')
print('-='*50)
escolha = int(input('Escolha uma das opções: '))
print()
if escolha == 1:
    print(f'{num} convertido para HEXADECIMAL fica {hex(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL fica {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para BINÁRIO fica {bin(num)[2:]}')
else:
    print('ERRO: Digite 1, 2 ou 3. Tente novamente!')
