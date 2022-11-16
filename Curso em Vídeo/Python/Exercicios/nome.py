pergunta = str(input('Qual seu nome todo?: ')).strip()
nome = pergunta.split()
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome)-1]}')
