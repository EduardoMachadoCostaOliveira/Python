# Refaça o Desafio051, lendo o primeiro termo de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura While
# Minha solução
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
termo = 0
while c < 10:
    if c == 0:
        print(primeiro, end='')
        termo = primeiro + razao
        c += 1
    else:
        print(',', termo, end='')
        termo += razao
        c += 1
print(', FIM')
# Solução Guanabara
primeiro2 = int(input('Primeiro termo: '))
razao2 = int(input('Razão: '))
termo2 = primeiro2
cont = 1
while cont <= 10:
    print(f'{termo2},', end=' ')
    termo2 += razao
    cont += 1
print('FIM')

# enésimo termo = primeiro termo + (nº termos - 1) * razão !!
# Decimo termo de PA com razão E primeiro termo 3 = 3 + (10 - 1) * 3