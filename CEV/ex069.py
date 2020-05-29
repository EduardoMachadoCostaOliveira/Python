# Faça um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou nao continuar.
# No final mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
maiores = homens = mulheres = 0
while True:
    print('--' * 20)
    print(f'CADASTRE UMA PESSOA')
    print('--' * 20)
    idade = int(input('Idade: '))
    #  A
    if idade > 18:
        maiores += 1

    sexo = ' '  # str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    #  B
    if sexo == 'M':
        homens += 1
    #  C
    if sexo == 'F' and idade < 20:
        mulheres += 1

    continua = ' '  # str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
