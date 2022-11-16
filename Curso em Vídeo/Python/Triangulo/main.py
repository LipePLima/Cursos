#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:  – EQUILÁTERO: todos os lados iguais  – ISÓSCELES: dois lados iguais, um diferente  – ESCALENO: todos os lados diferentes

print('-='*54)
print('\033[0;34manalisador de triângulo\033[m')
print('-='*54)
s1 = float(input('\033[0;32mInforme o primeiro segmento:\033[m '))
s2 = float(input('\033[0;32mInforme o segundo segmento:\033[m '))
s3 = float(input('\033[;32mInforme o segundo segmento:\033[m '))
print('-='*54)
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os segmentos informados PODEM FORMAR um triângulo ', end='')
    if s1 == s2 == s3:
        print('Este triângulo é EQUILÁTERO')
    elif s1 != s2 != s3:
        print('Este triângulo é ESCALENO')
    else:
        print('Este triângulo é ISÓSCELE')
else:
    print('Os segmentos informados não PODEM FORMAR um triângulo')