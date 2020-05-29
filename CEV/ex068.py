# Faça um programa que jogue pae ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
c = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = computador + jogador
    tipo = ' '  # obrigatorio espaço, caso nenhum espaço não entra no laço/while
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar: [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}.', end=' ')
    print(f'DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('--' * 20)
    if tipo == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!!')
            c += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    if tipo == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!!!')
            c += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    print('Vamos jogar novamente....')
print(f'GAME OVER!! Você consegui vencer {c} vezes')
