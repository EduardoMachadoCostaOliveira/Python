# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:# A) Apenas os 5 primeiros colocados.print('-=' * 20)
# # B) Os últimos 4 colocados da tabela# C) Uma lista com os times na ordem alfbética.
# D) Em que posição esta o time da Chapecoense.
times = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro',
         'CSA', 'Chapecoense', 'Avaí')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são {times[0: 5]}')
print('-=' * 20)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
