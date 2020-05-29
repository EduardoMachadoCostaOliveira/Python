# Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print('O valores sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
