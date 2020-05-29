# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar, [2]multiplicar, [3]maior, [4]novos números, [5]sair do programa
from time import sleep
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = v1 + v2
        print(f'RESPOSTA: a SOMA entre {v1} e {v2} é {soma}')
    elif opção == 2:
        multi = v1 * v2
        print(f'RESPOSTA: a MULTIPLICAÇÃO entre {v1} e {v2} é {multi}')
    elif opção == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'RESPOSTA: o MAIOR valor entre {v1} e {v2} é {maior}')
    elif opção == 4:
        print('Informe novos números: ')
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando')
    else:
        print('Escolha uma opção válida!')
    print('=-' * 10)
    sleep(2)
print('Programa Finalizado')
