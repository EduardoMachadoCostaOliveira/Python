# Elabore um programa que calcule o calor a ser pag por um por um produto,
# considerando o seu preço normal e condição de pagamento.
a = str(' LOJAS ABC ')
print(f'{a:=^30}')
valor = float(input('Preço das compras: R$ '))
forma = int(input('''Escolha uma das condições de pagamento a seguir?
[1] - Dinheiro a vista
[2] - Cartão a vista
[3] - Cartão (2x)
[4] - Cartão (3x ou mais) 
Digite o nûmero da opção escolhida: '''))
if forma == 1:
    preço = valor - valor * 10 / 100
    print(f'O valor do produto com pagamento em dinheiro a vista será de R${preço}')
elif forma == 2:
    preço = valor - valor * 5 / 100
    print(f'O valor do produto com pagamento no cartão a vista será de R${preço}')
elif forma == 3:
    preço = valor
    print(f'O valor do produto com pagamento no cartão (2x) será de R${preço}')
elif forma == 4:
    preço = valor + valor * 20/100
    totparc = int(input('Quantas parcelas? '))
    print(f'O valor do produto com pagamento no cartão (3x ou mais) será de R${preço}')
else:
    print('Forma Invalida! Digite uma das condições de pagamento válidas.')
print(f'Sua compra de {valor} vai custar no final {preço}')
