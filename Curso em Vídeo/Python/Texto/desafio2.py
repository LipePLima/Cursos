# Desafio 2 - Adicione o seu nome na lista de inscritos e depois todos os nomes que estão no 
# arquivo inscritos.txt no console

with open('inscritos.txt', 'a') as arquivo:
    arquivo.write("Felipe Lima" + '\n')