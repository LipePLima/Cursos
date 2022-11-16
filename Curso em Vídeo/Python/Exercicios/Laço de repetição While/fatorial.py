num = int(input('Digite um número: '))
f = 1
print(f'O fatorial de {num} é igual a:')
for fatorial in range(num, 0, -1):
    f *= fatorial
    print(fatorial, end=' ')
    print(' x ' if fatorial > 1 else ' = ', end=' ')
print(f)