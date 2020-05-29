#Crie um programa que leia um número  Real qualquer pelo teclado
#e mostre na tela a sua porção Inteira.
import math
número = float(input('Digite um número: '))
inteira = math.floor(número)
inteira2 = número//1
inteira3 = math.trunc(número)
inteira4 = int(número)
print(f'O número {número} tem a parte Inteira {inteira} e {inteira2:.0f} e {inteira3} e {inteira4} e')
a = inteira * 1
b = inteira2 * 1
c = inteira3 * 1
d = inteira4 * 1
print(f'Checking results {a:.1f}, {b}, {c}, {d}.')