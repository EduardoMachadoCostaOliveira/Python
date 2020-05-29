# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -Se ele ainda vai se alistar no serviço militar.
# -Se é a hora de se alistar.
# -Se já passou da hora
# Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
anoatual = datetime.date.today().year
anonascimento = int(input('Ano de nascimento: '))
sexo = str(input('Qual seu sexo: [F] ou [M}'))
idade = anoatual - anonascimento
print(f'Quem nasceu em {anonascimento} tem {idade} anos em {anoatual}')
if sexo == 'F':
    print('Sexo feminino não precisa de alistamento')
elif idade < 18:
    prazo = 18 - idade
    print(f'Você ainda vai se alistar no serviço militar. Faltam {prazo} anos!')
    ano = anoatual + prazo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    prazo = idade - 18
    print(f'Você já passou do tempo de alistamento. Ja se passaram {prazo} anos!')
    ano = anoatual - prazo
    print(f'Seu alistamento foi em {anoatual - prazo}')
else:
    print('Você está na idade para se alistar.')