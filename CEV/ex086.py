# Crie um programa que crie uma matriz de dimensão 3X3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(matriz)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()  # usando indentação para quebra de linha a cada 3 valores

'''valores = list()
for c in range(0, 3):
    for i in range(0, 3):
        valores.append(int(input(f'Digite um valor para [{c}, {i}]: ')))
for c, x in enumerate(valores):
    print(f'[{x:^5}]', end='')
    if (c+1) % 3 == 0:
        print()'''

'''for c in range(1, len(valores)+1):
    print(f'[ {valores[c-1]} ]', end='')
    if c % 3 == 0:
        print()'''
