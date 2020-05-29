turma = list()
dado = list()
maispesada = maisleve = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(turma) == 0:
        maisleve = maispesada = dado[1]
    else:
        if dado[1] > maispesada:
            maispesada = dado[1]
        if dado[1] < maisleve:
            maisleve = dado[1]
    turma.append(dado[:])
    dado.clear()
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo, você cadastrou {len(turma)} pessoas.')
print(f'O maior peso foi de {maispesada}KG. Peso de ', end='')
for p in turma:
    if p[1] == maispesada:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {maisleve}Kg. Peso de ', end='')
for p in turma:
    if p[1] == maisleve:
        print(f'[{p[0]}]', end='')
print()
