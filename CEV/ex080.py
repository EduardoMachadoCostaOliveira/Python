# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.
valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        for i, v in enumerate(valores):
            if num <= v:
                valores.insert(i, num)
                print(f'Adicionado na posição {i} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')

# Primeiros racionais abaixo, mas não consegui solucionar assim:
'''valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        valores.insert(0, num)
        print('Adicionado ao final da lista...')
    else:
        for p, v in enumerate(valores):
            if num < valores[0]:
                valores.insert(0, num)
                print(f'Adicionado na posição {p} da lista...!')
            if num > valores[p]:
                valores.append(num)
                print(f'Adicionado na posição {p+1} da lista...!!')
print(f'Os valores digitados em ordem foram {valores}')'''