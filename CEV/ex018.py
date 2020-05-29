#Faça um programa que leia um angulo qualquer e
#mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Qual o ângulo: '))
graus = math.radians(angulo)

seno = math.sin(graus)
seno2 = math.sin(math.radians(angulo))
cosseno = math.cos(graus)
cosseno2 = math.cos(math.radians(angulo))
tangente = math.tan(graus)
tangente2 = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem SENO de: {seno:.2f} e {seno2:.2f}')
print(f'O ângulo de {angulo} tem COSSENO de: {cosseno:.2f} e {cosseno2:.2f}')
print(f'A ângulo de {angulo} tem TANGENTE de: {tangente:.2f} e {tangente2:.2f}')
