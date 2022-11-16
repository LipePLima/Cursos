# Faça todos os desafios a seguir e depois clique a "Share", copie o código e 
# mande no comentário do vídeo, para que eu veja que você conseguiu (ou não) fazer! Eu confio em VOCÊ!

# Desafio 1 - Exiba todos os nomes dos inscritos que estão no arquivo inscritos.txt no console

with open('inscritos.txt', 'r') as arquivo:
    for nomes in arquivo:
        print(nomes)
