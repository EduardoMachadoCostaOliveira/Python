# Faça um programa que leia três números e mostre
# qual é o Maior e qual é o Menor.
a = int(input('\033[34;43mPrimeiro valor:\033[m '))
b = int(input('\033[32;44mSegundo valor:\033[m '))
c = int(input('\033[32;47mTerceiro valor:\033[m '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'\033[44mO menor valor digitado foi\033[m\033[4;33;41m {menor} \033[m')
print(f'\033[45mO maior valor digitado foi\033[m \033[4;31;43m {maior} \033[m')
'''Alternativa01
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
'''
