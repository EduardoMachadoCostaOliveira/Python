# Crie um programa que tenha uma tupla unica coma nomes de profutis e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
listagem = ('Estojo', 10,
            'Caneta', 2,
            'Borracha', 1,
            'Lápis', 0.50,
            'Lapiseira', 25)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f'R${listagem[c]:>7.2f}')
print('-' * 40)
