#Faça um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador
import random
import time
numero = random.randint(0, 5)
print('--' * 25)
print('Pensei em um numero entre 0 e 5. Tente advinhar!')
print('--' * 25)
chute = int(input('Qual numero pensei? '))
print('Verificando.....')
time.sleep(3)
if chute == numero:
    print(f'Parabens! Você ACERTOU! Pensei no numero {numero}')
else:
    print(f'Não! Você ERROU! Pensei no numero {numero}')
