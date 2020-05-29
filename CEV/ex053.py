# Crie um programa que leia uma frase qualquer e
# diga se ela é um palindromo, desconsiderando espaços.
# ex: APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O LOBO
# ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).upper().strip().split()
a = ''.join(frase)
print(f'O inverso de {a} é ', end='')
for c in range(len(a)-1, -1, -1):
    print(a[c], end='')
b = a + a[c]
print(f'\n{b}')
if a == b:
    print('SIM')
else:
    print('NÃO')
# print(len(''.join(frase)))
# print(len(a))
# print(a[0], a[1], a[2], a[3], a[4], a[5])
# lista = (a[0], a[1], a[2], a[3], a[4], a[5])
# print(lista)
# for i in range(len(a), 1, -1):
# print(a[i])
# print(frase)
# print(frase[0])
# print(len(frase[0]))
# print(a[0])