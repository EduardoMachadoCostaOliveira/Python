# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.No final mostre
# A) Quantas vezes a apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
valores = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite o último valor: ')))
print(f'Os valores digitados foram {valores}')
print(f'O valor 9 foi digitado {valores.count(9)} vezes.')
if 3 in valores:  # if valores.count(3) != 0:
    print(f'O valor 3 foi digitado na posição {valores.index(3)}')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares são: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
