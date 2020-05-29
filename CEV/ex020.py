#O mesmo professor do exercico anterior quer
#sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
a5 = input('Aluno 5: ')
sorteio = random.sample([a1, a2, a3, a4, a5], k=5)
print(f'A ordem1 é: {sorteio}')
lista = [a1, a2, a3, a4, a5]
sorteio2 = random.choices(lista, k=5)
print(f'A ordem2 é: {sorteio2}')
random.shuffle(lista)
print(f'A ordem3 é: {lista}')
print(f'A ordem3 é: {lista}')
