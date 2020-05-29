# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo coma média atingida.
# -Média abaixo de 5.0: REPROVADO.
# -Média entre 5.0 e 6.9: RECUPERAÇÃO
# -Média 7.0 ou superior: APROVADO
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
cores = '\033[m \033[33m \033[34m'.split()
print(f'A sua média foi de {media}')
if media < 5.0:
    cornota = '\033[31m'
    print(f'Média {cornota}{media}{cores[0]} abaixo de {cores[1]}5.0{cores[0]} : {cores[2]}REPROVADO')
elif media < 6.99:
    cornota = '\033[33m'
    print(f'Média{cornota} {media} {cores[0]}entre 5.0 e 6.9 : RECUPERAÇÃO')
else:
    cornota = '\033[32m'
    print(f'Média{cornota} {media} {cores[0]} igual ou superior a 7.0 : APROVADO')
