# Crie um programa que vai ler varios números e colocar em uma lista. Depois disso mostre:
# A) Quantos numeros foram digitados.
# B) A lista de valores, ordenada de forma descrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
resposta = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Tente novamente! Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':  # ou if resposta in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')  # A
lista.sort(reverse=True)  # B
print(f'Os valores em ordem descrescente são {lista}')
if 5 in lista:  # C
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
