#Faça um programa que leia o comprimento do
#cateto oposto e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa
from math import pow, sqrt, hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
hipotenusa2 = hypot(cateto_oposto, cateto_adjacente)
hipotenusa3 = (cateto_oposto ** 2 + cateto_adjacente **2) ** (1/2)
print(f'A hipotenusa tem comprimento de {hipotenusa}, {hipotenusa2}, {hipotenusa3}')