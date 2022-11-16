#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0 
conta = 0
for contagem in range(1, 7):
    numero = int(input(f'Digite o {contagem}° valor: '))
    if numero % 2 == 0:
        soma += numero
        conta += 1
print(f'Você inseriu {conta} números PARES e a soma de todos eles deu {soma}')
    
    
