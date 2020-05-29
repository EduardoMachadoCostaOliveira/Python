#Crie um programa que leia o nome de uma pessoa e
# diga se ela tem 'SILVA' no nome.
nome = str(input('Seu nome completo: '))
print('Tem SILVA no nome? ', 'Silva' in nome)
#Solução Guanabara
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
