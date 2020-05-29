# A confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
anoatual = date.today().year
anonascimento = int(input('Qual o ano do seu nascimento? '))
idade = anoatual - anonascimento
print(f'Você tem {idade} anos. Portanto...')
if idade <= 9:
    print('Categoria MIRIM.')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
