# Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então empréstimo será negado.
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
mensalidade = casa / (anos * 12)
limite = salario * 30/100
if salario * 30 / 100 < mensalidade:
    print(f'Empréstimo NEGADO! Prestação de R${mensalidade:.2f} excede R${limite}')
else:
    print(f'Empréstimo LIBERADO! A prestação mensal será de R$ {mensalidade:.2f}')
