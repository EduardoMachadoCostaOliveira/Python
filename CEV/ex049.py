# Refaça o Desafio 009, moostrando a tabuada de um numero que o usuario escolher,
# só que agora utilizando um laço for
num = int(input('Digite um numero para saber a Tabuada: '))
for c in range(1, 11):
    print(f'{num:2} x {c:2} = {num*c:>4}')
