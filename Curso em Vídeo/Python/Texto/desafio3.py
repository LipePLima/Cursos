# Desafio 3 - Com o seu nome já na lista de inscritos, exiba o nome de cada pessoas que está 
# inscrito na lista + o número que ele representa na lista em ordem crescente 
# (ex: 1 jhonatan , 2 Patricio Silva, 3 Kid Boy 3000)

with open('inscritos.txt', 'r') as arquivo:
    for index, nomes in enumerate(arquivo):
        print(index + 1, nomes)