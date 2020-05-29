from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(texto, cor=0):
    a = len(texto) + 4
    print(c[cor], end='')
    print('~' * a)
    print(f'  {texto}')
    print('~' * a)
    print(c[0], end='')
    sleep(1)


# PP
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)


# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comnado e o manual vai aparecer.
# Quando o usuário digitar a palavra FIM, o programa se encerrará.
