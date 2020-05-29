# Desenvolva um programa que leia o comprimento de três retas
# e diga se ao usuário se elas podem ou não formar um triângulo
a = float(input('Lado a = '))
b = float(input('Lado b = '))
c = float(input('Lado c = '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
'''if (a + b) > c and (b + c) > a and (c + a) > b:'''
