#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
vd = d*60
vk = k*0.15
pagar = (d*60) + (k*0.15)
print(f'O total a pagar é de R${vd+vk:.2f}')
print(f'O total a pagar é de R${pagar:.2f}')
print(f'O total a pagar é de R${d*60 + k*0.15:.2f}')