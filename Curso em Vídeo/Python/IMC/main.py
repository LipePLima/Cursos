#Crie um programa capaz de interagir e calcular o IMC de uma pessoa.

from time import sleep

class IndiceDeMassaCorporal:
    def __init__(self):
        self.escolha = 'Gostaria de calcular seu IMC(Indice de massa corporal)? Sim/Não: '
        self.peso = 'Digite seu peso: '
        self.altura = 'Digite sua altura: '

    def Iniciar(self):
        print('_'*100)
        print(      )
        while True: 
            escolha = str(input(self.escolha)).upper().strip()[0]
            if escolha == 'S':
                print('Ok! Vamos começar')
                break
            elif escolha == 'N': 
                print()
                print('A pesquisa encerrou! Obrigado pela sua atenção!')

    def Resultado(self):
        print()
        print('-'*100)
        nome = input('Primeiro, gostariamos de saber seu nome!: ')
        print()
        peso = float(input(self.peso))
        print()
        altura = float(input(self.altura))
        print()
        sleep(1)
        resultado = peso/(altura**2)
        print(f'Calculando seu IMC {nome}, aguarde um instante!')
        print('-'*100)
        sleep(1)
        print(f'{nome}, o seu IMC(indice de massa corporal) é {round(resultado, 1)}')
        print()
        if resultado < 18.5:
            print(
                f'Eita, {nome}! Você está abaixo do ideal, procure um especialista!')
        elif 18.5 <= resultado < 24.9:
            print(
                f'Boooa, {nome}! Você está dentro do ideal, ou seja, está saudável!!!')
        elif 25 <= resultado < 29.9:
            print(
                f'{nome}, você está na classificação "Sobrepeso". Não é grave, mas procure um especialista!')
        elif 30 <= resultado < 40:
            print(
                f'Tome cuidado, {nome}! Você está na classificação "Obesidade", procure um especialista!')
        elif 40 <= resultado < 50:
            print(
                f'MEU DEUS, {nome}!! Você está na classificação "Obesidade grave", procure um especialista com urgência!') 
        elif resultado > 50:
            print(f'{nome}, você está vivo???')
        print('_'*100)

Pesquisa = IndiceDeMassaCorporal()
Pesquisa.Iniciar()
Pesquisa.Resultado()
