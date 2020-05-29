# Crie um programa onde o usuario possa digitar sete valores numéricos e
# cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e ímpares em ordem crescente.
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
# print(f'Todos os valores {num}')
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')







'''pares = list()
impares = list()
valores = list()
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
        pares.sort()
    else:
        impares.append(valor)
        impares.sort()
valores.append(pares[:])
valores.append(impares[:])
print('=-' * 30)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')'''
