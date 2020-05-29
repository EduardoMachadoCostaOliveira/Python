# Faça um programa que tenha uma função chamada área(),
# que receba dimensões de um terreno retangular (largura e comprimento)
# e mostre a area do terreno.


def área(l, c):
    a = l * c
    print(f'A area do terreno de largura {l} e comprimento {c} é de {a}m².')


# Programa Principal
print('Insira as informações do terreno')
largura = float(input('Qual é a largura (m): '))
comprimento = float(input('Comprimento (m): '))
área(largura, comprimento)
