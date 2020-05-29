# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechado na ordem correta.
# expr = str(input('Digite uma expressão: '))
formula = str(input('Digite uma expressão: '))
pilha = list()
for simb in formula:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
    print(pilha)
else:
    print('Sua expressão está errada!')
    print(pilha)







'''
formula = str(input('Digite uma expressão: '))
abre = formula.count('(')
fecha = formula.count(')')
if abre == fecha:
    print('A expressão digitada esta correta!')
else:
    print('A expressão digitada está incorreta!')'''

