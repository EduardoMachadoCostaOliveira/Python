#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevenso o nome do escolhido
import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
escolhido = random.choice([a1, a2, a3, a4])
print(f'O aluno escolhido foi: {escolhido}')
lista = [a1, a2, a3, a4]
escolhido2 = random.choice(lista)
print(f'O aluno escolhido2 foi: {escolhido2}')
