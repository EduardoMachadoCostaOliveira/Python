# Faça um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionario.
# No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogos.items():  # Keys, Values
    print(f'{k} tirou {v} no dado.')
    # sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')


'''resultados = dict()
rodada = list()
for c in range(1, 5):
    print(f'O {c}º lugar foi____')

maior = 0
for k in jogos.values():
    if k > maior:
        maior = k
        print(maior)'''

'''for j in range(1, 5):
    dado = randint(1, 6)
    # print(f'O jogador {j} tirou {dado}')

    resultados['jogador'] = j
    resultados['num'] = dado
    rodada.append(resultados.copy())

print('Valores Sorteados:')
for a in rodada:
    print(f'    O jogador{a["jogador"]} tirou {a["num"]}')

print('Ranking dos Jogadores:')
for a in rodada:
    print(f'    {a["jogador"]}º lugar: jogador x com {a["num"]}')'''

# print(rodada)
# print(resultados)

