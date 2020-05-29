# Escreve um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite(calcule e mostre).
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print(f'O carro foi multado! A multa foi de R$ {(velocidade - 80) * 7:.2f}')
else:
    print('O carro não foi multado! Não ultrapassou 80Km/h!')
