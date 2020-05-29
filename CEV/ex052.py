# Faça um programa que leia um numero inteiro e
# diga se ele é ou não um número primo (obs.: é divisivel somente duas vezes!).
# divisiveis apenas por 1 e por ele mesmo
num = int(input('Digite um número: '))
contador = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[7;33m{c}\033[m', end=' ')
        contador += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {num} foi divisivel {contador} vezes')
if contador == 2:
    print(f'E por isso {num} É PRIMO!')
else:
    print(f'E por isso {num} NÃO É primo!')
