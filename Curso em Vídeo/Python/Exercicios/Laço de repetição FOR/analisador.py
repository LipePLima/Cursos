#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mediaidade = somaidade = maisvelhohomem = num_mulheres = 0 
nome_do_mais_velho = ''
for pessoa in range(1, 5):
    print(f'------ {pessoa}° PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]:')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maisvelhohomem = idade
        nome_do_mais_velho = nome
    if sexo in 'Mm' and idade > maisvelhohomem:
        maisvelhohomem = idade
        nome_do_mais_velho = nome
    if idade < 20 and sexo in 'Ff':
        num_mulheres += 1
    print()
mediaidade = somaidade / 4
print(f'A média de idade do grupo é igual a {mediaidade}.\nE o homem mais velho tem {maisvelhohomem} e seu nome é {nome_do_mais_velho}.\nE o número de mulheres que tem menos de 20 anos é {num_mulheres}')
