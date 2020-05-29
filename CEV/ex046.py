# Faça um programa que mostra na tela a contagem regressiva para o estouro dos fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVOOOO!!!!')
