# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-=' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))

tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE > ', '-=' * 5)







# '''for n in range(1, numeros + 1):
#     print(f'Jogo {n}: ', end='')
#     for c in range(0, 6):
#         num = randint(1, 60)
#         jogos.append(num)
#         jogos.sort()
#     print(jogos)
#     jogos.clear()
#     sleep(1)'''

# '''valores = list()
# jogo = list()
# for n in range(1, 61):
#     valores.append(n)
# numeros = int(input('Quantos jogos você quer que eu sorteie? '))
# for c in range(0, numeros+1):
#     jogo = choices(valores, k=6)
#     jogo.sort()
#     print(jogo)'''
