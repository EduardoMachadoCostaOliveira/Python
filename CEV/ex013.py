#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Informe qual é o seu salário atual: R$ '))
novo = salário + (salário * 15/ 100)
print(f'O seu novo salário com 15% de aumento é {novo:.2f}')
