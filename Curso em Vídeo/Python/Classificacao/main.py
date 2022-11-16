#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM    – Até 14 anos: INFANTIL    – Até 19 anos: JÚNIOR    – Até 25 anos: SÊNIOR   – Acima de 25 anos: MASTER

from datetime import date

data = date.today().year
ano = int(input('\033[0;32mInforme seu ano de nascimento:\033[m '))
calculo = data - ano
print(f'Você tem {calculo} anos')
if calculo <= 9:
    print('Você fatá parte da categoria de atletas MIRIM')
elif calculo <= 14:
    print('Você fará parte da categoria de atletas INFANTIL')
elif calculo <= 19:
    print('Você fará parte da categoria de atletas JÚNIOR')
elif calculo <= 25:
    print('Você fará parte da categoria de atletas SÊNIOR')
else:
    print('Você fará parte da categoria de atletas MASTER')