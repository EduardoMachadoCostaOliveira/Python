cabecalho = ' Python Calculator '
print(cabecalho.center(50, '*'), '\n\n', 'Selecione o número da operação desejada:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')


opcao = int(input('Digite sua opção (1/2/3/4): '))
opcao
if (opcao not in [1, 2 ,3, 4]):
    print('Opção Inválida!')
else:
    print('Opção Válida')
    
    n1 = int(input('Digite primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if(opcao == 1):
        print(n1, '+', n2, '=', n1+n2)

    if (opcao == 2):
        print(n1, '-', n2, '=', n1 - n2)

    if (opcao == 3):
        print(n1, '*', n2, '=', n1*n2)

    if(opcao ==4):
        print(n1, '/', n2, '=', n1/n2)

print('Programa encerrado!!')