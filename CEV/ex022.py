#Crie um programa que leia o nome completo de uma pessoa em mostre:
#O nome com todas letras maiúsculas
#O nome com todas minusculas
#Quantas letras ao toddo (sem considerar espaço)
#Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
#print(len(nome))
#print(nome.count(' '))
print('Quantidade de letras nome completo: ', len(nome) - nome.count(' '))
nome1 = nome.split()
print('Quantidade de letras primeiro nome:', len(nome1[0]))
print('Quantidade de letras primeiro nome:', nome.find(' '))