print('-='*64)
print('analisador de triângulo')
print('-='*64)
a1 = float(input('Digite o primeiro valor: '))
a2 = float(input('Digite o segundo valor: '))
a3 = float(input('Digite o terceiro valor: '))
print('-='*64)
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Esses valores acima podem formar um triângulo')
else:
    print('Os valores acima não podem formar um triângulo')