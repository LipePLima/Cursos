#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('PROGRESSÃO ARITMÉTICA')
print('-'*100)
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} - ', end=' ')
        cont += 1
        termo += razao
    print('Pausa')
    mais = int(input('Mais quantos termos?(Digite 0 para encerrar): '))
print(f'Progressão finalizada com {total} termos')