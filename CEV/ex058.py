# Melhore o jogo do Desafio028 onde o computador vai pensar em um numero entre 0 e 10.
# ó que agora o jogador vai tenta advinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

# 1ª Solução minha
'''from random import randint
palpites = 1
computador = randint(1, 10)
print('Tente advinhar em qual número o computador pensou, entre 0 e 10!')
jogador = int(input('Advinhe o número: '))
while computador != jogador:
    palpites += 1
    print('ERROU! Tente novamente!')
    jogador = int(input('Advinhe o numero: '))
print(f'ACERTOU!!!! Você precisou de {palpites} palpites para advinhar!')'''

# 2ª Solução, Guanabara
from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pnsar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais..')
        elif jogador > computador:
            print('Menos..')
print(f'Acertou com {palpites} tentativas. Parabéns!')
