#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando
#R$ 0,50 por Km para viagens até 200Km e
#R$ 0,45 para viagens mais longas.
km = float(input('Qual é a distância da viagem? '))
if km <= 200:
    print(f'O preço da passagem será de R${km * 0.5:.2f}')
else:
    print(f'O preço da passagem será de R${km * 0.45:.2f}')
