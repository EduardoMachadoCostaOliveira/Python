# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptavel.


def escreva(texto):
    a = len(texto)+4
    print('~' * a)
    print(f'{texto:^{a}}')  # Edu, alinhado no meio
    print('~' * a)
    print(f'  {texto}')  # Guanabara, só colocar dois espaços vazios no começo
    print('-' * a)


# Programa Principal
mensagem = str(input('Digite a mensagem que quer exibir: '))
escreva(mensagem)
