# Desenvolva uma ógica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status,
# de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do Peso.
# -Entre 18.8 e 25: Peso Ideal.
# -25 até 30: Sobrepeso.
# -30 até 40: Obesidade.
# -Acima de 40: Obesidade Mórbida.
altura = float(input('Qual é a sua \033[32mALTURA?\033[m '))
peso = float(input('Qual é o seu \033[32mPESO?\033[m '))
imc = peso / pow(altura, 2)
print(f'O seu IMC é de {imc:.1f}, portanto...')
if imc < 18.5:
    print('Você está ABAIXO do PESO!')
elif imc < 25:
    print('Voce está no seu PESO IDEAL!')
elif imc < 30:
    print('Você está com SOBREPESO!')
elif imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
