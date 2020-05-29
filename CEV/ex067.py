# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usúario.
# O programa sera interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('_' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n:2} x {c:2} = {n * c:>10}')
    print('_' * 40)
print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')
