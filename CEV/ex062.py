# Melhore o Desafio061, perguntando ao usuario se ele quer mostrar mais alguns termos.
# O programa  encerra quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(termo, end=', ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')


'''while c != 0:
    b = int(input('Quer mostrar mais quantos termos: '))
    for c in range(c, c+b):
        print(termo, end=', ')
        termo += razao
        c += 1
    print('PAUSA')
    if b == 0:
        print(f'Programa Encerrado!!!! Foram mostrados {c} termos.')
        c = 0'''
