#Crie um programa que leia um numero inteiro
#e mostre na tela se ele é PAR ou IMPAR
numero = int(input('Digite um numero: '))
if (numero % 2) > 0:
    print(f'O numero {numero} é IMPAR!')
else:
    print(f'O numero {numero} é PAR!')