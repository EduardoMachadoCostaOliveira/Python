#Faça um programa que leia uma frase pelo teclado mostre
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.upper().count("A")} vezes na frase')
#Minha solução *conta os espaços
print(frase.upper().find('A'))
print(frase.upper().rfind('A'))
#Solução Guanabara
print(f'A primeira letra A aparece na posição {frase.find("A") + 1}')
print(f'A última letra A aparece na posição {frase.rfind("A") + 1}')



