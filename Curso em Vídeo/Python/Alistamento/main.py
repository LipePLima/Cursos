# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
from time import sleep

data = date.today().year
nascimento = int(input('\033[0;32mInforme o seu ano de nascimento:\033[m '))
idade = data - nascimento
print(f'Você nasceu em {nascimento} e sua idade é {idade} anos')
print('-='*54)
sleep(1)
if idade == 18:
    print('Este ano você terá que se alistar!')
elif idade < 18:
    print(
        f'Você ainda é novo, só precisará se alistar daqui a {18-idade} anos, em {data + (18-idade)}')
elif idade > 18:
    print('Você já passou da idade pra se alistar!')
    pergunta = input(
        '\033[0;32mEstá tudo certo com sua obrigações? Sim/Não:\033[m ').upper()
    print()
    if pergunta == 'SIM':
        print('Isso ai, guerreiro. Tá liberado!')
    elif pergunta == 'NÃO':
        print('Vamos querer, bizonho. Corre atrás disso ai!')
    else:
        print('ERRO: Digite apenas "Sim" ou "Não"')
