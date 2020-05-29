# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número ja exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores unicos digitado, em ordem crescente.
valores = list()
while True:
    a = int(input('Digite um valor: '))
    if a not in valores:
        valores.append(a)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar....')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')


'''while True:
    a = int(input('Digite um valor: '))
    if a in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(a)
        print('Valor adicionado com sucesso...')
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Tente novamente. Quer continuar [S/N]: ')).strip().upper()
    if resposta in 'N':
        break'''