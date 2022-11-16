from time import sleep

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('-='*54)
print('PROCESSANDO')
print('-='*54)
sleep(1)
if num1 > num2:
    print('O PRIMEIRO número é maior')
elif num1 < num2:
    print('O SEGUNDO número é maior')
elif num1 == num2:
    print('AMBOS são iguais.')
