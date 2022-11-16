pessoal = list()
pessoa = dict()
soma = 0


while True:
    pessoa['nome'] = (str(input('Nome: ')))
    # Sexo e tratamento de erro
    pessoa['sexo'] = (str(input('Sexo [M/F]: '))).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = (str(input('Sexo [M/F]: '))).upper().strip()[0]
    pessoa['idade'] = (int(input('Idade: ')))
    soma += pessoa['idade']
    pessoal.append(pessoa.copy())

    # Pergunta e tratamento de erro
    pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while pergunta not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N.')
        pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        break
media = soma/len(pessoal)
print('-='*50)
print(f'A) Ao todo temos {len(pessoal)} pessoas cadastradas.')
print(f'B) A média de idades é de {media:5.2f}')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoal:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas com idade acima da média: ')
for p in pessoal:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< Encerrado >>>')
