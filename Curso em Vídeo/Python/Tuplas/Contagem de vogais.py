palavras = ('Python', 'Desenvolvedor', 'Aprender', 'JavaScript', 'PHP', 'TamoJunto', 'Curso')

for palavra in palavras:
    print(f'\nNa palavra "{palavra}" temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')