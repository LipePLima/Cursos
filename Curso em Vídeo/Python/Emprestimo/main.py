#escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor das prestações mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

valor_casa = float(input('\033[0;32mQual o valor do imóvel?:\033[m'))
anos = float(input('\033[0;32mEm quantos anos deseja pagar?:\033[m'))
salario = float(input('\033[0;32mQual o seu salário?:\033[m '))
prestacoes = valor_casa / (anos*12)
salario_prestacao = salario*30/100
print('-='*54)
sleep(1)
print(f'\033[0;32mO valor das prestações fica em {prestacoes:.1f} e 30% do seu salário é {salario_prestacao:.1f}\033[m')
sleep(1)
print('-='*54)

if prestacoes < salario_prestacao:
    print('\033[0;32mSeu empréstimo foi aprovado!!\033[m')
elif prestacoes == salario_prestacao:
    print('\033[0;32mSeu empréstimo foi aprovado!!\033[m')
else:
    print('\033[0;32mSeu empréstimo infelizmente foi negado\033[m')
