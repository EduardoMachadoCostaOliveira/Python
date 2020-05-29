#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m²
a = float(input('Qual é a altura da parede? '))
b = float(input('Qual é a largura da parede? '))
print(f'A parede possui {a * b} m², portanto será necessario {(a * b) / 2} litros de tinta para pintá-la.')