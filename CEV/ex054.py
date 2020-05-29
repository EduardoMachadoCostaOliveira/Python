# Crie um programa que leia o ano de nascimento de sete passoas
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    anonascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = anoatual - anonascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoa(s) JÁ  são maiores')
print(f'{menor} pessoa(s) NÃO são maiores')
