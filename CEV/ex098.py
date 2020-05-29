from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -=p
        print('FIM!')


# Programa Principal
contador(i=1, f=10, p=1)
contador(i=10, f=0, p=2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)



# Faça um programa que renha uma funçao chamada contador(), que receba
# três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) de 1 até 10, de 1 em 1.
# B) De 10 até 0, de 2 em 2.
# C) Uma contagem personalizada.