# Crie um programa que leia o nome e  o preço de vários produto.
# O Programa deverá perguntar se o usário vai continuar. No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.
print('-' * 30)
print('{:-^30}'.format(' LOJA SUPER BARATÃO '))
print('-' * 30)
total = totmil = menor = cont = 0
produtomenor = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco  # A
    cont += 1
    if preco > 1000:  # B
        totmil += 1

    if cont == 1 or preco < menor:  # C
        menor = preco
        produtomenor = produto
    '''else:
        if preco < menor:
            menor = preco
            produtomenor = produto'''

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print('----Fim do Programa----')
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {total:^10.3f}!')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {produtomenor} que custa R$ {menor:<10.2f}!')
