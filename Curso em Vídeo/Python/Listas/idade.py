galera = list()
dado = list()
totmaior = totmenor = 0

#Inserindo os dados nas listas
for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
#Analisando idades
for person in galera:
    if person[1] >= 21:
        print(f'{person[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{person[0]} é menor de idade')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores de idade')