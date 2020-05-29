frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
letras = ''.join(palavras)
inverso = ''
inversodois = letras[::-1]  # comecar do inicio: e terminar no fim :so que de tras pra frente
for c in range(len(letras)-1, -1, -1):
    inverso += letras[c]
print(f'O inverso de {letras} é {inverso}')
if letras == inverso:
    print('É um palindromo!')
else:
    print('Não é palindromo!')
print(f'A segunda alternativa é {inversodois}')