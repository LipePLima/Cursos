velocidade = float(input('Qual a velocidade atual do carro?: '))
print('-'*100)

if 107 <= velocidade <= 120:
    print('Você cometeu uma infração média, sua multa será de R$130,16 e 5 pontos na CNH!')
elif 120 <= velocidade <= 150:
    print('Você cometeu uma infração grave, sua multa será de R$195,23 e 4 pontos na CNH!')
elif velocidade > 150:
    print('Você cometeu uma infração média, sua multa será de R$880,41 e sua CNH será suspensa!')
else:
    print('Tudo certo, tenha uma ótima viagem!')
print()