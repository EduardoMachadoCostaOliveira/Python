# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final mostre: Média de idade do grupo
# Nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.
qtd = 2
somaidade = 0
maior = 0
nomemaior = 'nulo'
mulheresmenor = 0
for c in range(1, qtd+1):
    print(f'-----{c}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maior = idade
        nomemaior = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nomemaior = nome
    if sexo == 'F' and idade < 20:
            mulheresmenor += 1
media = somaidade / qtd
print(f'A média de idade do grupo é de {media}')
print(f'O homem mais velho tem {maior} anos e se chama {nomemaior}')
print(f'Ao todo são {mulheresmenor} mulheres com menos de 20 anos.')