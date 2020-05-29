def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta.
    :return: o valor fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


# Programa Principal
print(fatorial(5, True))
help(fatorial)


# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

