# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
tupla = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    pos = int(input('Digite um número entre 0 e 20: '))
    if 0 <= pos <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {tupla[pos]}')
