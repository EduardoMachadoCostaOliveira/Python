#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
real = float(input('Quanto dinheiro (R$) você tem na carteira? '))
dolar = real / 3.27
print(f'Com {real:.2f} reais você poderá comprar {dolar:.2f} dólares.')
