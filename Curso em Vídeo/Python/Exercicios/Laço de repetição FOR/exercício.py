inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))
intervalo = int(input('Digite de quanto em quantos número irá pular: '))
for contagem in range(inicio, fim+1, intervalo):
    print(contagem)
print('Fim')
