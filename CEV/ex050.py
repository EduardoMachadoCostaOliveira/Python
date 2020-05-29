# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares.
# Se o valor for impar desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} numeros pares e a soma deles é {soma}')

