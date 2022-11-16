#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número: '))
for contador in range(1, 11):
    print(f'{numero} X {contador} = {numero*contador}')