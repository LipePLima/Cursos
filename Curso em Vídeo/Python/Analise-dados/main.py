'''#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

numhomem = somaidade = num_mulheres = 0
while True:
    print('------ CADASTRE UMA PESSOA ------')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]:')).strip().upper()[0]
        print()
        if sexo not in 'FM':
            print('ERRO: Digite Feminino ou Masculino')
            print()
    print('-'*100)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print()
            print('ERRO: Digite apenas Sim ou não')
            print()
    print()
    if sexo in 'Mm':
        numhomem += 1
    if idade > 18:
        somaidade += 1
    if idade < 20 and sexo in 'Ff':
        num_mulheres += 1
    if escolha == 'N':
        break
print()
print(f'''Ao todo temos {somaidade} maiores de 18 anos;
{numhomem} homens cadastrados;
E o número de mulheres que tem menos de 20 anos é {num_mulheres}.''')
