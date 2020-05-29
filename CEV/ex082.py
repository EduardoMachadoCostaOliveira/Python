# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas que vão conter apenas os valores pares e os impares digitados, repectivamente.
# Ao final, mostre o conteudo das três listas geradas.
lista = list()
pares = list()
impares = list()
resposta = ''
while True:
    lista.append(int(input('Digite um valor:')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
