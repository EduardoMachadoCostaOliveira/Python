#Faça um algoritmo que leia o preço de um produto e mostre sue novo preço, com 5% de desconto.
n1 = float(input("Informe o preço do produto: R$ "))
print(f'O produto que custava R${n1}, na promoção com desconto de 5% vai custar: R$ {n1 * 0.95:.2f}')
