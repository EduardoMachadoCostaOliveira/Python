# Faça um programa que tenha uma lista chamada números e duas funcões chamadas sorteio() e somaPar().
# A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista
# e a segunda vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
from random import randint
from time import sleep


def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.2)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa Principal
numeros = list()
sorteio(numeros)
somapar(numeros)
