# Faça um programa que calcule a soma entre todos os
# numeros impares que são multiplos de tres eque estão entre 1 e 500
soma = 0
qtd = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        qtd += 1
        soma += c
print(f'A soma de todos os {qtd} valores solicitados é {soma}')
