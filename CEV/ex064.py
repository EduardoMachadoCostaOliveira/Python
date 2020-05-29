# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (deconsiderando o flag 999).
num = soma = c = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {c} numeros e a soma entre eles foi {soma}')

'''num = int(input('Digite um numero: '))
soma = 0
c = 0
while num != 999:
    soma += num
    c += 1
    num = int(input('Digite outro: '))
print(f'Você digitou {c} numeros e a soma deles é {soma}')'''