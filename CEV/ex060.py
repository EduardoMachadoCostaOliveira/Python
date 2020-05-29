# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# ex, 5! = 5x4x3x2x1= 120
'''from math import factorial
print('Digite um número para')
num = int(input('calcular o seu Fatorial: '))
c = 1
a = 0
b = 0
while num > c:  # Fatorial utilizando estrutura de repetição WHILE
    if c == 1:
        a = (num * (num - c))
        print(f'Calculando {num}! = {num} x {num - c}', end='')
        c += 1
    else:
        a = a * (num - c)
        print(f' x {num-c}', end='')
        c += 1
print(f' = {a}')

for f in range(1, num):  # Fatorial utilizando estrutura de repetição FOR
    if f == 1:
        b = num * (num - f)
        print(f'Calculando {num}! = {num} x {num - f}', end='')
        f += 1
    elif f != 1:
        b = b * (num - f)
        print(f' x {num-f}', end='')
        f += 1
print(f' = {b}')

print(factorial(num))  # Fatorial utlizando biblioteca MATH'''

# Solução Guanabara
n = int(input('Digite um número para calcular o seu fatorial: '))
c = c2 = n
f = f2 = 1
# WHILE
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -=1
print(f)
# FOR
print(f'Calculando {n}! = ', end='')
for c2 in range(c2, 0, -1):
    print(f'{c2}', end='')
    print(' x ' if c2 > 1 else ' = ', end='')
    f2 *= c2
print(f'{f2}')
