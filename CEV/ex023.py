#Faça um programa que leia um número de 0 a 9999 e
#mostre na tela cada um dos dígitos separados.
numero = float(input('Digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

"""num = str(numero)
print(num[0])
print(num[1])
print(num[2])
print(num[3])"""
