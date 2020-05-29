# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie tambem uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Usuario saiu do programa')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            v = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: por favor digite um número real válido.\033[m')
            continue
        else:
            return v


n1 = leiaInt('Digite um numero INTEIRO: ')
n2 = leiaFloat('Digite um numero REAL: ')
print(f'INTEIRO = {n1}'
      f' REAL = {n2}')
