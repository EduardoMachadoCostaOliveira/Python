# Refaça DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# Equilátero: todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes
a = float(input('Comprimento Lado A: '))
b = float(input('Comprimento Lado B: '))
c = float(input('Comprimento Lado C: '))
if a >= b + c or b >= a + c or c >= a + b:
    print('\033[1;31mIMPOSSIVEL\033[m formar um triângulo!')
elif a == b == c:
    print('O triângulo é \033[1;34mEQUILATERO')
elif a == b or b == c or c == a :
    print('O triângulo é \033[1;34mISÓCELES')
elif a != b or b != c or c != a:
    print('O triângulo é \033[1;34mESCALENO')
#if a < b + c and b < a + c and c < a + b: