#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input("Digite um número: "))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print(f'O dobro de {n1} vale {dobro}')
print(f'O triplo de {n1} vale {triplo}')
print(f'A raiz quadrada de {n1} é igual a {raiz:.2f}')
print(pow(n1,(1/2)))
