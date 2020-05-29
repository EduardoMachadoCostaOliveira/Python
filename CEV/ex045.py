# Crie um programa que faça o computador jogar JOKEMPÔ com você!
from random import choice
lista = ['Pedra', 'Papel', 'Tesoura']
comp = choice(lista)
eu = str(input('Pedra, Papel ou Tesoura? ')).strip().title()
# Computador ganhando
if comp == 'Tesoura' and eu == 'Papel':
    print('O computador Ganhou!')
elif comp == 'Pedra' and eu == 'Tesoura':
    print('O computador Ganhou!')
elif comp == 'Papel' and eu == 'Pedra':
    print('O computador Ganhou!')
# EU ganhando
elif eu == 'Tesoura' and comp == 'Papel':
    print('Você Ganhou!')
elif eu == 'Pedra' and comp == 'Tesoura':
    print('Você Ganhou!')
elif eu == 'Papel' and comp == 'Pedra':
    print('Você Ganhou!')
# EMPATE
else:
    print('EMPATOU!')
print('-' * 30)
print(f'Computador escolheu:    {comp}')
print(f'Você escolheu:          {eu}')
