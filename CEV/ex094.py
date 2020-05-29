galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERREADO >>')


# Crie um programa que leia nome, sexo, e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionario, e os dicionarios em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.






''' # Edu
pessoa = dict()
lista = list()
listamulheres = list()
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while pessoa['sexo'] not in 'FfMm':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
    if pessoa['sexo'] in 'Ff':
        listamulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    lista.append(pessoa.copy())
    resp = str(input('Quer continuar: [S/N] '))
    while resp not in 'SsNn':
        print('ERRO! Responda aoenas S ou N.')
        resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é {somaidade/len(lista):.2f} anos.')
print('- As mulheres cadastradas foram:', end=' ')
for c in listamulheres:
    print(c, end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for a, b in enumerate(lista):
    if b['idade'] >= somaidade/len(lista):
        print(f'nome = {b["nome"]}; sexo = {b["sexo"]}; idade = {b["idade"]};', end='')
    print()

print(lista)'''