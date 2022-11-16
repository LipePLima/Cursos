from datetime import datetime

ano = datetime.now().year
cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['nascimento'] = ano - nascimento
carteira = int(input('Número da Carteira de Trabalho (0 = não tem): '))

if carteira == 0:
    print('-='*30)
    print(f'   - Nome: {cadastro["nome"]}')
    print(f'   - Idade: {cadastro["nascimento"]}')
    print(f'   - ctps: Não possui')

if carteira != 0:
    cadastro['ctps'] = carteira
    cadastro['contratacao'] = int(input('Ano da contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['nascimento'] + ((cadastro['contratacao'] + 35) - datetime.now().year)

    print('-='*30)
    print(f'   - Nome: {cadastro["nome"]}')
    print(f'   - Idade: {cadastro["nascimento"]}')
    print(f'   - Ctps: {cadastro["ctps"]}')
    print(f'   - Contratação: {cadastro["contratacao"]}')
    print(f'   - Salário: {cadastro["salario"]}')
    print(f'   - Aposentadoria: {cadastro["aposentadoria"]}')
