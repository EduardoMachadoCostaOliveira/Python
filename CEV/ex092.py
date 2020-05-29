# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastro-os(com idade) em um dicionário
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá tambem o ano de contratação e o salário.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano  # datetime.date.today().year - ano
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário R$: '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - ano
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
