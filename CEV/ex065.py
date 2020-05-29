# Crie um programa que leia vários números inteiros pelo teclado.
# No final, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
# O programa deve perguntar ao usúario se ele quer ou não continuar a digitar valores.
resp = 'S'
quant = soma = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
