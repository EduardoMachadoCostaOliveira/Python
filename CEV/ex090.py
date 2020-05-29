# (21/01/2020)
# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrututa na tela.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k.title()} é igual a {v}')

# for d in aluno:
#     print(f'{d.title()} é igual a: {aluno[d]}')
