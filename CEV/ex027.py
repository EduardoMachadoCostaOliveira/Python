#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o ultimo nome separadamente
nome = str(input('Nome completo: ')).split()
print(nome[0])
ultimo = int(len(nome)-1)
print(nome[ultimo])
print(nome[len(nome)-1])
print(len(nome))