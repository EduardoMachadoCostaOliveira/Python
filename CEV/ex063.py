# Fibonacci
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print(f'{n1}, {n2}', end='')
contador = 3
while contador <= n:
    n3 = n1 + n2
    print(',', n3, end='')
    n1 = n2
    n2 = n3
    contador += 1
print(', FIM')
