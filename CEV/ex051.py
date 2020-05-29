# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
#decimo = pri + (10 - 1) * raz
for c in range(pri, ((10 * raz) + pri), raz):
    print(c, end='->')
print('ACABOU')

''' Primeira Solução edu->
pri = int(input('Primeiro termo da PA: '))
raz = int(input('Razão da PA: '))
pa = 0
for c in range(1, 11):
    pa = pri + (c - 1) * raz
    print(pa, end=' -> ')
print('ACABOU')'''
