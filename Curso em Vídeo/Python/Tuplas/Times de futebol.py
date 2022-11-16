'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

    a) Os 5 primeiros times.

    b) Os últimos 4 colocados.

    c) Times em ordem alfabética.

    d) Em que posição está o time da Chapecoense...'''

times = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Internacional', 'Fluminense', 'São Paulo', 'Flamengo', 'Botafogo', 'Santos', 'Avaí', 'Coritiba', 'América-MG', 'Bragantino', 'Ceará', 'Atlético-GO', 'Goiás', 'Cuiabá', 'Juventude', 'Fortaleza')

print(times[0:5])
print(times[-4:])
print(sorted(times))
print(times.count('Chapecoense'))