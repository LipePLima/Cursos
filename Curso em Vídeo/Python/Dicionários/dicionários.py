'''Faça um programa que leia nome e média de uma aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))
print(f'Nome é igual a {dados["nome"]}')
print(f'Média igual a {dados["media"]}')
if dados['media'] >= 6:
    print('Situação é APROVADO')
elif dados['media'] < 6:
    print('Situação é REPROVADO')
