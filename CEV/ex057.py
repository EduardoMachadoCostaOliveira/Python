# Faça um progama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# Minha solução
'''sexo = 0
while sexo == 0:
    # print('Digite um valor valido para sexo!')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        sexo = 'Masculino'
    elif sexo == 'F':
        sexo = 'Feminino'
    else:
        sexo = 0
        print('Digite um valor valido para sexo!')
print(f'Sexo é {sexo}')'''

# Solução Guanabara!
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
