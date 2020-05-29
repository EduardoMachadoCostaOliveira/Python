# Escreva um programa que leia dois numero inteiros e compare-os, mostrando na tela uma mensagem:
# -O primeiro valor é maior.
# -O segundo valor é maior.
# Não existe valor maior, os dois sõa iguais.
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
amarelo = '\033[33m'
azul = '\033[34m'
limpa = '\033[m'
cores = '\033[m \033[33m \033[34m'.split()
print(cores[0])
if v1 > v2:
    print(f'O \033[33mprimeiro valor\033[m é \033[34mmaior\033[m')
elif v2 > v1:
    print(f'O {amarelo}segundo valor{limpa} é {azul}maior')
else:
    print(f'{cores[1]}Não existe{cores[0]} valor maior, os dois são {cores[2]}iguais')
